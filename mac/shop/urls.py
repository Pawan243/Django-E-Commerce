from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackerStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.products, name="Products"),
    path("checkout/", views.checkout, name="Checkout"),
    path('register/',views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
