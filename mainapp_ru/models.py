from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class HomeRu(models.Model):
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
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.name


class InnerHomeRu(models.Model):
    outer_relation = models.ForeignKey(HomeRu, on_delete=models.CASCADE)
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
        verbose_name_plural = "Вложенные страницы"

    def __str__(self):
        return self.name


class ClientAssesment(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('0', 'Выбрать...'),
    ('1','Брак аннулирован'),
    ('2','Гражданский брак'),
    ('3','В разводе / Separated'),
    ('4','Legally Separated'),
    ('5','В браке'),
    ('6','Never Married / Single/ Холост'),
    ('7','Вдовец / вдова'),
    )

    CHOICE_IMMIGRATION_STATUS = (
    ('0', 'Выбрать...'),
    ("1", "Not Applicable"),
    ("2", "Гость"),
    ("3", "Student"),
    ("4", "Worker"),
    )
    CHOICE_EDU_LEVEL = (
    ('0','Выбрать...'),
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
    ('Y', 'Да'),
    ('N', 'Нет'),
    )
    CHOICE_YES_NO_N = (
    ('NO', 'None'),
    ('Y', 'Да'),
    ('N', 'Нет'),
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
    off_lang_en = models.CharField(max_length=40)
    off_lang_fr = models.CharField(max_length=40)
    work_exp_canada = models.TextField(max_length=120)
    # work_exp_home = models.TextField(max_length=120)
    canadian_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO,default='N')
    valid_job = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    nomin_cert = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    partner_status_of_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO_N, default='NO')
    partner_track = models.CharField(max_length=3, choices=CHOICE_YES_NO_N, default='NO')
    partner_edu = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL,  default='0')
    partner_work_exp = models.TextField(max_length=120, blank=True)
    partner_lang = models.CharField(max_length=40, blank=True)
    sibling_in_canada = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    memo = models.TextField(blank=True)
