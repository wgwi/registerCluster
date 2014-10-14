#-*- coding: gb2312 -*-
from django.shortcuts import render

# Create your views here.
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Column, Fieldset, Reset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.views.generic import CreateView, ListView, TemplateView
from django_tables2 import tables, SingleTableView
from simpleSite.models import StudentsUser, EmployeeUser, QA
from django.utils.translation import ugettext_lazy as _
from braces import views as braces


class StudentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_method = 'post'

    helper.layout = Layout(
        HTML(u"<p class=\"text-primary\">请如实填写以下注册信息:</p>"),
        Row(Div('realName', css_class="col-md-4")),
        Row(
            Div('loginName', css_class="col-md-4"),
            Div('teacher', css_class="col-md-4 col-md-offset-1")
        ),
        Row(
            Div('email', css_class="col-md-4"),
            Div('phone', css_class="col-md-4 col-md-offset-1")
        ),
        Row(
            Div(Field('organization', css_class="select-primary select-block mbl"), css_class="col-md-4"),
            Div(Field('position', css_class="select-primary select-block mbl"), css_class="col-md-4 col-md-offset-1"),
        ),
        'story',
        #FormActions for bootstrap only
        FormActions(
            Submit('save_changes', _(u'提交'), css_class="btn-primary"),
            Reset('reset', _(u'重置')),
        )

    )

    class Meta:
        model = StudentsUser


class TeacherForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_method = 'post'

    helper.layout = Layout(
        HTML(u"<p class=\"text-primary\">请如实填写以下注册信息:</p>"),
        Row(Div('realName', css_class="col-md-4")),
        Row(
            Div('loginName', css_class="col-md-4"),
            Div('projectAccount', css_class="col-md-6 col-md-offset-1")
        ),
        Row(
            Div('email', css_class="col-md-4"),
            Div('phone', css_class="col-md-4 col-md-offset-1")
        ),
        Row(
            Div(Field('organization', css_class="select-primary select-block mbl"), css_class="col-md-4"),
        ),
        'story',
        #FormActions for bootstrap only
        FormActions(
            Submit('save_changes', _(u'提交'), css_class="btn-primary"),
            Reset('reset', _(u'重置')),
        )

    )

    class Meta:
        model = EmployeeUser


class EmployeeRegisterView(braces.SuccessURLRedirectListMixin, CreateView):
    template_name = 'normal/employee.html'
    form_class = TeacherForm

    success_list_url = 'home'


class StudentRegisterView(braces.SuccessURLRedirectListMixin, CreateView):
    template_name = 'normal/student.html'
    form_class = StudentForm

    success_list_url = 'home'


class DocsView(ListView):
    template_name = 'normal/faq.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return QA.objects.all()


class StudentsTable(tables.Table):
    selection = tables.columns.CheckBoxColumn(accessor="id", orderable=False)

    class Meta:
        model = StudentsUser
        attrs = {"class": "paleblue"}
        exclude = ('id',)
        sequence = ('selection', 'realName', 'loginName', 'email', 'phone', 'organization', 'position', 'teacher', 'story')


class EmployeeTable(tables.Table):
    selection = tables.columns.CheckBoxColumn(accessor="id", orderable=False)
    pid = tables.columns.CheckBoxColumn(accessor="projectAccount", verbose_name=u"项目帐户")

    class Meta:
        model = EmployeeUser
        attrs = {"class": "paleblue"}
        exclude = ('id', 'projectAccount')
        sequence = ('selection', 'realName', 'loginName', 'email', 'phone', 'organization', 'pid', 'story')



class StudentsView(SingleTableView):
    template_name = 'admin/studentslist.html'
    model = StudentsUser
    table_class = StudentsTable


class EmployeeView(SingleTableView):
    template_name = 'admin/employeeslist.html'
    model = EmployeeUser
    table_class = EmployeeTable






