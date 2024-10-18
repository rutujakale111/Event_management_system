from rest_framework import serializers
from .models import Event, Invitation

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'start_time', 'end_time']

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ['id', 'event', 'attendee', 'rsvp_status', 'rsvp_time']