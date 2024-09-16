
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ecourses.models import Course, Category, Blog, Teacher, Video


class HomeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        # Agar siz har bir model uchun alohida queryset olishni istasangiz:
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        blogs = Blog.objects.all()

        # Bularni so'nggi kontekstda foydalanish uchun to'plang
        return {
            'teachers': teachers,
            'courses': courses,
            'blogs': blogs
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # QuerySetlarni kontekstga qo'shish
        context['teachers'] = Teacher.objects.all()
        context['courses'] = Course.objects.all()
        context['blogs'] = Blog.objects.all()

        return context


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/courses_detail.html'
    context_object_name = 'course'


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class VideoDetailView(DetailView):
    model = Video
    template_name = 'courses/courses_detail.html'
    context_object_name = 'videos'


