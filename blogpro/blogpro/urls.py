"""blogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.postview),
    path('tag/<slug:tagslug>',views.postview,name='postlist by tagname'),
    #path('(?p<year>\d{4})/(?p<month>\d{2})/(?p<day>\d{2})/*(?p<post>\[-\w]+)/',views.postdetails,name='postdetails'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.postdetails,name='postdetails'),
    path('<int:id>/share', views.Emailshareview),
]
