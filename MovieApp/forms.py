from django import forms;
from MovieApp.models import Movies

#class MoviesForm(forms.ModelForm):
    #no-separate fields are required(taken from model-Movies-class)
 #   class Meta:
  #      model=Movies
   #     fields='__all__'

class DateInput(forms.DateInput):
    input_type = 'date';


class MoviesForm(forms.ModelForm):
    releasedate = forms.DateField(widget=DateInput())
    moviename = forms.CharField()
    actor = forms.CharField()
    actress = forms.CharField()
    rating = forms.FloatField()
    director=forms.CharField()

    class Meta:
        model = Movies
        fields = ('releasedate', 'moviename', 'actor', 'actress', 'rating','director');
