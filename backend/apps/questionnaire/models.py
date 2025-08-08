from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from apps.core.models import Base, Historical
from apps.sth.models import Stage
from apps.practitionerseye.models import Element
from apps.cseframework.models import Process
from apps.continuousstar.models import ContinuousActivity
from apps.employee.models import Employee
from apps.organization.models import Organization


class AdoptedLevel(Base):
    """"""

    percentage = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)



    class Meta:
        db_table = 'adoptedlevel'

class Statement(Base):
    """"""

    code = models.CharField(max_length=300, null=True, blank=True)
    statement = models.CharField(max_length=300, null=True, blank=True)


    sth_stage = models.ForeignKey('apps_sth.Stage', blank=True, null=True, on_delete=models.CASCADE, related_name="sth_stage_%(class)s")
    pe_element = models.ForeignKey('apps_practitionerseye.Element', blank=True, null=True, on_delete=models.CASCADE, related_name="pe_element_%(class)s")
    fcse_processes = models.ManyToManyField('apps_cseframework.Process')
    continuous_activity = models.ForeignKey('apps_continuousstar.ContinuousActivity', blank=True, null=True, on_delete=models.CASCADE, related_name="continuous_activity_%(class)s")

    class Meta:
        db_table = 'statement'

class FeedbackQuestionnaire(Historical):
    """"""

    collected_date = models.DateField(null=True, blank=True)



    class Meta:
        db_table = 'feedbackquestionnaire'

class Questionnaire(Historical):
    """"""

    applied_date = models.DateField(null=True, blank=True)
    document = models.FileField(null=True, blank=True)


    employee = models.ForeignKey('apps_employee.Employee', blank=True, null=True, on_delete=models.CASCADE, related_name="employee_%(class)s")

    class Meta:
        db_table = 'questionnaire'

class QuestionnaireExcel(Questionnaire):
    """"""



    feedback = models.ForeignKey(FeedbackQuestionnaire, blank=True, null=True, on_delete=models.CASCADE, related_name="feedback_%(class)s")

    class Meta:
        db_table = 'questionnaireexcel'

class Answer(Historical):
    """"""

    comment = models.CharField(max_length=300, null=True, blank=True)


    questionnaire = models.ForeignKey(Questionnaire, blank=True, null=True, on_delete=models.CASCADE, related_name="questionnaire_%(class)s")
    adopted_level = models.ForeignKey(AdoptedLevel, blank=True, null=True, on_delete=models.CASCADE, related_name="adopted_level_%(class)s")
    statement = models.ForeignKey(Statement, blank=True, null=True, on_delete=models.CASCADE, related_name="statement_%(class)s")
    organization = models.ForeignKey('apps_organization.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name="organization_%(class)s")

    class Meta:
        db_table = 'answer'

