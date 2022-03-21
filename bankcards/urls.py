from django.urls import path
from .views import *


urlpatterns = [
    path("",Index,name = "home"),
    path("Credit/",CreditView,name="credit"),
    path("Debet/",DebetView,name="debet"),
    path("Update/<int:pk>",CardUpdateView.as_view(),name="update"),
    path("Detail/<int:pk>",CardDetailView.as_view(),name="detail"),
    path("Delete/<int:pk>",CardDeleteView.as_view(),name="delete"),
    path("Createcredit",CreateCreditCard,name="createcredit"),
    path("Createdebet",CreateDebetCard,name="createdebet"),
    path("SearchCreditresults/",SearchCreditResultsView.as_view(),name="searchcredit_results"),
    path("SearchDebetresults/",SearchDebetResultsView.as_view(),name="searchdebet_results"),
]