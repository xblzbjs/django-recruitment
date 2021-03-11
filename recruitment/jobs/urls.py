from django.urls import path

from . import views


urlpatterns = [
    # 职位列表
    path("list/", views.joblist, name="list"),
    path("", views.joblist,name="name"),
    # 职位详情
    path('<int:job_id>/', views.detail, name='detail'),
]