# -*- coding: utf-8 -*-
from django.conf import settings


FILEFIELDTOOLS_DIR = getattr(settings, 'FILEFIELDTOOLS_DIR', 'uploads')
FILEFIELDTOOLS_WHITESPACE = getattr(settings, 'FILEFIELDTOOLS_WHITESPACE', '-')
