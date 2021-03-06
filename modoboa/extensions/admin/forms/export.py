from django import forms
from django.utils.translation import ugettext_lazy


class ExportDataForm(forms.Form):
    filename = forms.CharField(
        label=ugettext_lazy("File name"), max_length=100, required=False
    )
    sepchar = forms.CharField(
        label=ugettext_lazy("Separator"), max_length=1, required=False
    )

    def __init__(self, *args, **kwargs):
        super(ExportDataForm, self).__init__(*args, **kwargs)
        self.fields["sepchar"].widget.attrs = {"class": "span1"}

    def clean_sepchar(self):
        if self.cleaned_data["sepchar"] == "":
            return ";"
        return str(self.cleaned_data["sepchar"])

    def clean_filename(self):
        if self.cleaned_data["filename"] == "":
            return self.fields["filename"].initial
        return str(self.cleaned_data["filename"])


class ExportDomainsForm(ExportDataForm):
    def __init__(self, *args, **kwargs):
        super(ExportDomainsForm, self).__init__(*args, **kwargs)
        self.fields["filename"].initial = "modoboa-domains.csv"


class ExportIdentitiesForm(ExportDataForm):
    def __init__(self, *args, **kwargs):
        super(ExportIdentitiesForm, self).__init__(*args, **kwargs)
        self.fields["filename"].initial = "modoboa-identities.csv"
