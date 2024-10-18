from django.db import models
from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    RSVP_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Pending', 'Pending')
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='invitations')
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='invitations')
    rsvp_status = models.CharField(max_length=10, choices=RSVP_CHOICES, default='Pending')
    rsvp_time = models.DateTimeField(null=True, blank=True)

    def clean(self):
        overlapping_invitations = Invitation.objects.filter(
            attendee=self.attendee,
            event__start_time__lt=self.event.end_time,
            event__end_time__gt=self.event.start_time
        ).exclude(id=self.id)

        if overlapping_invitations.exists():
            raise ValidationError(f'{self.attendee.name} has already RSVP\'d for an overlapping event.')

    def __str__(self):
        return f'{self.attendee.name} - {self.event.name}'
