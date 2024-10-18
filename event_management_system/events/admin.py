from django.contrib import admin
from django.contrib import admin
from .models import Event, Attendee, Invitation

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_time', 'end_time')
    search_fields = ('name', 'location')
    list_filter = ('start_time', 'end_time')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('event', 'attendee', 'rsvp_status', 'rsvp_time')
    list_filter = ('rsvp_status', 'rsvp_time')
    search_fields = ('attendee__name', 'event__name')
    actions = ['mark_as_accepted', 'mark_as_declined']

    def mark_as_accepted(self, request, queryset):
        queryset.update(rsvp_status='Yes')
    mark_as_accepted.short_description = "Mark selected invitations as accepted"

    def mark_as_declined(self, request, queryset):
        queryset.update(rsvp_status='No')
    mark_as_declined.short_description = "Mark selected invitations as declined"

admin.site.site_header = "Event Management Admin"
admin.site.site_title = "Event Management Portal"
admin.site.index_title = "Welcome to the Event Management Portal"

admin.site.register(Event, EventAdmin)
admin.site.register(Attendee)
admin.site.register(Invitation, InvitationAdmin)
