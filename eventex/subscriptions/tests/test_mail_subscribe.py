from django.test import TestCase

from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Fabio Faria', cpf='12345678901', email='fabio@faria.com', phone='21-999292929')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'fabiofa87@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['fabiofa87@gmail.com', 'fabio@faria.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Fabio Faria',
            '12345678901',
            'fabio@faria.com',
            '21-999292929',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
