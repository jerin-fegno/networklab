from django.views.generic import TemplateView


class GeneralInstructions(TemplateView):
    template_name = 'dashboard/general-instructions.html'
    extra_context = {
        'challenge_title': "General Instructions",
    }


