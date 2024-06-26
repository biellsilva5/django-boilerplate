from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from users.models import Users 


class UserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"), widget=forms.PasswordInput
    )
    
    class Meta:
        model = Users
        fields = ['email']
        
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Users
        fields = '__all__'

# Register your models here.
class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None,{'fields': ('email', 'password')},),
        (_('Personal info'),  {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'groups',
                'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ['email']
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(Users, UserAdmin)