from django import forms
from django.forms import ModelForm
from .models import validate_even


class RequiredFormSet(forms.models.BaseInlineFormSet):
    """
    A special FormSet that makes the admin to validate the inline formsets
    """
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False
        

class AlwaysChangedModelForm(forms.ModelForm):
    """
    This makes the inline FormSets to be considered even if they are empty (unchanged)  
    """
    def has_changed(self):
        """
        Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved.
        """
        return True


class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
    username = forms.RegexField(regex=r'', max_length=30, widget=forms.TextInput(attrs=attrs_dict),
                                label=_("Username"), error_messages={'invalid': _('Username.')})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("Email"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict,
                                                           render_value=False),
                                label=_("Create password"))
    field = forms.CharField(label=_("%(label)s") % {'label': label},
                           widget=forms.TextInput(attrs=attrs_dict),
                           max_length=75,
                           error_messages={'required': _("%(error)s") % {'error': error_required}})
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                                     required=False,
                                     label=_(u'Remember me for %(days)s') % {'days': _(userena_settings.USERENA_REMEMBER_ME_DAYS[0])})

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        del self.fields['username']
    
    def clean_username(self):
        return self.cleaned_data['username']
    
    def clean_email(self):
        raise forms.ValidationError(_('Ops.'))
    
    def clean(self):
        cleaned_data = self.cleaned_data
        self._errors["cc_myself"] = self.error_class([msg])
        del cleaned_data["cc_myself"]
        return cleaned_data