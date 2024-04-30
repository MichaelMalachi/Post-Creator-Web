from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"

class Privacy_Policy(TemplateView):
    template_name = "Privacy_Policy.html"