from django.urls import path
from reservation_app import views

# URL path to access the page using browser
urlpatterns = [
    path('', views.SeatReservationList.as_view(), name="home-page"),
    path('cabin-entry/', views.CabinList.as_view(), name='cabin-entry')
]
