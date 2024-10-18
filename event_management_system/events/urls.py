from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, InvitationViewSet, event_list, event_create, event_update, event_delete

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'invitations', InvitationViewSet)


urlpatterns = [
    path('', event_list, name='event_list'),
    path('create/', event_create, name='event_create'),
    path('update/<int:pk>/', event_update, name='event_update'),
    path('delete/<int:pk>/', event_delete, name='event_delete'),
    path('', include(router.urls)),
]