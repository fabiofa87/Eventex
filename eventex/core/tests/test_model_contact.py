from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Fabio Faria',
            slug='fabio-faria',
            photo='http://hbn.link/hb-pic',
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='fabio@faria.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-99999-9999'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P."""
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B'
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='fabio@faria.com'
        )
        self.assertEqual('fabio@faria.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Fabio Faria',
            slug='fabio-faria',
            photo='http://hbn.link/hb-pic',
        )
        s1 = s.contact_set.create(kind=Contact.EMAIL, value='fabio@faria.com')
        s2 = s.contact_set.create(kind=Contact.PHONE, value='21-99999-9999')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = self.s1 = ['fabio@faria.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = self.s2 = ['21-99999-9999']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)