# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import hashlib
import trans

from django.conf import settings
from django.utils.encoding import smart_str, smart_unicode

from filefieldtools import settings as app_settings


def translate_filename(filename):
    filename = smart_unicode(filename)
    filename = filename.encode('trans')
    filename = smart_str(filename)
    return filename


def clean_filename(filename):
    whitespace = app_settings.FILEFIELDTOOLS_WHITESPACE
    filename = translate_filename(filename)
    name, ext = os.path.splitext(filename)
    name = re.sub(r'\W|_', ' ', name)
    name, ext = name.strip(), ext.strip()
    name = re.sub(r'\s{2,}', ' ', name)
    name = re.sub(r'\s', whitespace, name)
    return ''.join([name, ext])


def rename_to_hash(filename):
    timestamp = str(time.mktime(datetime.datetime.now().timetuple()))
    h = hashlib.sha1()
    h.update(settings.SECRET_KEY)
    h.update(smart_str(filename))
    h.update(timestamp)
    name, ext = os.path.splitext(filename)
    return ''.join([h.hexdigest()[:25], ext])


def control_length(filepath, max_length):
    max_length = int(max_length)
    if len(filepath) > max_length:
        path = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)
        number = len(filepath) - max_length
        if len(name) - number >= 1:
            whitespace = app_settings.FILEFIELDTOOLS_WHITESPACE
            name = name[:len(name) - number]
            name = name.strip(whitespace)
            return os.path.join(path, ''.join([name, ext]))
    return filepath


def _upload_to(instance, filename,
               path=None, to_hash=False,
               to_lower=True, field_name=None):
    
    upload_dir = app_settings.FILEFIELDTOOLS_DIR
    upload_dir = upload_dir.strip(os.pathsep)

    if path is None:
        path = upload_dir
    else:
        path = os.path.join(upload_dir, path)

    if to_hash:
        filename = rename_to_hash(filename)
    else:
        filename = clean_filename(filename)

    if to_lower:
        filename = filename.lower()

    filepath = os.path.join(path, filename)
    if not field_name is None:
        opts = instance._meta
        field = opts.get_field(field_name)
        max_length = getattr(field, 'max_length')
        return control_length(filepath, max_length)
    return filepath


def upload_to(*args, **kwargs):
    if len(args) > 0:
        kwargs.update({'path': args[0]})
    return lambda instance, filename: _upload_to(instance, filename, **kwargs)
