from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.conf.urls import url, include

from django.contrib import admin

from demo.views import (login_view,register_view,logout_view,MyView,UserUpdate,UserDelete)

from demo import views as core_views

from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index, name='index'),
    url(r'^signup/$', register_view, name='signup'),
    url(r'^login/$', login_view, name='login'),
    url(r'^pro/$', MyView, name='pro'),
    url(r'^logout/$', logout_view, name='logout'),
  	path('edit/<int:pk>', UserUpdate.as_view(), name='user_edit'),
  	path('delete/<int:pk>', UserDelete.as_view(), name='user_delete'),
]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
