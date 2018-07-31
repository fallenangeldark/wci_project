from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


# Create your models here.

class HomeEn(models.Model):
    name = models.CharField(max_length=30, blank=True)
    h1 = models.CharField(max_length=30, blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.name


class InnerHomeEn(models.Model):
    outer_relation = models.ForeignKey(HomeEn, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    h1 = models.CharField(max_length=30, blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    paragraph4 = models.TextField(blank=True)
    paragraph5 = models.TextField(blank=True)
    paragraph6 = models.TextField(blank=True)
    paragraph7 = models.TextField(blank=True)
    paragraph8 = models.TextField(blank=True)
    paragraph9 = models.TextField(blank=True)
    paragraph10 = models.TextField(blank=True)
    paragraph11 = models.TextField(blank=True)
    paragraph12 = models.TextField(blank=True)
    paragraph13 = models.TextField(blank=True)


    class Meta():
        verbose_name_plural = "Nested Pages"

    def __str__(self):
        return self.name

class ClientAssesment(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('1','Annulled Marriage'),
    ('2','Common-Law'),
    ('3','Divorced / Separated'),
    ('4','Legally Separated'),
    ('5','Married'),
    ('6','Never Married / Single'),
    ('7','Widowed'),
    )

    CHOICE_IMMIGRATION_STATUS = (
    ("1", "Not Applicable"),
    ("2", "Visitor"),
    ("3", "Student"),
    ("4", "Worker"),
    )
    CHOICE_EDU_LEVEL = (
    ("1", "None, or less then secondary (high school)"),
    ("2", "Secondary diploma (High school Diploma)"),
    ("3", "One-year program at a university, college, trade or technical school, or other institute"),
    ("4", "Two-year program at a university, college, trade or technical school, or other institute"),
    ("5", "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"),
    ("6", "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years"),
    ("7", "Master's degree, or professional degree needed to practice in a licensed profession"),
    ("8", "Doctoral level university degree (PhD)"),
    )
    CHOICE_YES_NO = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    CHOICE_YES_NO_N = (
    ('NO', 'None'),
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    name = models.CharField(max_length=35, blank=False, default='')
    travel_doc_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    address = models.CharField(max_length=50, blank=True)
    contact_number = PhoneNumberField(blank=False)
    marital_status = models.CharField(max_length=22,choices=CHOICE_MARITAL_STATUS, default='6')
    nationality = models.CharField(max_length=25)
    dob = models.DateField()
    immigration_status = models.CharField(max_length=14,choices=CHOICE_IMMIGRATION_STATUS, default='1')
    edu_level = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL, default='1')
    canadian_dipl = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    school_progr_name = models.TextField(blank=True)
    off_lang_en = models.CharField(max_length=40)
    off_lang_fr = models.CharField(max_length=40)
    work_exp_canada = models.TextField()
    work_exp_home = models.TextField()
    canadian_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO,default='N')
    valid_job = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    nomin_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    partner_status_of_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO_N, default='NO')
    partner_track = models.CharField(max_length=3, choices=CHOICE_YES_NO_N, default='NO')
    partner_edu = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL, blank=True)
    partner_work_exp = models.TextField(blank=True)
    partner_lang = models.CharField(max_length=40, blank=True)
    sibling_in_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    memo = models.TextField()
