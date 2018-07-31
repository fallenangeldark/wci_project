from django import forms
from .models import ClientAssesment


class ClientAssesmentEn(forms.ModelForm):
    # CHOICE_YES_NO = (
    # (False, 'No'),
    # (True, 'Yes'),
    # )
    # canadian_dipl = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
    #                choices=((0, 'False'), (1, 'True')),
    #                widget=forms.RadioSelect()
    #             )
    # canadian_cert = forms.TypedChoiceField(coerce=lambda x: bool(int(x)),
    #                choices=((0, 'False'), (1, 'True')),
    #                widget=forms.RadioSelect()
    #             )
    # canadian_dipl = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Have you earned a Canadian degree, diploma or certificate?')
    # canadian_cert = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Do you have a certificate of qualification from a Canadian province or territory? (Skilled trade occupations)')
    # valid_job = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Do you have a valid job offer supported by a Labour Market Impact Assessment (if needed)?')
    # nomin_cert = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Do you have a nomination certificate from a province or territory?')
    # partner_status_of_canada = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'If you are married, is your spouse or common-law partner a citizen or permanent resident of Canada?')
    # partner_track = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Will your spouse or common-law partner come with you to Canada?')
    # sibling_in_canada = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=CHOICE_YES_NO, label = 'Do you have a sibling in Canada who is a Canadian citizen or permanent resident of at least 18 years of age ?')


    class Meta:
        model = ClientAssesment
        fields = '__all__'

        labels = {
        'travel_doc_name': 'Official Name on your travel document (required)',
        'email': 'Your Email (required)',
        'address': 'Address',
        'contact_number': 'Your Contact Number (required)',
        'marital_status': 'What is your marital status?',
        'nationality': 'What is your nationality?',
        'dob': ' What is your D.O.B (Date of Birth)?',
        'immigration_status': 'What is your current immigration status?',
        'edu_level': 'What is your level of education?',
        'school_progr_name': ' If yes, please provide School name and Program name.',
        'off_lang_en': 'Official Languages: English (Test Name: Speaking / Listening / Reading / Writing)',
        'off_lang_fr': 'Official Languages: French (Test Name: Speaking / Listening / Reading / Writing)',
        'work_exp_canada': ' Work Experience (Full-Time) in Canada (NOC 0, A or B - Please provide Job title and Duration.)',
        'work_exp_home': 'Work Experience (Full-Time) in your country in the past 10 years (NOC 0, A or B - Please provide Job title and Duration.)',
        'partner_edu': ' What is the highest level of education for which your spouse or common-law partner\'s has:',
        'partner_work_exp': 'Spouse\'s Work Experience (Full-Time) in Canada (NOC 0, A or B)',
        'partner_lang': 'Official Languages (Spouse): English or French (Test Name: Speaking / Listening / Reading / Writing)',
        'memo': 'Memo',
        'canadian_dipl': 'Have you earned a Canadian degree, diploma or certificate?',
        'canadian_cert':'Do you have a certificate of qualification from a Canadian province or territory? (Skilled trade occupations)',
        'valid_job': 'Do you have a valid job offer supported by a Labour Market Impact Assessment (if needed)?',
        'nomin_cert': 'Do you have a nomination certificate from a province or territory?',
        'partner_status_of_canada': 'If you are married, is your spouse or common-law partner a citizen or permanent resident of Canada?',
        'partner_track': 'Will your spouse or common-law partner come with you to Canada?',
        'sibling_in_canada': 'Do you have a sibling in Canada who is a Canadian citizen or permanent resident of at least 18 years of age?',
        }
        widgets = {
        'travel_doc_name': forms.Textarea(),
        'name': forms.TextInput(attrs={'placeholder': 'Alex'}),
        'dob': forms.DateInput(attrs={'placeholder': 'dd.mm.yyyy'}),
        'email': forms.TextInput(attrs={'placeholder': 'example@mail.com'}),
        'contact_number': forms.TextInput(attrs={'placeholder': '+7XXXXXXXXXX or +380XXXXXXXXX etc.'}),
        'canadian_dipl': forms.RadioSelect(attrs={'class': 'radio'}),
        'canadian_cert': forms.RadioSelect(attrs={'class': 'radio'}),
        'valid_job': forms.RadioSelect(attrs={'class': 'radio'}),
        'nomin_cert': forms.RadioSelect(attrs={'class': 'radio'}),
        'partner_status_of_canada': forms.RadioSelect(attrs={'class': 'radio'}),
        'partner_track': forms.RadioSelect(attrs={'class': 'radio'}),
        'sibling_in_canada': forms.RadioSelect(attrs={'class': 'radio'}),
        }
