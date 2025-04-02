from django.contrib import admin
from .models import IntroPage, Milestone
from .models import TeamMember


from .models import TeamMember

# Register your models here.
from .models import AboutPage

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    
    

@admin.register(IntroPage)
class IntroPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')
    
    

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    
    
