#-*- coding: gb2312 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

STUDENTS_CHOICES = (
    ('M', u"˶ʿ"),
    ('D', u"��ʿ"),
)


class Organization(models.Model):
    callName = models.CharField(_(u"������λ"), max_length=40, unique=True)

    def __unicode__(self):
        return self.callName

    class Meta:
        verbose_name = _(u'��֯����')
        verbose_name_plural = _(u'��֯����')


class RegisterUser(models.Model):
    realName = models.CharField(_(u"��ʵ����"), max_length=10, null=False, blank=False)
    loginName = models.CharField(_(u"�Ż��ʻ�"), max_length=20, unique=True)
    email = models.EmailField(_(u"�ʼ���ַ"), max_length=40, null=False, blank=False)
    phone = models.CharField(_(u"�ƶ��绰"), max_length=13, null=False, blank=False)
    organization = models.ForeignKey(Organization, verbose_name=_(u"��λ"), to_field='id')
    story = models.TextField(_(u"��Ŀ����"), max_length=800, null=False, blank=False)
    #pre_password = models.CharField(_(u"Ԥ���趨������"), max_length=8)
    status = models.BooleanField(_(u"�Ѵ���"), default=False)

    class Meta:
        abstract = True


class StudentsUser(RegisterUser):
    position = models.CharField(_(u"���"), max_length=1, choices=STUDENTS_CHOICES, default=u"��ʿ")
    teacher = models.CharField(_(u"ָ����ʦ"), max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = _(u'ע��ѧ��')
        verbose_name_plural = _(u'ע��ѧ��')

    def __unicode__(self):
        return self.organization.callName + "," + self.realName

class EmployeeUser(RegisterUser):
    projectAccount = models.BooleanField(_(u"��Ŀ�û�,�������ʹ��ͬһ�ʻ���½"), max_length=1)

    class Meta:
        verbose_name = _(u'ע��̹�')
        verbose_name_plural = _(u'ע��̹�')

    def __unicode__(self):
        return self.organization.callName + "," + self.realName

class QA(models.Model):
    qu = models.TextField(_(u"����"), max_length=300, null=False, blank=False)
    an = models.TextField(_(u"�ش�"), max_length=1000, null=False, blank=False)

    class Meta:
        verbose_name = _(u'�����')
        verbose_name_plural = _(u'�����')

    def __unicode__(self):
        return self.qu