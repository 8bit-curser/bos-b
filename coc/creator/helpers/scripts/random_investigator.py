"""Example call of script from /coc/coc location inside container.

python3 creator/helpers/scripts/random_investigator.py"
"""
from os import environ
from random import randint

from django.core.wsgi import get_wsgi_application

APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'creator'
]

environ.setdefault("DJANGO_SETTINGS_MODULE", "coc.settings")
environ.setdefault("INSTALLED_APPS", str(APPS))
get_wsgi_application()

from django.contrib.auth.models import User

from creator.enums import Attribute
from creator.models import (Investigator, InvestigatorAttribute,
                            InvestigatorSkills, Occupation, OccupationAttribute,
                            OccupationSkills, Skills)
from creator.helpers.model_helpers import attribute_roller, roller_stats


def calc_proff_points(attribute: int, mod: int, inv: Investigator):
    """Calculate the amount of points that correspond to certain attribute"""
    inv_attrs = InvestigatorAttribute.objects.filter(
        attr=attribute,
        investigator=inv
    ).first()
    res = inv_attrs.value * mod
    return res


def occ_skill_picker(occ_skills: list, inv: Investigator):
    """Pick a random skill from an occupation skill list."""
    choice = randint(0, len(occ_skills)-1)
    skill_pick = occ_skills[choice]
    ret = None
    current_skills_cat = InvestigatorSkills.objects.filter(
        category=skill_pick.category,
        investigator=inv
    )
    if skill_pick.optional:
        if len(current_skills_cat) < skill_pick.limit:
            ret = skill_pick
        else:
            return occ_skill_picker(occ_skills, inv)
    else:
        ret = skill_pick
    return ret


def free_skill_picker(skills: list):
    """Pick a random skill from an occupation skill list."""
    choice = randint(0, len(skills)-1)
    skill_pick = skills[choice]
    ret = skill_pick

    return ret


def load_investigator_attributes(inv: Investigator):
    """Seed an investigator with attributes."""
    # Obtain list of attibutes with their ids.
    attrs = Attribute.items()

    # Seed attributes
    for attr in attrs:
        inv_attr = InvestigatorAttribute(
            investigator=inv,
            attr=attr[1],
            value=attribute_roller(attr[1])
        )
        inv_attr.save()


def amount(points_available: int, limit: int):
    """Recursively find an adequate value."""
    val = randint(1, 99 - limit)
    if (points_available - val) >= 0:
        ret = val
    else:
        ret = amount(points_available, limit)
    return ret


def occ_point_assigner(max_points: int, occ_skills: list, inv: Investigator):
    """Assign points for the skills related to occupations."""
    # Assing profession points
    while max_points > 0:
        occ_skill = occ_skill_picker(occ_skills, inv)
        # Determine if the skill has already been assigned to the investigator.
        inv_skill = InvestigatorSkills.objects.filter(
            investigator=inv,
            skill=occ_skill.skill
        )
        # If not create a new record else update the new one.
        if inv_skill.first() is None:
            # Remember not to surpass 99 limit
            val = amount(max_points, occ_skill.skill.default_value)
            record = InvestigatorSkills(
                investigator=inv,
                skill=occ_skill.skill,
                value=occ_skill.skill.default_value + val,
                category=occ_skill.category
            )
            record.save()
            max_points -= val
        else:
            record = inv_skill.first()
            # Remember not to surpass the 99 limit
            val = amount(max_points, record.value)
            if (record.value + val) < 100:
                record.value += val
                record.save()
                max_points -= val


def free_point_assigner(max_points: int, skills: list, inv: Investigator):
    """Assign points to any skill."""
    while max_points > 0:
        skill = free_skill_picker(skills)
        # Determine if the skill has already been assigned to the investigator.
        inv_skill = InvestigatorSkills.objects.filter(
            investigator=inv,
            skill=skill
        )
        # If not create a new record else update the new one.
        if inv_skill.first() is None:
            # Remember not to surpass 99 limit
            val = amount(max_points, skill.default_value)
            record = InvestigatorSkills(
                investigator=inv,
                skill=skill,
                value=skill.default_value + val,
                category='4'
            )
            record.save()
            max_points -= val
        else:
            record = inv_skill.first()
            # Remember not to surpass the 99 limit
            val = amount(max_points, record.value)
            if (record.value + val) < 100:
                record.value += val
                record.save()
                max_points -= val


def main():
    """Main wrapper."""
    # Pick a random occupation
    occ = Occupation.objects.get(pk=randint(1, 117))
    attrs = {
        "user": User.objects.get(pk=1),
        "name": "John Doe",
        "player": "John Doe player",
        "sex": "M",
        "residence": "Providence",
        "birthplace": "Misissippi",
        "age": randint(15, 90),
        "occupation": occ,
        "ideologies": "Atheist",
        "sanity": roller_stats(3),
        "luck": roller_stats(3)
    }
    inv = Investigator(**attrs)
    inv.save()
    load_investigator_attributes(inv)
    # Load derivative statuses
    inv.health = inv.max_health
    inv.sanity = inv.power
    inv.save()
    # Obtain skills and occupations related to the investigator occupation.
    occ_skills = OccupationSkills.objects.filter(occupation=inv.occupation)
    proff_points = inv.occupation_skill_points
    # Assign points to occupation skills
    occ_point_assigner(proff_points, occ_skills, inv)
    free_skills = Skills.objects.all()
    free_point_assigner(inv.free_skill_points, free_skills, inv)


if __name__ == '__main__':
    main()

