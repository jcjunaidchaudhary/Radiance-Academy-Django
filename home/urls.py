from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("neet",views.neet, name="neet"),
    path("jee",views.jee, name="jee"),
    path("mhcet",views.mhcet, name="mhcet"),
    path("ssc&hsc",views.sschsc, name="ssc&hsc"),
    path("contact",views.contact, name="contact"),
    path("success",views.success, name="success"),
    path("result",views.result, name="result"),
    path("gallery",views.gallery, name="gallery"),
    path("download",views.download, name="download"),
    path("view-pdf/<int:id>",views.viewpdf,name="view-pdf"),
    path("notice-pdf/<int:id>",views.noticepdf,name="notice-pdf"),
    path("notice/<int:id>",views.notice,name="notice")
    

]
