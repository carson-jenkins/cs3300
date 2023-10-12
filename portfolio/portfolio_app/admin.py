from django.contrib import admin
from .models import Student, Portfolio, Project
#ProjectsInPortfolio

# Define a custom admin class for Portfolio
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_email', 'is_active')
    search_fields = ('title', 'contact_email')

# Register your models with the custom admin classes
admin.site.register(Student)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Project)
# admin.site.register(ProjectsInPortfolio)