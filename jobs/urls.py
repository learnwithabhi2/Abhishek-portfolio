from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-offer/', views.submit_offer, name='submit_offer'),
    path('submission/', views.submission_list, name='submission_list'),  # ✅ Add this
]
