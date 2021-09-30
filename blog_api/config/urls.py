from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),

    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
