from rest_framework.routers import DefaultRouter
from configapp.views import MovieApi, ActorApi

router = DefaultRouter()
router.register(r"", MovieApi, basename="movie_api")
router.register(r"", ActorApi, basename="actor_api")
