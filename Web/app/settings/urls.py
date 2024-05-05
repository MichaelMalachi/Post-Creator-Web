from django.contrib import admin
from django.urls import path
from postCreator.views import HomeView, Privacy_Policy, HomePostCreatorView
from accounts.views import SignInView, WelcomeView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home-link"),
    path('sign_in/', SignInView.as_view(), name="sign_in-link"),
    path('welcome/', WelcomeView.as_view(), name="welcome-link"),
    path('home/', HomePostCreatorView.as_view(), name="home-link"),
    path('Privacy_Policy/', Privacy_Policy.as_view(), name="Privacy_Policy-link"),
        path('Privacy_Policy.html', RedirectView.as_view(url='/Privacy_Policy/')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)