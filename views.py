# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', {})
