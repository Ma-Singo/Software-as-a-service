import stripe 
from decouple import config

STRIPE_SECRET_KEY=config("STRIPE_SECRET_KEY", default="", cast=str)

stripe.api_key = STRIPE_SECRET_KEY

def create_customer(name: str, email: str, metadata: dict):
    response = stripe.Customer.create(
        name=name,
        email=email,
        metadata=metadata,
    )
    stripe_id = response.id 
    return stripe_id