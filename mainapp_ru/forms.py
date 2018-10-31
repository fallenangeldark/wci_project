from django import forms
from .models import ClientAssesment, Education


class ClientAssesmentRu(forms.ModelForm):

    class Meta:
        model = ClientAssesment
        fields = '__all__'

        labels = {
        'travel_doc_name': 'ФИО* ',
        'email': 'Email* ',
        'address': 'Адресс ',
        'contact_number': 'Контактный номер* ',
        'marital_status': 'Семейное положение* ',
        'country': 'Страна проживания* ',
        'dob': 'Дата рождения* ',
        'immigration_status': 'Есть ли у вас виза? *',
        'edu_level': 'Какой ваш самый высокий уровень образования? *',
        'school_progr_name': 'Если Да, то укажите название учебного заведения и программы.',
        'off_lang_en_level': 'Укажите уровень владения Английским* ',
        'off_lang_fr_level': 'Укажите уровень владения Французским* ',
        'work_exp_canada': 'Укажите ваш опыт работы в Канаде по классификации NOC (0, A или B), должность и продолжительность работы:',
        # 'work_exp_home': 'Work Experience (Full-Time) in your country in the past 10 years (NOC 0, A or B - Please provide Job title and Duration.)',
        'partner_edu': 'Укажите самый высокий уровень образования вашего партнера:',
        'partner_work_exp': 'Пожалуйста, укажите опыт работы вашего партнера в Канаде по классификации NOC (0, A или B)',
        'partner_lang': 'Укажите уровень владения вашим партнером официальными языками и результаты тестирования при их наличии:',
        'canadian_dipl': 'Есть ли у вас какие-либо дипломы Канадского образования?',
        'canadian_cert':'Есть ли у вас квалификационный сертификат Skilled Trade occupations?',
        'valid_job': 'Есть ли у вас приглашение на работу от канадского работодателя?',
        'nomin_cert': 'Есть ли у вас номинационный сертификат?',
        'partner_status_of_canada': 'Является ли ваш партнер гражданином или постоянным жителем (permanent resident) Канады?',
        'partner_track': 'Приедет ли ваш партнер в Канаду?',
        'sibling_in_canada': 'Есть ли у вас родные братья или сестры старше 18 лет, являющиеся канадскими гражданами или постоянными жителями (permanent resident)?',
        'memo': 'Дополнительная информация',
        }
        widgets = {
        'travel_doc_name': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{10,60}'}),
        'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'pattern': '\w{1,}[-]{0,10}\w{0,}@\w{1,}[-]{0,3}\w{0,}\.\w{1,}'}),
        'address': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{10,80}'}),
        'contact_number': forms.TextInput(attrs={'placeholder': '+7XXXXXXXXXX или +380XXXXXXXXX и т.д.', 'pattern': '\+\d{10,19}'}),
        'country': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,45}'}),
        'dob': forms.DateInput(attrs={'placeholder': 'дд.мм.гггг', 'pattern': '(([0-2]{1}[0-9]{1})|([3][0-1]))\.((0{1}[0-9]{1})|(1{1}[0-2]{1}))\.((19[3-9][0-9])|(20[0-1][1-8]))'}),
        'school_progr_name':forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{5,80}'}),
        'canadian_dipl': forms.RadioSelect(attrs={'class': 'radio'}),
        'canadian_cert': forms.RadioSelect(attrs={'class': 'radio'}),
        'valid_job': forms.RadioSelect(attrs={'class': 'radio'}),
        'nomin_cert': forms.RadioSelect(attrs={'class': 'radio'}),
        'partner_status_of_canada': forms.RadioSelect(attrs={'class': 'radio'}),
        'partner_track': forms.RadioSelect(attrs={'class': 'radio'}),
        'sibling_in_canada': forms.RadioSelect(attrs={'class': 'radio'}),
        'off_lang_en': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{1,40}'}),
        'off_lang_fr': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{1,40}'}),
        'work_exp_canada': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,120}'}),
        'partner_work_exp': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,120}'}),
        'partner_work_exp': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,120}'}),
        'partner_lang': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,40}'}),
        # 'work_exp_home': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,120}'}),
        'memo': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,80}'}),
        # 'marital_status': forms.Select(attrs={'disabled':'disabled'}),
        }

class EducationRu(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'

        labels = {
        'travel_doc_name': 'ФИО* ',
        'email': 'Email* ',
        'contact_number': 'Контактный номер* ',
        'citizenship': 'Гражданство* ',
        'country': 'Страна проживания* ',
        'dob': 'Дата рождения* ',
        'marital_status': 'Семейное положение* ',
        'edu_level': 'Какой ваш самый высокий уровень образования? *',
        'off_lang_en_level': 'Укажите уровень владения Английским* ',
        'off_lang_fr_level': 'Укажите уровень владения Французским* ',
        'en_fr_cert': 'Есть ли у вас сертификаты тестирований английского или французского (IELTS, TOEFL, DAFL, CELPIP, etc)?',
        'int_program': 'Интересующая программа*',
        'plan_date': 'Планируемая дата начала программы* ',
        'pref_province': 'Предполагаемая провинция обучения',
        'plan_budget': 'Планируемый бюджет* ',
        'visa_rejected': 'Наличие предыдущих отказов в визе в Канаду?',
        'memo': 'Дополнительная информация',
        }
        widgets = {
        'travel_doc_name': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '[A-z]{2,20} [A-z]{2,20} [A-z]{2,20}'}),
        'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'pattern': '\w{1,}[-]{0,10}\w{0,}@\w{1,}[-]{0,3}\w{0,}\.\w{1,}'}),
        'citizenship': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,4}'}),
        'contact_number': forms.TextInput(attrs={'placeholder': '+7XXXXXXXXXX or +1XXXXXXXXXX etc.', 'pattern': '\+\d{10,19}'}),
        'country': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,45}'}),
        'dob': forms.DateInput(attrs={'placeholder': 'dd.mm.yyyy', 'pattern': '(([0-2]{1}[0-9]{1})|([3][0-1]))\.((0{1}[0-9]{1})|(1{1}[0-2]{1}))\.((19[3-9][0-9])|(20[0-1][1-8]))'}),
        'school_progr_name':forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{5,80}'}),
        'en_fr_cert': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,120}'}),
        'plan_date': forms.DateInput(attrs={'placeholder': 'dd.mm.yyyy', 'pattern': '(([0-2]{1}[0-9]{1})|([3][0-1]))\.((0{1}[0-9]{1})|(1{1}[0-2]{1}))\.((20[1][8-9])|(20[2][1-9]))'}),
        'pref_province': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,40}'}),
        'plan_budget': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '\d{1,10}'}),
        'visa_rejected': forms.RadioSelect(attrs={'class': 'radio'}),
        'memo': forms.Textarea(attrs={'placeholder': ' ', 'pattern': '.{1,80}'}),
        }
