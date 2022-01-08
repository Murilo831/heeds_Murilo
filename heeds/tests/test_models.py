
from django.test import TestCase
from model_mommy import mommy

from ..models import Search


class SearchTestCase(TestCase):

    def test_create(self):
        self.data = Search.objects.create(
            address='Dubai'
        )
        self.data.save()

    def test_str(self):
        self.assertEquals(str(self.data), 'Dubai')

