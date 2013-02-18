# -*- coding: utf-8 -*-
import os
import shutil

from django.utils import unittest
from django.conf import settings
from django.core.files.base import ContentFile

from tests.app.models import Phone1, Phone2


class TestModels(unittest.TestCase):
    def setUp(self):
        self.upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
        if os.path.exists(self.upload_path):
            shutil.rmtree(self.upload_path)

    def test_upload(self):
        phone = Phone1(title='My book')
        phone.price.save('Phone Prices.txt', ContentFile('Phone Prices'))
        phone.save()

        path = os.path.join(self.upload_path, 'phones/prices/phone-prices.txt')
        self.assertTrue(os.path.exists(path))

    def test_field_name(self):
        phone = Phone2(title='My book')

        filename = '.'.join(['a' * 100, 'txt'])
        phone.price.save(filename, ContentFile('Phone Prices'))
        phone.save()

        self.assertEqual(len(str(phone.price)), 100)
        self.assertTrue(str(phone.price).endswith('.txt'))