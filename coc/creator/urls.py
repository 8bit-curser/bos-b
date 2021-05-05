from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path(
        'detail/<slug:id>/<str:model_name>', 
        views.GenericViews.record_detail,
        name='detail'
    ),
    path(
        'list/<str:model_type>',
        views.GenericViews.generic_model_list,
        name="listing"
    ),
     #Add endpoints
    path(
        'add_phobia',
        views.ManiaPhobiaInvestigatorView.add_phobia,
        name='phobia_add'
    ),
    path(
        'add_mania',
        views.ManiaPhobiaInvestigatorView.add_mania,
        name='mania_add'
    ),
    path(
        'mania/<slug:inv>/<slug:mania>/remove',
        views.ManiaPhobiaInvestigatorView.remove_mania,
        name='mania-rem'
    ),
    path(
        'phobia/<slug:inv>/<slug:phobia>/remove',
        views.ManiaPhobiaInvestigatorView.remove_phobia,
        name='phobia-rem'),
    #generate random inv
    path(
        'random',
        views.GeneralInvestigatorViews.generate_random_investigator),
    # Core endpoints
    path(
        '<slug:inv>',
        views.GeneralInvestigatorViews.get_investigators_data,
        name="inv_data"
    ),
    path(
        '<slug:inv>/info',
        views.GeneralInvestigatorViews.investigators_basic_info,
        name="basic_info"
    ),
    path(
        '<slug:inv>/attrs',
        views.AttributesInvestigatorViews.investigators_attributes,
        name="inv_attrs"
    ),
    path(
        '<slug:inv>/attrs/update',
        views.AttributesInvestigatorViews.investigators_attribute_update,
        name="inv_attr_update"
    ),
    path(
        '<slug:inv>/derivative_attrs',
        views.AttributesInvestigatorViews.investigators_deriv_attrs,
        name="inv_deriv_attrs"
    ),
    path(
        '<slug:inv>/portrait',
        views.GeneralInvestigatorViews.get_investigators_portrait,
        name="inv_portrait"
    ),
    # Skills endpoints
    path(
        '<slug:inv>/skills',
        views.SkillsInvestigatorViews.get_investigators_skills,
        name="inv_skills"
    ),
    path(
        '<slug:inv>/skills_update',
        views.SkillsInvestigatorViews.update_investigators_skills,
        name="inv_skills_update"
    ),
    path(
        '<slug:inv>/skill_update',
        views.SkillsInvestigatorViews.update_investigators_skill,
        name="inv_skill_update"
    ),
    path(
        '<slug:inv>/skills_shuffle',
        views.SkillsInvestigatorViews.investigators_skills_shuffle,
        name="inv_skills_shuffle"
    ),
    path(
        '<slug:inv>/skills_reset',
        views.SkillsInvestigatorViews.investigators_skills_reset,
        name="inv_skills_reset"
    ),
    # Items endpoints
    path(
        '<slug:inv>/weapons',
        views.ItemsInvestigatorViews.get_investigators_weapons,
        name="inv_weapons"
    ),
    path(
        '<slug:inv>/gear',
        views.ItemsInvestigatorViews.get_investigators_gear,
        name="inv_gear"
    ),
    path(
        'inventory/<slug:inventory>/remove',
        views.ItemsInvestigatorViews.remove_investigators_gear,
        name="inv_gear_remove"
    ),
    path(
        'inventory/<slug:inventory>/edit',
        views.ItemsInvestigatorViews.edit_investigators_gear,
        name="inv_gear_edit"
    ),
    # Backstory endpoints
    path(
        '<slug:inv>/manias_phobias',
        views.BackstoryInvestigatorViews.get_investigators_manias_and_phobias,
        name="inv_manias_phobias"
    ),
    path(
        '<slug:inv>/arcane',
        views.BackstoryInvestigatorViews.get_investigators_arcane,
        name="inv_arcane"
    ),
    path(
        '<slug:inv>/backstory',
        views.BackstoryInvestigatorViews.get_investigators_backstory,
        name="inv_backstory"
    ),
    path(
        '<slug:inv>/backstory/update',
        views.BackstoryInvestigatorViews.update_investigators_backstory,
        name="inv_backstory_update"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
