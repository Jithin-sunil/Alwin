from django.urls import path
from Admin import views
app_name='Admin'
urlpatterns = [
    path('District/',views.District,name="District"),
    path('Adminreg/',views.Adminreg,name="Adminreg"),
    path('Type/',views.Type,name="Type"),
    path('deltype/<int:id>',views.deltype,name="deltype"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
    path('edittype/<int:id>',views.edittype,name="edittype"),
    path('place/',views.place,name="place"),
    path('delplace/<int:id>',views.delplace,name="delplace"),
    path('editplace/<int:id>',views.editplace,name="editplace"),
]