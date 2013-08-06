from django.conf.urls import patterns, url

urlpatterns = patterns('apps.team.views',
    url(r'^ajax/get_member/(?P<pk>[0-9]+)/$', 'get_member', name='team_get_member'),
    url(r'^member/publication/(?P<slug>.+)/$', 'generic_page', name='team_publication_item'),
    url(r'^publications/$', 'generic_page', name='team_articles_list'),

)
