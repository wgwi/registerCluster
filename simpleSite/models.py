#-*- coding: gb2312 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

POSITION_CHOICES = (
    ('T', u"�̹�"),
    ('S', u"ѧ��"),
)


class Organization(models.Model):
    callName = models.CharField(_(u"������λ"), max_length=40, unique=True)


class RegisterUser(models.Model):
    realName = models.CharField(_(u"��ʵ����"), max_length=10, null=False, blank=False)
    loginName = models.CharField(_(u"�Ż��ʻ�"), max_length=20, unique=True)
    projectAccount = models.BooleanField(_(u"��Ŀ�û�,�������ʹ��ͬһ�ʻ���½"), max_length=1)
    email = models.EmailField(_(u"�ʼ���ַ"), max_length=40, null=False, blank=False)
    phone = models.CharField(_(u"�ƶ��绰"), max_length=13, null=False, blank=False)
    organization = models.ForeignKey(Organization, to_field='id')
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=u"�̹�")
    story = models.TextField(_(u"��Ŀ����"), max_length=50, null=False, blank=False)

