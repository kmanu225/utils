from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class PDFUploadForm(forms.Form):
    pdfs = forms.FileField(widget=MultiFileInput(attrs={"multiple": True}))
