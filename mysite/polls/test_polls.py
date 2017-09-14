from django.test import TestCase

class PollTestCase(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_something(self):
        self.assertEqual(True, True)
