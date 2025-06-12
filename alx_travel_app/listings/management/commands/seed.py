from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        # Create a sample user if not exists
        user, created = User.objects.get_or_create(
            username='samplehost',
            defaults={'email': 'host@example.com', 'password': 'password123'}
        )

        # Sample listings data
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A nice and cozy apartment in the heart of the city.',
                'location': 'Downtown',
                'price_per_night': 100.00,
                'host': user,
            },
            {
                'title': 'Beachside Villa',
                'description': 'Enjoy the sea breeze in this beautiful villa.',
                'location': 'Beachside',
                'price_per_night': 250.00,
                'host': user,
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'A peaceful cabin in the mountains.',
                'location': 'Mountain',
                'price_per_night': 150.00,
                'host': user,
            },
        ]

        for data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))