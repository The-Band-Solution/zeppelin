from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel
from apps.core.models import Base, Historical
from apps.organization.models import Organization
from apps.sth.models import Stage


class AcademicDegreeCategory(Base):
    """"""




    class Meta:
        db_table = 'academicdegreecategory'

class AcademicDegree(Base):
    """"""



    academic_degree_category = models.ForeignKey(AcademicDegreeCategory, blank=True, null=True, on_delete=models.CASCADE, related_name="academic_degree_category_%(class)s")

    class Meta:
        db_table = 'academicdegree'

class AcademicDegreeStatus(Base):
    """"""




    class Meta:
        db_table = 'academicdegreestatus'

class KnwoledgeLevel(Base):
    """"""

    value = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)



    class Meta:
        db_table = 'knwoledgelevel'

class ExperienceLevel(Base):
    """"""

    value = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)



    class Meta:
        db_table = 'experiencelevel'

class Position(Base):
    """"""




    class Meta:
        db_table = 'position'

class Employee(Base):
    """"""

    e_mail = models.EmailField(null=True, blank=True)
    role = models.CharField(max_length=300, null=True, blank=True)


    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE, related_name="position_%(class)s")
    organization = models.ForeignKey('apps_organization.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name="organization_%(class)s")

    class Meta:
        db_table = 'employee'

class EmployeeKnowledge(Historical):
    """"""



    academic_degree = models.ForeignKey(AcademicDegree, blank=True, null=True, on_delete=models.CASCADE, related_name="academic_degree_%(class)s")
    academic_degree_status = models.ForeignKey(AcademicDegreeStatus, blank=True, null=True, on_delete=models.CASCADE, related_name="academic_degree_status_%(class)s")
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name="employee_%(class)s")

    class Meta:
        db_table = 'employeeknowledge'

class SthStageKnwoledgeLevel(Historical):
    """"""



    stage = models.ForeignKey('apps_sth.Stage', blank=True, null=True, on_delete=models.CASCADE, related_name="stage_%(class)s")
    Knwoledge_level = models.ForeignKey(KnwoledgeLevel, blank=True, null=True, on_delete=models.CASCADE, related_name="knwoledge_level_%(class)s")
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name="employee_%(class)s")

    class Meta:
        db_table = 'sthstageknwoledgelevel'

class SthStageExperienceLevel(Historical):
    """"""



    stage = models.ForeignKey('apps_sth.Stage', blank=True, null=True, on_delete=models.CASCADE, related_name="stage_%(class)s")
    experience_level = models.ForeignKey(ExperienceLevel, blank=True, null=True, on_delete=models.CASCADE, related_name="experience_level_%(class)s")
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name="employee_%(class)s")

    class Meta:
        db_table = 'sthstageexperiencelevel'

class Team(Base):
    """"""



    organization = models.ForeignKey('apps_organization.Organization', blank=True, null=True, on_delete=models.CASCADE, related_name="organization_%(class)s")
    responsible = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE, related_name="responsible_%(class)s")

    class Meta:
        db_table = 'team'

