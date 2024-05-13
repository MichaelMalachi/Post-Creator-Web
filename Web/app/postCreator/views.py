from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

class Privacy_Policy(TemplateView):
    template_name = "Privacy_Policy.html"


class HomePostCreatorView(TemplateView):
    template_name = "home_post_creator.html"


class CreatePostView(TemplateView):
    template_name = "create_post.html"