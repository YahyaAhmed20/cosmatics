# home


from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services, name='services'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),

    path('order-summary/<int:service_id>/', views.order_summary, name='order_summary'),
    path('payment/', views.payment, name='payment'),
    path('payment-success/', views.payment_success, name='payment_success'),

   

    
]