from django.urls import path
from . import views

urlpatterns = [
    path('',views.starting_page,name='starting_page'),
    path('post',views.posts,name='posts_page'),
    path('post/<slug:slug>',views.post_details,name='post_detail_page')
    

]
