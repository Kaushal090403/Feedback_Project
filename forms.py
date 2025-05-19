from django import forms
class FbForm(forms.Form):
    name=forms.CharField()
    Class=forms.IntegerField()
    feedback=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"col":22,"style":"resize:none"}))
    