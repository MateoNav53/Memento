from django.shortcuts import render, redirect
from .models import Diary
from .forms import NewDiaryModelForm

# Create your views here.
def index(request):
    return render(request, 'diary_app/home.html')

def diary(request):
    diaries = Diary.objects.all()
    context = {
        'diaries': diaries
    }
    return render(request, 'diary_app/diary.html', context)

def new_diary(request):
    form = NewDiaryModelForm(request.POST or None, request.FILES or None)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('/diary')  
    return render(request, 'diary_app/new_diary.html', {'form': form})
    
    

def detail(request, pk):
    diary_detail = Diary.objects.get(pk=pk)
    template_name = 'diary_app/diary_detail_page.html'
    data = {
        'title': diary_detail.title, 
        'date': diary_detail.publish_date,
        'content': diary_detail.content,
        'image': diary_detail.image,
    }
    return render(request, template_name, data)

