from django.urls import path

from .views import joblist, detail, ResumeCreateView


app_name = "jobs"

urlpatterns = [
    # 职位列表
    path("list/", joblist, name="list"),
    path("", joblist,name="name"),
    # 职位详情
    path('<int:job_id>/', detail, name='detail'),
    # 提交简历
    path('resume/add/', ResumeCreateView.as_view(), name='resume-add'),
]