# settings/urls.py

from django.contrib import admin
from django.urls import path
from postCreator.views import HomeView, PrivacyPolicyView, HomePostCreatorView, CreatePostView
from accounts.views import SignInView, WelcomeView, LogoutView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from keys.views import KeysView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeView.as_view(), name="home-link"),
                  path('sign_in/', SignInView.as_view(), name="sign_in-link"),
                  path('welcome/', WelcomeView.as_view(), name="welcome-link"),
                  path('home/', HomePostCreatorView.as_view(), name="home_post_creator-link"),
                  path('create_post/', CreatePostView.as_view(), name="create_post-link"),
                  path('Privacy_Policy/', PrivacyPolicyView.as_view(), name="Privacy_Policy-link"),
                  path('Privacy_Policy.html', RedirectView.as_view(url='/Privacy_Policy/')),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('keys.json', KeysView.as_view(), name='keys'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)