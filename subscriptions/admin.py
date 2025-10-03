from django.contrib import admin

from subscriptions.models import (
    Subscription,
    SubscriptionPrice
)

admin.site.register(Subscription)
admin.site.register(SubscriptionPrice)