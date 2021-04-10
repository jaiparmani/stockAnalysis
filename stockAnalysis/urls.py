from django.urls import path
from . import views

app_name="stockAnalysis"

urlpatterns = [
    path("stockDetail/<str:symbol>", views.stockDetail),
    path("stockList", views.stockList, name="stockList")
]
