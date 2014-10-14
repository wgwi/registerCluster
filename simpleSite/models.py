#-*- coding: gb2312 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

STUDENTS_CHOICES = (
    ('M', u"硕士"),
    ('D', u"博士"),
)


class Organization(models.Model):
    callName = models.CharField(_(u"所属单位"), max_length=40, unique=True)

    def __unicode__(self):
        return self.callName

    class Meta:
        verbose_name = _(u'组织机构')
        verbose_name_plural = _(u'组织机构')


class RegisterUser(models.Model):
    realName = models.CharField(_(u"真实姓名"), max_length=10, null=False, blank=False)
    loginName = models.CharField(_(u"门户帐户"), max_length=20, unique=True)
    email = models.EmailField(_(u"邮件地址"), max_length=40, null=False, blank=False)
    phone = models.CharField(_(u"移动电话"), max_length=13, null=False, blank=False)
    organization = models.ForeignKey(Organization, verbose_name=_(u"单位"), to_field='id')
    story = models.TextField(_(u"项目描述"), max_length=800, null=False, blank=False)
    #pre_password = models.CharField(_(u"预先设定的密码"), max_length=8)
    status = models.BooleanField(_(u"已处理"), default=False)

    class Meta:
        abstract = True


class StudentsUser(RegisterUser):
    position = models.CharField(_(u"身份"), max_length=1, choices=STUDENTS_CHOICES, default=u"博士")
    teacher = models.CharField(_(u"指导老师"), max_length=10, null=False, blank=False)

    class Meta:
        verbose_name = _(u'注册学生')
        verbose_name_plural = _(u'注册学生')

    def __unicode__(self):
        return self.organization.callName + "," + self.realName

class EmployeeUser(RegisterUser):
    projectAccount = models.BooleanField(_(u"项目用户,允许多人使用同一帐户登陆"), max_length=1)

    class Meta:
        verbose_name = _(u'注册教工')
        verbose_name_plural = _(u'注册教工')

    def __unicode__(self):
        return self.organization.callName + "," + self.realName

class QA(models.Model):
    qu = models.TextField(_(u"问题"), max_length=300, null=False, blank=False)
    an = models.TextField(_(u"回答"), max_length=1000, null=False, blank=False)

    class Meta:
        verbose_name = _(u'问与答')
        verbose_name_plural = _(u'问与答')

    def __unicode__(self):
        return self.qu