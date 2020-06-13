from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('diary/', views.diary, name="diary"),
    path('diary/new_diary/', views.new_diary, name="new diary"),
    re_path(r'^diary/diary_detail_page/(?P<pk>\d+)/$', views.detail, name="diary_item"),
]