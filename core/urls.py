
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.url')),
    path('product/', include('product.url')),
]

schema_url_patterns = [
    path('schema/',get_schema_view(
        title="jewelry shop",
        description='api endpoint for jewelry shop management',
        version='1.0',
        ), name='open api schema'),

    path('doc/',include_docs_urls(title='jewelry shop api'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.extend(schema_url_patterns)

