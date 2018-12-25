from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from datetime import datetime
# from ckeditor.fields import RichTextField


CHOICE_YES_NO = (
('Y', 'Yes'),
('N', 'No'),
)
CHOICE_LANG_EN_LEVEL = (
('0','Please Choose...'),
("1", "Beginner"),
("2", "Intermediate"),
("3", "Advanced"),
("4", "Fluent"),
)
CHOICE_LANG_LEVEL = (
('0','Please Choose...'),
("1", "Not applicable"),
("2", "Beginner"),
("3", "Intermediate"),
("4", "Advanced"),
("5", "Fluent"),
)
# Create your models here.

class HomeEn(models.Model):
    name = models.CharField(max_length=30, blank=True)
    h1 = models.CharField(max_length=33, blank=True)
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
    link = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.name


class InnerHomeEn(models.Model):
    outer_relation = models.ForeignKey(HomeEn, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    h1 = models.CharField(max_length=33, blank=True)
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
    link = models.TextField(blank=True)


    class Meta():
        verbose_name_plural = "Nested Pages"

    def __str__(self):
        return self.name

class ClientAssesment(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('0', 'Please Choose...'),
    ('1','Annulled Marriage'),
    ('2','Common-Law'),
    ('3','Divorced / Separated'),
    ('4','Legally Separated'),
    ('5','Married'),
    ('6','Never Married / Single'),
    ('7','Widowed'),
    )

    CHOICE_IMMIGRATION_STATUS = (
    ('0', 'Please Choose...'),
    ("1", "Not Applicable"),
    ("2", "Visitor"),
    ("3", "Student"),
    ("4", "Worker"),
    )
    CHOICE_EDU_LEVEL = (
    ('0','Please Choose...'),
    ("1", "None, or less then secondary (high school)"),
    ("2", "Secondary diploma (High school Diploma)"),
    ("3", "One-year program at a university, college, trade or technical school, or other institute"),
    ("4", "Two-year program at a university, college, trade or technical school, or other institute"),
    ("5", "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)"),
    ("6", "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years"),
    ("7", "Master's degree, or professional degree needed to practice in a licensed profession"),
    ("8", "Doctoral level university degree (PhD)"),
    )


    travel_doc_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    address = models.CharField(max_length=80, blank=True)
    contact_number = PhoneNumberField(blank=False)
    marital_status = models.CharField(max_length=22,choices=CHOICE_MARITAL_STATUS, default='0')
    country = models.CharField(max_length=45, blank=False)
    dob = models.DateField()
    immigration_status = models.CharField(max_length=14,choices=CHOICE_IMMIGRATION_STATUS, default='0', error_messages={'required': (u'Waehlen Sie die Zahlungsart!'), 'invalid': (u'Waehlen Sie die Zahlungsart!')})
    edu_level = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL, default='0')
    canadian_dipl = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    school_progr_name = models.TextField(max_length=80,blank=True)
    # off_lang_en = models.CharField(max_length=40)
    off_lang_en_level = models.CharField(max_length=15,choices=CHOICE_LANG_EN_LEVEL, default='0')
    # off_lang_fr = models.CharField(max_length=40)
    off_lang_fr_level = models.CharField(max_length=15,choices=CHOICE_LANG_LEVEL, default='0')
    work_exp_canada = models.TextField(max_length=120)
    # work_exp_home = models.TextField(max_length=120)
    canadian_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO,default='N')
    valid_job = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    nomin_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    partner_status_of_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    partner_track = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    partner_edu = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL,  default='1')
    partner_work_exp = models.TextField(max_length=120, blank=True)
    partner_lang = models.CharField(max_length=40, blank=True)
    sibling_in_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    memo = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Assesments forms"

    def __str__(self):
        return self.name

class Education(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('0', 'Please Choose...'),
    ('1','Married'),
    ('2','Common-Law'),
    ('3','Single / Divorced'),
    )
    CHOICE_EDU_LEVEL = (
    ('0','Please Choose...'),
    ("1", "None, or less then secondary (high school)"),
    ("2", "Secondary diploma (High school Diploma)"),
    ("3", "College certificate"),
    ("4", "Bachelor's degree"),
    ("5", "Master's degree"),
    ("6", "Doctoral university degree (PhD)"),
    )
    CHOICE_PROGRAM = (
    ('0','Please Choose...'),
    ("1", "English language courses"),
    ("2", "French language courses"),
    ("3", "Kids and teens camp programs"),
    ("4", "College or university preparation"),
    ("5", "University"),
    ("5", "Postsecondary diploma"),
    ("5", "Masters degree"),
    ("5", "PhD"),
    )
    travel_doc_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField(max_length=30, blank=False)
    contact_number = PhoneNumberField(blank=False)
    citizenship = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=45, blank=False)
    dob = models.DateField()
    marital_status = models.CharField(max_length=22,choices=CHOICE_MARITAL_STATUS, default='0')
    edu_level = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL, default='0')
    off_lang_en_level = models.CharField(max_length=15,choices=CHOICE_LANG_EN_LEVEL, default='0')
    off_lang_fr_level = models.CharField(max_length=15,choices=CHOICE_LANG_LEVEL, default='0')
    en_fr_cert = models.TextField(blank=True)
    int_program = models.CharField(max_length=15,choices=CHOICE_PROGRAM, default='0')
    plan_date = models.DateField()
    pref_province = models.CharField(max_length=40, blank=True)
    plan_budget = models.CharField(max_length=15, blank=False)
    visa_rejected = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    memo = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Education forms"

    def __str__(self):
        return self.name
