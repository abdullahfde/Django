"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url

from django.contrib import admin

from assginment4 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addstudent/$',views.addastudent),
    url(r'^all-students/$',views.all_students),
    url(r'^addteacher/$',views.addateacher),
    url(r'^all-teachers/$',views.all_teachers),
    url(r'^addcourse/$',views.addacourse),
    url(r'^all-courses/$',views.all_courses),
    url(r'^enroll-students/$',views.enrollstudents),
    url(r'^show-students/(\d+)$',views.show),



]
