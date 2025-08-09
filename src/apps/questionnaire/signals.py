from .models import AdoptedLevel, Statement, FeedbackQuestionnaire, Questionnaire, QuestionnaireExcel, Answer
from django.db.models.signals import (
    pre_init,   post_init,
    pre_save,   post_save,
    pre_delete, post_delete,
    m2m_changed
)
from django.dispatch import receiver
from django.contrib.auth.models import Group

## Signals from AdoptedLevel
@receiver(pre_init, sender=AdoptedLevel)
def pre_init_adoptedlevel(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=AdoptedLevel)
def post_init_adoptedlevel(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=AdoptedLevel)
def pre_save_adoptedlevel(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=AdoptedLevel)
def post_save_adoptedlevel(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=AdoptedLevel)
def pre_delete_adoptedlevel(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=AdoptedLevel)
def post_delete_adoptedlevel(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=AdoptedLevel)
def m2m_changed_adoptedlevel(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from Statement
@receiver(pre_init, sender=Statement)
def pre_init_statement(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Statement)
def post_init_statement(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Statement)
def pre_save_statement(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Statement)
def post_save_statement(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Statement)
def pre_delete_statement(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Statement)
def post_delete_statement(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Statement)
def m2m_changed_statement(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from FeedbackQuestionnaire
@receiver(pre_init, sender=FeedbackQuestionnaire)
def pre_init_feedbackquestionnaire(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=FeedbackQuestionnaire)
def post_init_feedbackquestionnaire(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=FeedbackQuestionnaire)
def pre_save_feedbackquestionnaire(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=FeedbackQuestionnaire)
def post_save_feedbackquestionnaire(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=FeedbackQuestionnaire)
def pre_delete_feedbackquestionnaire(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=FeedbackQuestionnaire)
def post_delete_feedbackquestionnaire(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=FeedbackQuestionnaire)
def m2m_changed_feedbackquestionnaire(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from Questionnaire
@receiver(pre_init, sender=Questionnaire)
def pre_init_questionnaire(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Questionnaire)
def post_init_questionnaire(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Questionnaire)
def pre_save_questionnaire(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Questionnaire)
def post_save_questionnaire(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Questionnaire)
def pre_delete_questionnaire(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Questionnaire)
def post_delete_questionnaire(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Questionnaire)
def m2m_changed_questionnaire(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from QuestionnaireExcel
@receiver(pre_init, sender=QuestionnaireExcel)
def pre_init_questionnaireexcel(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=QuestionnaireExcel)
def post_init_questionnaireexcel(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=QuestionnaireExcel)
def pre_save_questionnaireexcel(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=QuestionnaireExcel)
def post_save_questionnaireexcel(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=QuestionnaireExcel)
def pre_delete_questionnaireexcel(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=QuestionnaireExcel)
def post_delete_questionnaireexcel(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=QuestionnaireExcel)
def m2m_changed_questionnaireexcel(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass


## Signals from Answer
@receiver(pre_init, sender=Answer)
def pre_init_answer(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Answer)
def post_init_answer(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Answer)
def pre_save_answer(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Answer)
def post_save_answer(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Answer)
def pre_delete_answer(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Answer)
def post_delete_answer(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Answer)
def m2m_changed_answer(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass

