from django.urls import path
from . import views




urlpatterns = [
    # Function Based Views-----
    #path('', views.contactPage),
    #path('ajax/contact', views.postContact, name ='contact_submit'),
    #----Class Based views
    path('', views.ContactAjax.as_view(), name = 'contact_submit'), #Class Based views


]
