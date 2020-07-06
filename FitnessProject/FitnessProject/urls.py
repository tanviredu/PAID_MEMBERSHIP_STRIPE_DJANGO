from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from plans import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('plans/<int:pk>',views.plan,name='plan'),
    path('auth/',include('django.contrib.auth.urls')),
    path('auth/signup',views.SignUp.as_view(),name='signup'),
    path('join/',views.join,name="join"),
    path('checkout',views.checkout,name='checkout'),
    path('auth/settings',views.settings,name='settings'),

]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
