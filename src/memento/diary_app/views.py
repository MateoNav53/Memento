from django.shortcuts import render
from .models import Diary

# Create your views here.
def index(request):
    return render(request, 'diary_app/template.html')

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
            # image=request.POST['image'],
            content=request.POST['content']
        )
        create_new_diary.save()
    return render(request, 'diary_app/new_diary.html')