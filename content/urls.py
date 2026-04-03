from rest_framework.routers import DefaultRouter

from .views import ContentView

app_name = "content"

router = DefaultRouter()

router.register("content", ContentView)

urlpatterns = router.urls
