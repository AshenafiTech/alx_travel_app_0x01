from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    host = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'host', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.StringRelatedField(read_only=True)
    listing = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'guest', 'check_in', 'check_out', 'created_at']