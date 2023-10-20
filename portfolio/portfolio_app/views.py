from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import ProjectForm, PortfolioForm 
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio

class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.object.project_set.all()
        return context

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

def create_project(request, portfolio_id):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Set the portfolio_id from the URL parameter
            form.instance.portfolio_id = portfolio_id
            form.save()
            return redirect('project-list')  # Redirect to the project list page
    else:
        form = ProjectForm()
    return render(request, 'portfolio_app/project_form.html', {'form': form})

def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')  # Redirect to the project list page
    else:
        form = ProjectForm(instance=project)
    return render(request, 'portfolio_app/project_form.html', {'form': form})

def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project-list')  # Redirect to the project list page
    return render(request, 'portfolio_app/project_confirm_delete.html', {'object': project})

def updatePortfolio(request, pk):
    try:
        portfolio = Portfolio.objects.get(pk=pk)
    except Portfolio.DoesNotExist:
        portfolio = Portfolio()  # Create a new portfolio if it doesn't exist

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', pk=portfolio.id)  # Redirect to the portfolio detail page
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, 'portfolio_app/portfolio_form.html', {'form': form, 'portfolio': portfolio})