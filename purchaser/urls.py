from django.urls import path
from . import views

urlpatterns = [
   path('create/',views.create,name='purchaser.create'),
   path('create/save/',views.save,name='purchaser.save'),
   path('<int:id>/',views.detail,name='purchaser.detail')
]
