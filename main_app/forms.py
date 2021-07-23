from django.forms import ModelForm
from .models import Stop


class StopForm(ModelForm):
    class Meta:
        model = Stop
        fields = ['stop_name', 'stop_adress',
                  'stop_city', 'stop_state', 'stop_date']
