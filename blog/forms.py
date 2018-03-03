from django import forms

from .models import Post

class PostForm(forms.ModelForm):
  #PostForm is the name of our form
  # Tell Django that this form is a ModelForm – forms.ModelForm is responsible for that

    class Meta:
      #class Meta, where we tell Django which model should be used to create this form (model = Post)
        model = Post
        fields = ('title', 'description', 'text',)
        #only title & text fields are exposed
        #author is automatically assigned (logged in user)
        #created_date is set when post is created