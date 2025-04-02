# services/models.py
from about.models import TeamMember
from django.db import models

from home.models import Service

class SpecialService(Service):
    
    owner = models.ForeignKey(
        TeamMember, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='special_services'
    )
    
    # إضافة حقول جديدة إذا كنت تحتاج إلى توسيع النموذج

    def __str__(self):
        return f"Special Service: {self.name}"  # افترض أن النموذج الأصلي يحتوي على حقل اسمه "name"
    
    
