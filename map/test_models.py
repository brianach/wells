from django.test import TestCase
from .models import Well


class WellModelTestCase(TestCase):
    def setUp(self):
        # Create a sample Well object for testing
        self.well = Well.objects.create(
            well="Sample Well",
            townland="Sample Townland",
            county="Sample County",
            longitude=12.3456,
            latitude=78.9012,
            cures="Sample Cures"
        )

    def test_well_str(self):
        # Check the __str__ method of the Well model
        self.assertEqual(str(self.well), "Sample Well")

    def test_well_fields(self):
        # Check individual fields of the Well model
        self.assertEqual(self.well.well, "Sample Well")
        self.assertEqual(self.well.townland, "Sample Townland")
        self.assertEqual(self.well.county, "Sample County")
        self.assertEqual(self.well.longitude, 12.3456)
        self.assertEqual(self.well.latitude, 78.9012)
        self.assertEqual(self.well.cures, "Sample Cures")
