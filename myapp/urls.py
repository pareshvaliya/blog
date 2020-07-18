from django.urls import path
from myapp.views import index,detail,PostCreate,like

app_name = 'myapp'

urlpatterns = [
	path('',index,name = 'index'),
	# here the pk is variavle of type int which stores 
	# the primary key coming from index.html
	# for ex. if pk =1 then path becomes detail/1/
	# from here the control goes to the detail view as written below
	# that when any one come for detail/pk path redirects to the detail views
	path('detail/<int:pk>/',detail,name = 'detail'),
	path('create/',PostCreate.as_view(),name = 'create'),
	path('ajax/like/',like,name = 'like'),
]