from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'whatwilllearn', 'whatlearn', 'pros', 'future']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название ОП'
            }),
            "whatwilllearn": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Что буду изучать'
            }),
            "whatlearn": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Чему научусь'
            }),
            "pros": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Преимущества программы'
            }),
            "future": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Перспективы после'
            }),
        }


