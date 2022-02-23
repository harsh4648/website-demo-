

from django.urls import path
from .import views

urlpatterns = [
    path("", views.index,name='shop Home'),
    path("about",views.about,name='AboutUs'),
    path("contact",views.contact,name='contact'),
    path("tracker",views.tracker,name='track your order '),
    path("products/<int:myid>",views.productview,name='productview'),
    path("checkout",views.checkout,name='checkout'),
    path("checkout1",views.checkout1,name='checkout1'),
    path("search",views.search,name='search'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
