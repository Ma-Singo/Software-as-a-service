from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse


from helpers import stripe_template


User = get_user_model()

class SubscriptionStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    TRIALING = 'trialing', 'Trialing'
    INCOMPLETE = 'incomplete', 'Incomplete'
    INCOMPLETE_EXPIRED = 'incomplete_expired', 'Incomplete Expired'
    PAST_DUE = 'past_due', 'Past Due'
    CANCELED = 'canceled', 'Canceled'
    UNPAID = 'unpaid', 'Unpaid'
    PAUSED = 'paused', 'Paused'


class Subscription(models.Model):

    class Subscription_Permissions(models.TextChoices):
        BASIC = 'basic', 'Basic'
        PRO = "pro", "Pro"
        ADVANCED = 'advanced', "Advanced"

    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    permission_level = models.CharField(max_length=15, choices=Subscription_Permissions.choices, default=Subscription_Permissions.BASIC)
    stripe_product_id = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]
        permissions = [
            ("basic_access", "Can access basic features"),
            ("pro_access", "Can access professional features"),
            ("advance_access", "Can access advanced features"),
        ]
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.stripe_product_id:
            product_id = stripe_template.create_product(
                name=self.name,
                metadata={
                    "subscription_id": self.id
                }
            )
            self.stripe_product_id = product_id
        super().save(*args, **kwargs)


    
    @property
    def has_basic_access(self):
        return self.is_active and self.permission_level in ['basic', 'pro', 'advance']
    
    @property
    def has_pro_access(self):
        return self.is_active and self.permission_level in ['pro', 'advance']
    
    @property
    def has_advance_access(self):
        return self.is_active and self.permission_level == 'advance'



class SubscriptionPrice(models.Model):

    class IntervalChoices(models.TextChoices):
        DAY = "day", "Daily"
        WEEKLY = "week", "Weekly"
        MONTHLY = "month", "Monthly"
        YEARLY = "year", "Yearly"

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subscription_prices"
        )
    
    interval = models.CharField(
        max_length=10, 
        choices=IntervalChoices.choices,
        default=IntervalChoices.MONTHLY)
    interval_count = models.PositiveIntegerField(default=1)
    unit_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=9.99,
        )
    currency = models.CharField(max_length=3, default='usd')
    stripe_price_id = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True,)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-unit_amount"]

    def __str__(self):
        return f"{self.product.name} - ${self.unit_amount} / {self.interval}"
    
    @property
    def product_id(self):
        if not self.subscription:
            return None
        return self.subscription.stripe_product_id
    
    @property
    def stripe_price(self):
        return int(self.price * 100)
    
    @property
    def product_name(self):
        if not self.subscription:
            return None
        return self.subscription.name
    

    def save(self, *args, **kwargs):
        if not self.stripe_price_id and self.product_id is not None:
            price_id = stripe_template.create_price(
                currency=self.currency,
                product=self.product_id,
                recurring={"interval": self.interval},
                product_data={"name": self.product_name},
                meta={
                    'Subscription_price': self.id
                }
            )

            self.stripe_price = price_id
        super().save(*args, **kwargs)

    

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_id = models.CharField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=SubscriptionStatus.choices, blank=True, null=True)
    current_period_start = models.DateTimeField(blank=True, null=True)
    current_period_end = models.DateTimeField(blank=True, null=True)
    cancel_at_period_end = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - ({self.status})"
    
    def get_absolute_url(self):
        return reverse("user_subscription")
    
    @property
    def is_active(self):
        return self.status in ['trialing', 'active']
    
    @property
    def is_trialing(self):
        return self.status == 'trialing' and self.trial_end and self.trial_end > timezone.now()

