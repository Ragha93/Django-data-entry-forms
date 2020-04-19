from django import forms
from walkapp.models import Userprofileinfo,Wts_table
from django.contrib.auth.models import User

class Registerform(forms.ModelForm):
    password = forms.CharField(max_length=20, min_length=5, widget=(forms.PasswordInput()))
    class Meta:
        model = User
        fields = ('email','username','password')
        help_texts = {
            'username': None,
        }


class Inputform(forms.ModelForm):
    class Meta:
        model = Userprofileinfo
        exclude = ('user','date','timenow')

# class Wtsform(forms.ModelForm):
#     asin = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     vendorCode= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     Asinsitestatus= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     asincurrentcategory= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     item_name= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     brand_name= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point1= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point2= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point3= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point4= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point5= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point6= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point7= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     bullet_point8= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     asinsitemsg= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     color_name= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     size_name= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     asin_subject_keywords= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     allocatedto= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     allocationdate= forms.DateField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
#     class Meta:
#         model = Wts_table
#         fields = '__all__'
