from django.shortcuts import render, redirect
from .models import Diary

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
    if request.method =="POST":
        create_new_diary = Diary.objects.create(
            title=request.POST['title'],
            image=request.POST['image'],
            content=request.POST['content']
        )
        create_new_diary.save()
        return redirect('/diary')
    return render(request, 'diary_app/new_diary.html')
    
    

def detail(request, pk):
    diary_detail = Diary.objects.get(pk=pk)
    template_name = 'diary_app/diary_detail_page.html'
    data = {
        'title': diary_detail.title, 
        'date': diary_detail.publish_date,
        'content': diary_detail.content
    }
    return render(request, template_name, data)

