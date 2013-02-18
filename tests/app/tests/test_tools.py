# -*- coding: utf-8 -*-
from django.utils import unittest
from filefieldtools.tools import (clean_filename, translate_filename,
                                  control_length, upload_to)


class TestTools(unittest.TestCase):
    def test_translate_filename(self):
        value = translate_filename(u'Прайс для клиентов')
        self.assertEqual(value, 'Prays dlya klientov')

    def test_clean_name(self):
        value = clean_filename('   Price_-_.for clients.xls   ')
        self.assertEqual(value, 'Price-for-clients.xls')

        value = clean_filename('Price   for clients')
        self.assertEqual(value, 'Price-for-clients')

        value = clean_filename(u'Прайс для клиентов.xls')
        self.assertEqual(value, 'Prays-dlya-klientov.xls')

    def test_upload_to(self):
        value = upload_to()(None, 'picture.jpg')
        self.assertEqual(value, 'uploads/picture.jpg')

        value = upload_to('books/authors')(None, 'picture.jpg')
        self.assertEqual(value, 'uploads/books/authors/picture.jpg')

        value = upload_to('books/authors', to_lower=False)(None, 'Picture.JPG')
        self.assertEqual(value, 'uploads/books/authors/Picture.JPG')

        value = upload_to('books/authors')(None, 'Picture.JPG')
        self.assertEqual(value, 'uploads/books/authors/picture.jpg')

        value = upload_to('books/authors', to_hash=True)(None, 'Picture.JPG')
        self.assertNotEqual(value, 'uploads/books/authors/picture.jpg')
        self.assertTrue(value.startswith('uploads/books/authors/'))
        self.assertTrue(value.endswith('.jpg'))

    def test_control_length(self):
        # lenght = 49
        value = control_length('uploads/books/authors/client_prices_abcdefghi.xls', 50)
        self.assertEqual(value, 'uploads/books/authors/client_prices_abcdefghi.xls')

        # lenght = 50
        value = control_length('uploads/books/authors/client_prices_abcdefghij.xls', 50)
        self.assertEqual(value, 'uploads/books/authors/client_prices_abcdefghij.xls')

        # length = 51
        value = control_length('uploads/books/authors/client_prices_abcdefghijk.xls', 50)
        self.assertEqual(value, 'uploads/books/authors/client_prices_abcdefghij.xls')

        # length = 51
        value = control_length('uploads/books/authors/client_prices_abcdefghi-k.xls', 50)
        self.assertEqual(value, 'uploads/books/authors/client_prices_abcdefghi.xls')

        # length = 51
        value = control_length('uploads/books/12345678901234567890123/authors/a.xls', 50)
        self.assertEqual(value, 'uploads/books/12345678901234567890123/authors/a.xls')
