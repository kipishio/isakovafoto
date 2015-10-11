# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response


# Create your views here.


def index(request):
    index = 'index'
    return render_to_response('myinfo/index.html', {'index': index})


def indexart(request):
    index = 'index'
    return render_to_response('architect/index.html', {'index': index})


def architect_blog_four(request):
    index = 'index'
    return render_to_response('architect/blog_four.html', {'index': index})


def architect_blog_one(request):
    index = 'index'
    return render_to_response('architect/blog_one.html', {'index': index})


def architect_blog_three(request):
    index = 'index'
    return render_to_response('architect/blog_three.html', {'index': index})


def architect_blog_two(request):
    index = 'index'
    return render_to_response('architect/blog_two.html', {'index': index})


def architect_contact(request):
    index = 'index'
    return render_to_response('architect/contact.html', {'index': index})


def architect_pages_404(request):
    index = 'index'
    return render_to_response('architect/pages_404.html', {'index': index})


def architect_pages_grid(request):
    index = 'index'
    return render_to_response('architect/pages_grid.html', {'index': index})


def architect_pages_sample(request):
    index = 'index'
    return render_to_response('architect/pages_sample.html', {'index': index})


def architect_pages_shortcodes(request):
    index = 'index'
    return render_to_response('architect/pages_shortcodes.html', {'index': index})


def architect_portfolio_four(request):
    index = 'index'
    return render_to_response('architect/portfolio_four.html', {'index': index})


def architect_portfolio_one(request):
    index = 'index'
    return render_to_response('architect/portfolio_one.html', {'index': index})


def architect_portfolio_three(request):
    index = 'index'
    return render_to_response('architect/portfolio_three.html', {'index': index})


def architect_portfolio_two(request):
    index = 'index'
    return render_to_response('architect/portfolio_two.html', {'index': index})


def architect_services(request):
    index = 'index'
    return render_to_response('architect/services.html', {'index': index})


def architect_team(request):
    index = 'index'
    return render_to_response('architect/team.html', {'index': index})
