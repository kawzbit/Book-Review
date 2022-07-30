from django.forms import ModelForm, Textarea 
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})
       
        self.fields['top_rating'].widget.attrs.update({'class': 'form-check-input'})
    class Meta:
        model = Review        
        fields = ['text','top_rating']            
        labels = {'top_rating': ('Top Rating') }  
        widgets = {'text': Textarea(attrs={'rows': 4}),} 

