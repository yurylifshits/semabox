#!/usr/bin/env python

import os
import sys
import django.core.handlers.wsgi

sys.path.append('/home/sb/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = django.core.handlers.wsgi.WSGIHandler()
