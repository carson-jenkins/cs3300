from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolios/', views.PortfolioListView.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('create-project/<int:portfolio_id>/', views.create_project, name='create-project'),
    path('update-project/<int:pk>/', views.update_project, name='update-project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete-project'),
    path('update-portfolio/<int:pk>', views.updatePortfolio, name='update-portfolio'),
]