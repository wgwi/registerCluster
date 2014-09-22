#-*- coding: gb2312 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

POSITION_CHOICES = (
    ('T', u"教工"),
    ('S', u"学生"),
)


class Organization(models.Model):
    callName = models.CharField(_(u"所属单位"), max_length=40, unique=True)


class RegisterUser(models.Model):
    realName = models.CharField(_(u"真实姓名"), max_length=10, null=False, blank=False)
    loginName = models.CharField(_(u"门户帐户"), max_length=20, unique=True)
    projectAccount = models.BooleanField(_(u"项目用户,允许多人使用同一帐户登陆"), max_length=1)
    email = models.EmailField(_(u"邮件地址"), max_length=40, null=False, blank=False)
    phone = models.CharField(_(u"移动电话"), max_length=13, null=False, blank=False)
    organization = models.ForeignKey(Organization, to_field='id')
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=u"教工")
    story = models.TextField(_(u"项目描述"), max_length=50, null=False, blank=False)

