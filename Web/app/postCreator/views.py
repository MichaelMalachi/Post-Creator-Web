# postCreator/views.py

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

class PrivacyPolicyView(TemplateView):
    template_name = "Privacy_Policy.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_post_creator-link')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = redirect('welcome-link')
        response.set_cookie('privacy_accepted', 'true')
        return response

@method_decorator(ensure_csrf_cookie, name='dispatch')
class HomePostCreatorView(TemplateView):
    template_name = "home_post_creator.html"

class CreatePostView(TemplateView):
    template_name = "create_post.html"
