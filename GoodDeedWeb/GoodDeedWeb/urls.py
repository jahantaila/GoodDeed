"""GoodDeedWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('',views.index, name = 'index'),
    path('home/',views.index, name = 'index'),
    path('register/',views.register, name = 'register'),
    path('admin/', admin.site.urls),
    path('login/', views.loginpage, name = 'loginpage' ),
    path('logout/', views.logoutuser, name = 'logout' ),
    path('dashboard/',views.dashboard, name = 'dashboard' ),
    path('donate/', views.donate, name = 'donate' ),
    path('availablesupplies/', views.availablesupplies, name = 'availablesupplies' ),
    path('thankyou/', views.thankyou, name = 'thankyou' ),
    path('donations/<pk>/', views.DonationDetail.as_view(), name='donation-detail'),
    path('donations/<str:id>/delete/', views.deleteDonation, name='delete_donations'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name = 'contact' ),
    path('request/', views.request, name = 'request' ),
    path('viewrequests/', views.viewrequests, name = 'viewrequests' ),
    path('requests/<pk>/', views.RequestDetail.as_view(), name='request-detail'),
    path('requests/<str:id>/delete/', views.deleteRequest, name='delete_requests'),
    path('leaderboard/',views.leaderboard, name = 'leaderboard' ),


]


#image stuff bellow
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)