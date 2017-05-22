from django.conf.urls import url
from .views import UserRegister
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup/', UserRegister.as_view(), name = "register"),
    url(r'^login/', login, {'template_name':'users/login.html'}, name = 'login'),
    url(r'^logout/', login_required(logout), {'next_page': '/'}, name='logout'),
    url(r'^reset/password_reset', password_reset,{'template_name':'users/registration/password_reset_form.html','email_template_name': 'users/registration/password_reset_email.html'},name='password_reset'),
    url(r'^password_reset_done', password_reset_done,{'template_name': 'users/registration/password_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name': 'users/registration/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'users/registration/password_reset_complete.html'},name='password_reset_complete'),
]
