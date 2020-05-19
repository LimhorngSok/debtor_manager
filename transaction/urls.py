from django.urls import path
from . import views

urlpatterns = [
   path('<int:user>/red/create',views.createRed,name='transaction.red.create'),
   path('<int:user>/red/save',views.saveRed,name='transaction.red.save'),
   path('<int:user>/red/view/<int:id>',views.viewRed,name='transaction.red.view'),
   path('<int:user>/green/create',views.createGreen,name='transaction.green.create'),
   path('<int:user>/green/save',views.saveGreen,name='transaction.green.save'),
   path('<int:user>/green/view/<int:id>',views.viewGreen,name='transaction.green.view'),
]
