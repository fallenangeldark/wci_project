from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor.fields import RichTextField



# Create your models here.

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

class HomeRu(models.Model):
    # body = RichTextUploadingField(config_name='default', blank=True)
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
    link = models.TextField(blank=True)

    class Meta():
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.name


class InnerHomeRu(models.Model):
    outer_relation = models.ForeignKey(HomeRu, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    h1 = models.CharField(max_length=35, blank=True)
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
        verbose_name_plural = "Вложенные страницы"

    def __str__(self):
        return self.name


class ClientAssesment(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('0', 'Выбрать...'),
    ('1','Брак признан недействительным'),
    ('2','В гражданском браке'),
    ('3','В разводе'),
    ('4','Не в браке'),
    ('5','В браке'),
    ('6','Вдовец / вдова'),
    )

    CHOICE_IMMIGRATION_STATUS = (
    ('0', 'Выбрать...'),
    ("1", "Туристическая"),
    ("2", "Студенческая"),
    ("3", "Рабочая"),
    ("4", "Нет"),
    )
    CHOICE_EDU_LEVEL = (
    ('0','Выбрать...'),
    ("1", "Школьное образование"),
    ("2", "Неоконченное высшее"),
    ("3", "Cреднее специальное"),
    ("4", "Бакалавриат"),
    ("5", "Магистратура"),
    ("6", "Кандидат наук"),
    )
    CHOICE_LANG_LEVEL = (
    ('0','Выбрать...'),
    ("1", "Не владею"),
    ("2", "Начальный"),
    ("3", "Средний"),
    ("4", "Выше среднего"),
    ("5", "Свободное"),
    )
    CHOICE_YES_NO = (
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
    immigration_status = models.CharField(max_length=14,choices=CHOICE_IMMIGRATION_STATUS, default='0')
    edu_level = models.CharField(max_length=118,choices=CHOICE_EDU_LEVEL, default='0')
    canadian_dipl = models.CharField(max_length=3, choices=CHOICE_YES_NO, default='N')
    school_progr_name = models.TextField(max_length=80,blank=True)
    # off_lang_en = models.CharField(max_length=40)
    off_lang_en_level = models.CharField(max_length=15,choices=CHOICE_LANG_LEVEL, default='0')
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

class Education(models.Model):

    CHOICE_MARITAL_STATUS = (
    ('0', 'Выбрать...'),
    ('1','В браке'),
    ('2','В гражданском браке'),
    ('3','Не в браке'),
    )
    CHOICE_EDU_LEVEL = (
    ('0','Выбрать...'),
    ("1", "Среднее"),
    ("2", "Среднее специальное"),
    ("3", "Высшее"),
    ("4", "Бакалавриат"),
    ("5", "Аспирантура / Докторантура"),
    )
    CHOICE_PROGRAM = (
    ('0','Выбрать...'),
    ("1", "Курсы английского языка"),
    ("2", "Курсы французского языка"),
    ("3", "Каникулярные программы для детей и подростков"),
    ("4", "Среднее образование"),
    ("5", "Подготовка к поступлению в вуз"),
    ("6", "Высшее образование"),
    ("7", "Последипломное образование"),
    ("8", "Магистратура"),
    ("9", "Докторантура"),
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
