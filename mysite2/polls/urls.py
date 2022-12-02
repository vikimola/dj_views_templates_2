from django.urls import path
from . import views
urlpatterns =[
    path("home", views.home, name="home"),
    path("add_owner", views.add_owner, name="add_owner"),
    path("add_pet", views.add_pet, name="add_pet"),
    path("list_of_owners", views.list_of_owners, name="list_of_owners"),
    path("list_of_owners/<int:owner_id>", views.owner_profile, name="owner_profile"),

    path("owners", views.OwnersList.as_view(), name="list_of_owners_2"),
    path("owner/<int:pk>", views.OwnerDetails.as_view(), name="owner_details"),

    path("cookie", views.cookie, name="cookie"),
    path("sessfun", views.sessfun, name="sessfun"),

    # dj tutorial 4
    path("detail", views.detail, name="detail"),

]