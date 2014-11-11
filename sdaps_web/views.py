from django.conf.urls import url, patterns
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout),
#    url(r'^accounts/profile/$', auth_views.profile),
    url(r'^accounts/password_change/$', auth_views.password_change),
    url(r'^accounts/password_change_done/$', auth_views.password_change_done),

# TODO: Password reset
# password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)
