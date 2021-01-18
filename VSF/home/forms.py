from django.forms import ModelForm
from .models import contact_details

class contact_form(ModelForm):
    class Meta:
        model=contact_details
        fields=['person_name','person_email_id','subject','Message']