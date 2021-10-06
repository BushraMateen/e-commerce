from django.conf.urls import url
from webapp.views import productApi
from webapp import views

urlpatterns=[
    url(r'product$',views.productApi),
    url(r'^product/([a-zA-Z0-9]*)$',views.productApi)
]

