from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

"""
# Model to represent the relationship between projects and portfolios.
# Each instance of this model will have a reference to a Portfolio and a Project,
# creating a many-to-many relationship between portfolios and projects. 
class ProjectsInPortfolio(models.Model):

    # Deleting a portfolio will delete associated projects
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    # Deleting a project will not affect the portfolio
    # Just the entry will be removed from this table
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        # Ensures that each project is associated with only one portfolio
        unique_together = ('portfolio', 'project')
"""


class Student(models.Model):
    MAJOR = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )
    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices=MAJOR, blank=False)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
