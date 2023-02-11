from django.urls import path

from .views import main_view, home_veiw, list_view, listing_view, edit_view, like_listing_view, inqurire_listing_using_email

urlpatterns = [
    path('', main_view, name='main'),
    path('home/', home_veiw, name='home'),
    path('list/', list_view, name='list'),
    path('listing/<str:id>/', listing_view, name='listing'),
    path('listing/<str:id>/edit/', edit_view, name='edit'),
    path('listing/<str:id>/like/', like_listing_view, name='like_listing'),
    path('listing/<str:id>/inquire/', inqurire_listing_using_email, name='inquire_listing'),
]
