from datetime import datetime

from django.utils.html import format_html
from django.contrib import admin, messages


from .models import Job, Resume
from ..interview.models import Candidate


class JobAdmin(admin.ModelAdmin):
    """
    职位管理模块
    """
    exclude = ('creator','created_date','modified_date')
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
        super().save_model(request, obj, form, change)


def enter_interview_process(modeladmin, request, queryset):
    """ 进入面试流程 """
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = candidate.username + "," + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人: %s 已成功进入面试流程' % (candidate_names) )



class ResumeAdmin(admin.ModelAdmin):
    """
    简历管理
    """

    list_display = ('username', 'applicant', 'city', 'apply_position',
                    'bachelor_school', 'master_school', 'major','created_date',
    )

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender", ),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience","project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(Resume,ResumeAdmin)
