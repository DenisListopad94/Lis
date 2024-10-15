"""
URL configuration for TaskTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from base.views import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from TaskTracker import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('tasks/', include('task_tracker.urls')),
    # path('comments/', include('task_tracker.urls')),
    path('tags/', include('task_tracker.tags_page.urls')),
    path('', include('base.urls')),
    # path('base/main/tasks/', views.task),
    path('base/main/tasks/users/', views.users),
    path('api-auth/', include('rest_framework.urls')),
]+ debug_toolbar_urls()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)