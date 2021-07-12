from django.urls import path
from  . import views

urlpatterns = [
    path('',views.fun,name='fun'),
    path('about.html/',views.about,name='about'),
    path('blog.html/',views.blog,name='blog'),
    path('blog-single.html/',views.blogsingle,name='blogsingle'),
    path('contact.html/',views.contact,name='contact'),
    path('doctors.html/',views.doctors,name='doctors'),
    path('blog.html/blog-single.html',views.detail,name='detail'),
    path('blog.html/dermatology.html', views.dermatology, name='dermatology'),
    path('blog.html/gynaecology.html', views.gynaecology, name='gynaecology'),
    path('blog.html/cardiology.html', views.cardiology, name='cardiology'),
    path('blog.html/nephrology.html', views.nephrology, name='nephrology'),
    path('blog.html/orthology.html', views.orthology, name='orthology'),

]