from django import forms
from .models import ClientAssesment, Education



class ClientAssesmentEn(forms.ModelForm):

    class Meta:
        model = ClientAssesment
        fields = '__all__'

        labels = {
        'travel_doc_name': 'Official Name on your travel document (required)',
        'email': 'Your Email (required)',
        'address': 'Address',
        'contact_number': 'Your Contact Number (required)',
        'marital_status': 'What is your marital status? (required)',
        'country': 'What is your country? (required)',
        'dob': 'What is your D.O.B (Date of Birth)?',
        'immigration_status': 'What is your current immigration status? (required)',
        'edu_level': 'What is your level of education? (required)',
        'school_progr_name': 'Please provide School name and Program name.',
        'off_lang_en_level': 'What is your level of English? (required)',
        'off_lang_fr_level': 'What is your level of French? (required)',
        'work_exp_canada': 'Work Experience (Full-Time) in Canada (NOC 0, A or B - Please provide Job title and Duration.)',
        # 'work_exp_home': 'Work Experience (Full-Time) in your country in the past 10 years (NOC 0, A or B - Please provide Job title and Duration.)',
        'partner_edu': 'What is the highest level of education for which your spouse or common-law partner\'s has:',
        'partner_work_exp': 'Spouse\'s Work Experience (Full-Time) in Canada (NOC 0, A or B)',
        'partner_lang': 'Official Languages (Spouse): English or French (Test Name: Speaking / Listening / Reading / Writing)',
        'canadian_dipl': 'Have you earned a Canadian degree, diploma or certificate?',
        'canadian_cert':'Do you have a certificate of qualification from a Canadian province or territory? (Skilled trade occupations)',
        'valid_job': 'Do you have a valid job offer supported by a Labour Market Impact Assessment (if needed)?',
        'nomin_cert': 'Do you have a nomination certificate from a province or territory?',
        'partner_status_of_canada': 'Is your spouse or common-law partner a citizen or permanent resident of Canada?',
        'partner_track': 'Will your spouse or common-law partner come with you to Canada?',
        'sibling_in_canada': 'Do you have a sibling in Canada who is a Canadian citizen or permanent resident of at least 18 years of age?',
        'memo': 'Memo',
        }
        widgets = {
        'travel_doc_name': forms.TextInput(attrs={'placeholder': 'John Smith', 'pattern': '[A-z]{2,20} [A-z]{2,20}[ ]{0,1}[A-z]{0,20}'}),
        'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'pattern': '[A-z.]{1,}[-.]{0,10}[A-z.]{0,}@\w{1,}[-.]{0,3}\w{0,}\.\w{1,}'}),
        'address': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,80}'}),
        'contact_number': forms.TextInput(attrs={'placeholder': '+1XXXXXXXXXX', 'pattern': '\+\d{10,19}'}),
        'country': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,45}'}),
        'dob': forms.DateInput(attrs={'placeholder': 'dd.mm.yyyy', 'pattern': '(([0-2]{1}[0-9]{1})|([3][0-1]))\.((0{1}[0-9]{1})|(1{1}[0-2]{1}))\.((19[3-9][0-9])|(20[0-1][1-8]))'}),
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

class EducationEn(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'

        labels = {
        'travel_doc_name': 'Official Name on your travel document (required)',
        'email': 'Your Email (required)',
        'contact_number': 'Your Contact Number (required)',
        'citizenship': 'What is your citizenship? (required)',
        'country': 'What is your country? (required)',
        'dob': 'What is your D.O.B (Date of Birth)?',
        'marital_status': 'What is your marital status? (required)',
        'edu_level': 'What is your level of education? (required)',
        'off_lang_en_level': 'What is your level of English? (required)',
        'off_lang_fr_level': 'What is your level of French? (required)',
        'en_fr_cert': 'Have you ever taken English or French Proficiency tests (IELTS, TOEFL, DAFL, CELPIP, etc)? (required)',
        'int_program': 'What is the program that you are interested in?',
        'plan_date': 'When do you plan to start your program? (required)',
        'pref_province': 'Do you have a preferred province?',
        'plan_budget': 'What is an estimated budget for your studies?(required)',
        'visa_rejected': 'Have you ever been rejected a visa to come to Canada?',
        'memo': 'Memo',
        }
        widgets = {
        'travel_doc_name': forms.TextInput(attrs={'placeholder': 'John Smith', 'pattern': '[A-z]{2,20} [A-z]{2,20}[ ]{0,1}[A-z]{0,20}'}),
        'email': forms.TextInput(attrs={'placeholder': 'example@mail.com', 'pattern': '[A-z.]{1,}[-.]{0,10}[A-z.]{0,}@\w{1,}[-.]{0,3}\w{0,}\.\w{1,}'}),
        'citizenship': forms.TextInput(attrs={'placeholder': ' ', 'pattern': '.{2,4}'}),
        'contact_number': forms.TextInput(attrs={'placeholder': '+1XXXXXXXXXX', 'pattern': '\+\d{10,19}'}),
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
