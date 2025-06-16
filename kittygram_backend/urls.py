from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from cats.views import AchievementViewSet, CatViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),  # Работа с пользователями
    path('api/', include('djoser.urls.authtoken')),  # Работа с токенами
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
{
    "username": "User1",
    "password": "!TestUser1"

    "auth_token": "90518850b0e4087ce012e346e88bf81faf8ef02f"
}
'''