from django.views.generic import TemplateView


class SignInView(TemplateView):
    template_name = "Sign_in.html"

class WelcomeView(TemplateView):
    template_name = "Welcome.html"