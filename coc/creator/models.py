from uuid import uuid4

from creator.constants import GENDER
from django_enumfield.enum import Enum, EnumField

from django.db.models import (BooleanField, CASCADE, CharField, ForeignKey,
                              Model, OneToOneField, PROTECT,
                              PositiveIntegerField, SET_NULL, UUIDField)
from django.contrib.auth.models import User


def obtain_attribute_value(inv, attribute_name):
    """Look for the investigators attribute and return its value.
    Parameters:
        inv -- Investigator class instance.
        attr_name -- name of the attribute e.g. STR, DEX, ...
    """
    attr_value = filter(lambda x: x[0] == attribute_name, Attribute.items())
    attr_value = attr_value.__next__()[1]
    attr = InvestigatorAttribute.objects.filter(
        investigator_id=inv.id, attr=attr_value).first().value
    return attr


# Create your models here.
class Attribute(Enum):
    """Attribute enum."""
    STR = 1
    DEX = 2
    CON = 3
    POW = 4
    EDU = 5
    INT = 6
    APP = 7


class Tag(Model):
    """Tag class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)

    def __str__(self):
        """String representation of the object."""
        return '#{}'.format(self.title)


class Skills(Model):
    """Skills class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'skills'

    def __str__(self):
        """String representation of the object."""
        return self.title


class Occupation(Model):
    """Occupation class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=50)
    credit_rating_min = PositiveIntegerField()
    credit_rating_max = PositiveIntegerField()

    def __str__(self):
        """String representation of the object."""
        return self.title


class Investigator(Model):
    """Investigators class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1, choices=GENDER)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = PositiveIntegerField(default=18)
    # TODO: Verify if SET_NULL is the correct behaviour or PROTECT
    occupation = OneToOneField(
        Occupation, on_delete=SET_NULL, default=None, null=True)

    @property
    def dexterity(self):
        """Dexterity attribute property that obtains the value for the
        investigator.
        """
        dex = obtain_attribute_value(self, 'DEX')
        return dex

    @property
    def strength(self):
        """Strength attribute property that obtains the value for the
        investigator.
        """
        str_ = obtain_attribute_value(self, 'STR')
        return str_

    @property
    def constitution(self):
        """Constitution attribute property that obtains the value for the
        investigator.
        """
        con = obtain_attribute_value(self, 'CON')
        return con

    @property
    def power(self):
        """Power attribute property that obtains the value for the
        investigator.
        """
        pow_ = obtain_attribute_value(self, 'PWR')
        return pow_

    @property
    def size(self):
        """Size attribute property that obtains the value for the
        investigator.
        """
        siz = obtain_attribute_value(self, 'SIZ')
        return siz

    @property
    def education(self):
        """Education attribute property that obtains the value for the
        investigator.
        """
        edu = obtain_attribute_value(self, 'EDU')
        return edu

    @property
    def intelligence(self):
        """Intelligence attribute property that obtains the value for the
        investigator.
        """
        int_ = obtain_attribute_value(self, 'INT')
        return int_

    @property
    def appearance(self):
        """Appearance attribute property that obtains the value for the
        investigator.
        """
        app = obtain_attribute_value('APP')
        return app

    @property
    def health(self):
        """Health property."""
        health = (self.size + self.constitution) // 10
        return health

    @property
    def sanity(self):
        """Sanity property."""
        return self.power

    @property
    def magic_points(self):
        """Magic points property."""
        mp = self.sanity // 5
        return mp

    @property
    def move(self):
        """Move rate property, affected by certain conditions."""
        if self.strength >= self.size or self.dexterity >= self.size:
            mov = 8
        elif self.strength > self.size and self.dexterity > self.size:
            mov = 9
        else:
            mov = 7

        if self.age // 10 >= 4:
            mov = mov - ((self.age // 10) - 3)

        return mov

    @property
    def build(self):
        """Build attribute property."""
        amount = self.strength + self.size
        res = ()
        if amount <= 64:
            res = ('-2', -2)
        elif amount <= 84:
            res = ('-1', -1)
        elif amount <= 124:
            res = ('0', 0)
        elif amount <= 164:
            res = ('+1D4', 1)
        elif amount <= 204:
            res = ('+1D6', 2)
        elif amount <= 284:
            res = ('+2D6', 3)
        else:
            mod = (amount - 205) // 80
            dices = '{}D6'.format(mod+2)
            build = 3 + mod
            res = (dices, build)

        return res

    @property
    def free_skill_points(self):
        """Obtain the amount of free skill points an investigator has."""
        return self.intelligence * 2

    @property
    def occupation_skill_points(self):
        """Based on the occupation obtain the amount of free skill points."""
        skill_points = 0
        # Obtain a list of the occupation attributes.
        occ_attr = [occ for occ in OccupationAttribute.objects.filter(
                       occupation__uuid=self.occupation.uuid)]
        # Generate a diccionary with the investigators attribute data.
        inv_attr = {reg.attr.name: reg.value for reg in
                    InvestigatorAttribute.objects.filter(
                        investigator_id=self.id)}
        optionals = [0]
        # Iterate through the occupation attributes and add the skill points if
        # they are compulsory, if not check the the bigger of the optionals and
        # add it to the accumulator.
        for attr in occ_attr:
            if not attr.optional:
                skill_points += inv_attr[attr.attr.name] * attr.modifier
            else:
                optionals.append(inv_attr[attr.attr.name] * attr.modifier)
        skill_points += max(optionals)

        return skill_points

    def __str__(self):
        """String representation of the object."""
        return '{} - {}'.format(self.player, self.name)


class OccupationAttribute(Model):
    """Relation between occupation and attribute."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    attr = EnumField(Attribute)
    modifier = PositiveIntegerField()
    optional = BooleanField(default=False)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.occupation.title, self.attr, self.value)
        return title


class InvestigatorAttribute(Model):
    """Relation between investigator and its attributes."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    attr = EnumField(Attribute)
    value = PositiveIntegerField()

    @property
    def half_value(self):
        """Return half of attribute value."""
        return self.value // 2

    @property
    def fifth_value(self):
        """Return fifth of attribute value."""
        return self.value // 5

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.investigator.name, self.attr, self.value)
        return title


class InvestigatorSkills(Model):
    """Skills relation with investigator class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=PROTECT)
    value = PositiveIntegerField(default=0)

    @property
    def half_value(self):
        """Return half of attribute value."""
        return self.value // 2

    @property
    def fifth_value(self):
        """Return fifth of attribute value."""
        return self.value // 5

    class Meta:
        verbose_name_plural = 'investigator skills'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.investigator.name, self.skill.title, self.value)
        return title


class OccupationSkills(Model):
    """Skills relation with Occupation."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=PROTECT)

    class Meta:
        verbose_name_plural = 'occupation skills'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.occupation.title, self.skill.title, self.value)
        return title
