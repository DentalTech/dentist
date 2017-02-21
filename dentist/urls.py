"""dentist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dentist_app import views
from django.conf.urls import url, include
from accounts import views as accounts_views
from services import views as service_views
from appointments import views as appointment_views
from django.conf import settings
from django.views.static import serve
from blog import views as blog_views
from threads import views as forum_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index'),
    url(r'^ourteam/$', views.get_ourteam, name='ourteam'),

    #Authentication URLs
    url(r'^membership/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),

    #Blog URLs
    url(r'^blog/$', blog_views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),


    #Media URLs
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    #Services URLs
    url(r'^services/$', service_views.all_services, name='services'),

    #Appointments URLs
    url(r'^appointments/$', appointment_views.all_appointments, name='appointments'),
    url(r'^create_appointment/$', appointment_views.create_appointment, name='create_appointment'),

    # Forum URLs
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),


]
