from django import forms

from . models import Comment, Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name':''}

#REPEAT SLIDE 2 ON PART V FOR COMMENTS

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name':''}
