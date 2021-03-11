from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings.base import AUTH_USER_MODEL


# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

# 职位类型
JobTypes = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类"),
    (4,"市场营销类")
]

# 招聘城市
Cities = [
    (0,"北京"),
    (1,"上海"),
    (2,"深圳"),
    (3,"杭州"),
    (4,"广州")
]


class Job(models.Model):
    # Translators: 职位实体的翻译
    job_name = models.CharField(max_length=250, blank=False, verbose_name=_("职位名称"))
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name=_("职位类别"))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_("工作地点"))
    job_description = models.TextField(max_length=1024, verbose_name=_("职位描述"))
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name=_("职位要求"))
    creator = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("创建人"), null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_("创建日期"), auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name=_("修改日期"), auto_now=True)

    class Meta:
        verbose_name = _('职位')
        verbose_name_plural = _('职位列表')

    def __str__(self):
        return self.job_name
    

