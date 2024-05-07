from django import forms

class NameForm(forms.Form):
 subject = forms.CharField(label="subject",max_length=100)
 message = forms.CharField(label="message", widget=forms.Textarea)
 sender = forms.EmailField(label="sender")
 cc_myself = forms.BooleanField(label="myself",required=False)