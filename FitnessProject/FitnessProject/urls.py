from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from plans import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('plans/<int:pk>',views.plan,name='plan'),
    
    # why this url is added
    # because now you dont need to write any view
    # or anyting for login,logout
    # you just give the template
    # and add the url
    # and this will work through django administration
    # watch the base.html to understand
    # for login it wil automatically want a tempate
    # inside the registration folder
    # so you have to make a registration folder
    # for this
    path('auth/',include('django.contrib.auth.urls')),
    path('accounts/profile/',views.redi,name='redi'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('accounts/login/',views.red_to_login,name='red_to_login'),
    
    path('auth/signup',views.SignUp.as_view(),name='signup'),
    path('join/',views.join,name="join"),
    path('checkout',views.checkout,name='checkout'),
    path('auth/settings',views.settings,name='settings'),
    path('updateaccounts', views.updateaccounts, name='updateaccounts'),

]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
