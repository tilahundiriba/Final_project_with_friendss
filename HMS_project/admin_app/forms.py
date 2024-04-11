# forms.py
from django.contrib.auth.forms import PasswordResetForm

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add custom CSS classes to form fields
        for field_name in ['new_password1', 'new_password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'