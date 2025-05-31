from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = 'Seed the database with sample listings'
    
    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Cozy Cottage", "description": "A beautiful place to relax", "price": 120.50},
            {"title": "Luxury Apartment", "description": "Fully furnished with a city view", "price": 250.00},
        ]
        
        for data in sample_listings:
            Listing.objects.create(**data)
            
            
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))