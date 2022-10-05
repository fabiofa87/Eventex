from django.test import TestCase

from eventex.core.managers import PeriodManager
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
            description='Descrição da palestra',
            start='10:00',
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many speakers and vice-versa"""
        self.talk.speakers.create(
            name='Fabio Faria',
            slug='fabio-faria',
            website='http://fabiofaria.net',
        )
        self.assertEqual(1, self.talk.speakers.count())

    def test_blank_fields(self):
        contents = [
            'description',
            'start',
            'speakers'
        ]
        for expect in contents:
            with self.subTest():
                field = self.talk._meta.get_field(expect)
                self.assertTrue(field.blank)

    def start_null(self):
        field = self.talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(
            title="Morning Talk",
            start="11:59",
        )
        Talk.objects.create(
            title="Afternoon Talk",
            start="12:00",
        )

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
