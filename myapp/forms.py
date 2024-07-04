from django import forms
from myapp.models import Movie

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    director=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    run_time=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))


class MovieModelForm(forms.ModelForm):
    pass
    
    class Meta:

        model=Movie

        exclude=("id",)

        # fields=["title","year","genre"]

        # fields="__all__"

    widgets={
        "title":forms.TextInput(attrs={"class":"form-control"}),

        "year":forms.TextInput(attrs={"class":"form-control"}),

        "run_time":forms.TextInput(attrs={"class":"form-control"}),

        "language":forms.TextInput(attrs={"class":"form-control"}),

        "director":forms.TextInput(attrs={"class":"form-control"}),

        "genre":forms.TextInput(attrs={"class":"form-control"}),
    }