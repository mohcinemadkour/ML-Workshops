from django.conf.urls import url,include
from .import views
from django.contrib.auth.views import login

urlpatterns = [
 url(r'^home/$',views.home),
 url(r'^search/$',views.search),
 #url(r'^$',views.home),
 url(r'^MedEngine/$',views.Upload),
 #url(r'^MedEngine/MedEx/',views.MedEx),
 #url(r'^MedEngine/MetaMap/',views.MetaMap),
 #url(r'^MedEngine/cliner/',views.cliner),
 #url(r'^MedEngine/relationextractor/',views.relationextractor),
 url(r'^graph/$',views.graph)
 #url(r'^design/$',views.design)
 #url(r'^login/$',login,{'template_name':'myapp/login.html'})
]

# model_folder ./models/NN_models/Test_November