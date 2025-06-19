from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

def forma_home(request):
    forma = Articles.objects.order_by('title')
    return render(request, 'forma/forma_home.html', {'forma': forma})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()  # исправлено
        else:
            error = 'Ошибка при заполнении формы'  # исправлено

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error  # добавлена запятая
    }

    return render(request, 'forma/create.html', data)
