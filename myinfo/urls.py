# -*- coding: utf-8 -*-
__author__ = 'Юля'

from django.conf.urls import patterns, url
from myinfo import views

urlpatterns = patterns('',
                       url(r'^$', views.indexart, name='indexart'),
                       # url(r'^$', views.indexart, name='indexart'),
                       url(r'^index.html/$', views.indexart, name='indexart'),
                       url(r'^blog_four.html/$', views.architect_blog_four, name='architect_blog_four'),
                       url(r'^blog_one.html/$', views.architect_blog_one, name='architect_blog_one'),
                       url(r'^blog_three.html/$', views.architect_blog_three, name='architect_blog_three'),
                       url(r'^blog_two.html/$', views.architect_blog_two, name='architect_blog_two'),
                       url(r"^contact.html/$", views.architect_contact, name='architect_contact'),
                       url(r'^pages_404.html/$', views.architect_pages_404, name='architect_pages_404'),
                       url(r'^pages_grid.html/$', views.architect_pages_grid, name='architect_pages_grid'),
                       url(r'^pages_sample.html/$', views.architect_pages_sample,
                           name='architect_pages_sample'),
                       url(r'^pages_shortcodes.html/$', views.architect_pages_shortcodes,
                           name='architect_pages_shortcodes'),
                       url(r'^portfolio_four.html/$', views.architect_portfolio_four,
                           name='architect_portfolio_four'),
                       url(r'^portfolio_one.html/$', views.architect_portfolio_one,
                           name='architect_portfolio_one'),
                       url(r'^portfolio_three.html/$', views.architect_portfolio_three,
                           name='architect_portfolio_three'),
                       url(r'^portfolio_two.html/$', views.architect_portfolio_two,
                           name='architect_portfolio_two'),

                       url(r'^services.html/$', views.architect_services,
                           name='architct_services'),
                       url(r'^team.html/$', views.architect_team,
                           name='architect_team'),

                       # url(r'^architect/$', views.indexart, name='indexart'),
                       # url(r'^architect/index.html/$', views.indexart, name='indexart'),
                       # url(r'^architect/blog_four.html/$', views.architect_blog_four, name='architect_blog_four'),
                       # url(r'^architect/blog_one.html/$', views.architect_blog_one, name='architect_blog_one'),
                       # url(r'^architect/blog_three.html/$', views.architect_blog_three, name='architect_blog_three'),
                       # url(r'^architect/blog_two.html/$', views.architect_blog_two, name='architect_blog_two'),
                       # url(r"^architect/contact.html/$", views.architect_contact, name='architect_contact'),
                       # url(r'^architect/pages_404.html/$', views.architect_pages_404, name='architect_pages_404'),
                       # url(r'^architect/pages_grid.html/$', views.architect_pages_grid, name='architect_pages_grid'),
                       # url(r'^architect/pages_sample.html/$', views.architect_pages_sample,
                       #     name='architect_pages_sample'),
                       # url(r'^architect/pages_shortcodes.html/$', views.architect_pages_shortcodes,
                       #     name='architect_pages_shortcodes'),
                       # url(r'^architect/portfolio_four.html/$', views.architect_portfolio_four,
                       #     name='architect_portfolio_four'),
                       # url(r'^architect/portfolio_one.html/$', views.architect_portfolio_one,
                       #     name='architect_portfolio_one'),
                       # url(r'^architect/portfolio_three.html/$', views.architect_portfolio_three,
                       #     name='architect_portfolio_three'),
                       # url(r'^architect/portfolio_two.html/$', views.architect_portfolio_two,
                       #     name='architect_portfolio_two'),
                       #
                       # url(r'^architect/services.html/$', views.architect_services,
                       #     name='architct_services'),
                       # url(r'^architect/team.html/$', views.architect_team,
                       #     name='architect_team'),



                       )
