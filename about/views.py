from django.shortcuts import render,get_object_or_404

from .models import AboutPage
from .models import TeamMember

from .models import IntroPage, Milestone


# Create your views here.


def about(request):
    page = AboutPage.objects.first()
    page = IntroPage.objects.first()
    # جلب جميع الإحصائيات
    milestones = Milestone.objects.all()
    team_members = TeamMember.objects.all()


    context = {'page': page,'milestones': milestones,'team_members': team_members}
    
    return render(request, 'about/about.html',context)

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(TeamMember, id=doctor_id)
    return render(request, 'about/doctor_detail.html', {'doctor': doctor})
