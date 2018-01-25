from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import beers.urls

apps_urls = [
    beers.urls,
]

pattern = [
    url(r'', include(app_url))
    for app_url in apps_urls
]


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^api/',
        include(
            pattern,
            namespace='api',
        ),
    ),
]

"""
URL settings for rosetta if instaled.
"""

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns += [
        url(
            r'^__debug__/',
            include(
                debug_toolbar.urls,
            ),
        ),
    ] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))