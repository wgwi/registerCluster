from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from simpleSite.views import StudentRegisterView, EmployeeRegisterView, DocsView, StudentsView, EmployeeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'registerCluster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^success/', TemplateView.as_view(template_name='normal/success.html'), name="success"),
    url(r'^faq/', DocsView.as_view(), name="faq"),
    url(r'^docs/', TemplateView.as_view(template_name='normal/doc.html'), name="docs"),
    url(r'^student/', StudentRegisterView.as_view(), name="student"),
    url(r'^employee/', EmployeeRegisterView.as_view(), name="employee"),
    url(r'^reg_students/', StudentsView.as_view(), name="reg_students"),
    url(r'^reg_employees/', EmployeeView.as_view(), name="reg_employees"),
    url(r'^login/', 'django.contrib.auth.views.login', {'authentication_form': AuthenticationForm, 'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),

)
