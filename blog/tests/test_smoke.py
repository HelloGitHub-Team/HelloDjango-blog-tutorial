from django.test import TestCase


class SmokeTestCase(TestCase):
    def test_smoke(self):
        self.assertEqual(1 + 1, 2)
