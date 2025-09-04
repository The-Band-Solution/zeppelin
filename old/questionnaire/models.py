from django.core.exceptions import ValidationError
from django.db import models
from sth.models import Stage
from practitioners_eye.models import Element
from cse_framework.models import Process
from core.models import Base
from organization.models import Organization 
from employee.models import  Employee
from continuous_star.models import ContinuousActivity

class AdoptedLevel(Base):

    """
    Represents an adopted level`.
    """

    name = models.CharField(max_length=200,help_text= "name")
    description = models.TextField(help_text= "description")
    percentage = models.IntegerField(help_text= "percentage")

    class meta:
        db_table = 'adopted_level'
    
    def __str__(self):
        return self.name

    
class Statement(Base):

    """
    Represents a statement related to :model:`sth.stage`, related to :model:`practitioners_eye.element` and related to :model:`cse_framework.process`
    """

    code = models.CharField(max_length=200, null=True, blank=True)
    statement = models.TextField()
    sth_stage = models.ForeignKey(Stage, on_delete=models.CASCADE,null=True, blank=True)
    pe_element = models.ForeignKey(Element, on_delete=models.CASCADE,null=True, blank=True)
    fcse_processes = models.ManyToManyField(Process)
    continuous_activity = models.ForeignKey(ContinuousActivity, on_delete=models.CASCADE,null=True, blank=True)

    class meta:
        db_table = 'statement'
    
    def __str__(self):
        return self.code + "-"+ self.statement

class FeedbackQuestionnaire(Base):
    feedback_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.feedback_date)

class Questionnaire(Base):
    
    """
    Represents a Questionnaire related to :model:`questionnaire.employee`.
    """
    
    applied_date = models.DateTimeField(null=True, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
   
    class meta:
        db_table = 'questionnaire'
    
    def __str__(self):
       return self.document.name


class QuestionnaireExcel(Questionnaire):

    feedback_questionnaire = models.ForeignKey(FeedbackQuestionnaire, on_delete=models.CASCADE, null=True, blank=True)


class QuestionnaireGoogleForms(Questionnaire):
    pass

class Answer(Base):

    """
    Represents a answer of questionnaire related to :model:`questionnaire.Questionnaire`, related to :model:`questionnaire.AdoptedLevel` and :model:`questionnaire.Statement`.
    """

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, blank=True, null=True)
    adopted_level = models.ForeignKey(AdoptedLevel, on_delete=models.CASCADE)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    comment = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
   

    class meta:
        db_table = 'answer'
    
    def __str__(self):
        return self.statement.code 
