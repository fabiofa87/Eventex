from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Fabio Faria', cpf='12345678901', email='fabio@faria.com', phone='21-999292929')
        self.response = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_detail.html')

    def test_content(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, response.status_code)