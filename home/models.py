# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Slide(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='slider_images/', verbose_name=_("Image"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active?"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")
        
        
class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="التخصص")

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الطبيب")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="doctors", verbose_name="التخصص")

    def __str__(self):
        return f"{self.name} - {self.specialty}"

class Appointment(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="الاسم الكامل")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="التخصص")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="الطبيب")
    appointment_date = models.DateField(verbose_name="تاريخ الموعد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    is_paid = models.BooleanField(default=False, verbose_name="تم الدفع؟")

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date}"

    class Meta:
        verbose_name = "حجز موعد"
        verbose_name_plural = "حجوزات المواعيد"
        
        
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255, verbose_name="العنوان")
    subtitle = models.CharField(max_length=255, verbose_name="العنوان الفرعي")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='why_choose_us/', verbose_name="الصورة")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "لماذا تختارنا"
        verbose_name_plural = "لماذا تختارنا"

class WhyChooseUsItem(models.Model):
    why_choose_us = models.ForeignKey(WhyChooseUs, on_delete=models.CASCADE, related_name="items", verbose_name="لماذا تختارنا")
    icon = models.ImageField(upload_to='icons/', verbose_name="الأيقونة")
    title = models.CharField(max_length=255, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")


    def save(self, *args, **kwargs):
        # Ensure only one record is active at a time
        if self.is_active:
            WhyChooseUs.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "عنصر لماذا تختارنا"
        verbose_name_plural = "عناصر لماذا تختارنا"
        
        
class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الخدمة")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(verbose_name="الوصف", default="")
    icon = models.ImageField(upload_to='service_icons/', verbose_name="الأيقونة")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")

    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        
        
class DiscountOffer(models.Model):
    discount_percentage = models.PositiveIntegerField(verbose_name="نسبة الخصم (%)")
    title = models.CharField(max_length=255, verbose_name="العنوان")
    description = models.TextField(verbose_name="الوصف")
    image = models.ImageField(upload_to='discount_offers/', verbose_name="الصورة")
    is_active = models.BooleanField(default=True, verbose_name="نشط؟")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "عرض خصم"
        verbose_name_plural = "عروض الخصم"