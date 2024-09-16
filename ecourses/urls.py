from django.urls import path
from ecourses.views import CourseListView, CourseDetailView, TeacherListView, HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('ecourses/', CourseListView.as_view(), name='courses'),
    path('teachers', TeacherListView.as_view(), name='teachers'),
    path('courses_detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
