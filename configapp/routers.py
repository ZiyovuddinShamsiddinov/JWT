from rest_framework.routers import DefaultRouter
from configapp.views import *

router = DefaultRouter()
router.register(r"", MovieCreateView, basename="movie_api")
router.register(r"", MovieCreateView, basename="actor_api")
