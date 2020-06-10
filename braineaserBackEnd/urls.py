
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User
from django.contrib import admin
from braineaserAPI.views import Clients, Users, register_user, login_user, Interventions, BaselineAnxietyScores, UserInterventions, Prompts, Journals

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'clients', Clients, 'client')
router.register(r'users', Users, 'user')
router.register(r'interventions', Interventions, 'intervention')
router.register(r'user_interventions', UserInterventions, 'user_intervention')
router.register(r'baseline', BaselineAnxietyScores, 'baselineAnxietyScore')
router.register(r'prompts', Prompts, 'prompt')
router.register(r'journals', Journals, 'journal')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]