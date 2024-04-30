from django.contrib import admin
from django.urls import path
from postCreator.views import HomeView, Privacy_Policy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home-link"),
    path('Privacy_Policy/', Privacy_Policy.as_view(), name="Privacy_Policy-link"),
        path('Privacy_Policy.html', RedirectView.as_view(url='/Privacy_Policy/')),
]
