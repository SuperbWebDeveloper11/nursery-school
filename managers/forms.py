from django import forms
from .models import Babysitter, Group, Baby, Activity, Sitting


# we'll use this class to display html5 date input
class DateInput(forms.DateInput):
    input_type = 'date'

# we'll use this class to display html5 datetime-local input
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class BabysitterForm(forms.ModelForm):
    class Meta:
        model = Babysitter
        fields = ('name', 'surname', 'date_of_bearth', 'picture')
        widgets = {'date_of_bearth': DateInput()} # display html5 date input


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'taken_by')


class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ('name', 'surname', 'date_of_bearth', 'picture', 'belong_to')
        widgets = {'date_of_bearth': DateInput()} # display html5 date input


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description', 'picture')


class SittingForm(forms.ModelForm):
    class Meta:
        model = Sitting
        fields = ('started_at', 'finished_at', 'activities', 'done_by')
        widgets = {'started_at': DateTimeInput(), 'finished_at': DateTimeInput() } # display html5 datetime-local input
        # works perfect for create sitting but when update the form doesn't display the initial data



