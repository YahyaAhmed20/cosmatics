# services/models.py
from about.models import TeamMember
from django.db import models
from django.contrib.auth.models import User

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
    
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    appointment_date = models.DateField(null=True, blank=True)  # العميل يحددها بعد الدفع

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"