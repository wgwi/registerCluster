from django.contrib import admin

# Register your models here.
from models import StudentsUser, Organization, EmployeeUser, QA


class QAAdmin(admin.ModelAdmin):
    list_display = ('qu', 'an')


class StudentsUserAdmin(admin.ModelAdmin):
    list_display = ('realName', 'loginName', 'email', 'phone', 'organization', 'position', 'teacher', 'status')


class EmployeeUserAdmin(admin.ModelAdmin):
    list_display = ('realName', 'loginName', 'email', 'phone', 'organization', 'projectAccount', 'status')

admin.site.register(StudentsUser, StudentsUserAdmin)
admin.site.register(Organization)
admin.site.register(EmployeeUser, EmployeeUserAdmin)
admin.site.register(QA, QAAdmin)
