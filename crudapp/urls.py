from django.urls import path,include
from . import views
urlpatterns = [
 path("",views.index,name="index"),
 path("insert/",views.insertdata,name="insert"),
path("insertdata",views.contactme,name="insertdata"),
path("conta/",views.conta,name="conta"),
path("editpage/<int:pk>",views.editdata,name="editpage"),
path("updatebaby",views.updatebaby,name="updatebaby"),
path("deldata/<int:dele>",views.deldata,name="deldata"),
path("register",views.register,name="register"),

]