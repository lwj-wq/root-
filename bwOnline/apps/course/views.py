from django.shortcuts import render
from django.views.generic import View
from .models import Course
from pure_pagination import Paginator,PageNotAnInteger

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        # 热门课程推荐
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        # 排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses,2 , request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            "all_courses":courses,
            'sort': sort,
            'hot_courses':hot_courses,

        })

class CourseDetailView(View):
    '''课程详情'''
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 课程的点击数加1
        course.click_nums += 1
        course.save()
        return  render(request, "course-detail.html", {
            'course':course,
        })