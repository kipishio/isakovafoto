# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response


# Create your views here.


def index(request):
    index = 'index'
    return render_to_response('myinfo/index.html', {'index': index})
