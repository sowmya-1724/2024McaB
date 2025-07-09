from django.forms import fields  
  
from django import forms  
from .models import EmployeeModel 
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = EmployeeModel  # To specify the model to be used to create form
        fields = '__all__'  # It includes all the fields of model