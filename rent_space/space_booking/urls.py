from django.urls import path

from .views import ApprovedAdSpaceList, CreateAdSpace, GetAdSpace, UpdateAdSpace, DeleteAdSpace, NotApprovedAdSpaceList, \
    AdSpaceListByOwner
from .views import BookingListView, BookingCreateView, BookingDeleteView
from .views import CreateAdSpace, GetAdSpace, UpdateAdSpace, DeleteAdSpace
from .views import BookingListView, BookingCreateView, BookingDeleteView, FetchBookings, BookingListByClient
from .views import PaymentList, CreatePayment, GetPayment, UpdatePayment, DeletePayment
from .views import RatingList, CreateRating, GetRating, UpdateRating, DeleteRating

urlpatterns = [
    path('get-all-adspaces/', ApprovedAdSpaceList.as_view(), name='get-all-adspaces'),
    path('get-unapproved-adspaces/', NotApprovedAdSpaceList.as_view(), name='get-unapproved-adspaces'),
    path('adspaces/owner/<int:ownerId>/', AdSpaceListByOwner.as_view(), name='adspace-list-by-owner'),
    path('get-all-bookings/', FetchBookings.as_view(), name='get_all_bookings'),
    path('create-adspace/', CreateAdSpace.as_view(), name='create-adspace'),
    path('adspace/<int:pk>/', GetAdSpace.as_view(), name='get-adspace'),
    path('adspace/<int:pk>/update/', UpdateAdSpace.as_view(), name='update-adspace'),
    path('adspace/<int:pk>/delete/', DeleteAdSpace.as_view(), name='delete-adspace'),

    path('get-all-ratings/', RatingList.as_view(), name='get-all-ratings'),
    path('create-rating/', CreateRating.as_view(), name='create-rating'),
    path('rating/<int:pk>/', GetRating.as_view(), name='get-rating'),
    path('rating/<int:pk>/update/', UpdateRating.as_view(), name='update-rating'),
    path('rating/<int:pk>/delete/', DeleteRating.as_view(), name='delete-rating'),

    path('new-booking/', BookingCreateView.as_view(), name='new-booking'),
    path('bookings/client/<int:clientId>/', BookingListByClient.as_view(), name='booking-list-by-client'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDeleteView.as_view(), name='booking-delete'),

    path('payments/', PaymentList.as_view(), name='payment'),
    path('payments/<int:pk>/', DeletePayment.as_view(), name='payment-delete'),
    path('payments/<int:pk>/update/', UpdatePayment.as_view(), name='payment-update'),
    path('payments/<int:pk>', GetPayment.as_view(), name='get-payment'),
    path('create/payments/', CreatePayment.as_view(), name='create-payment')
]
