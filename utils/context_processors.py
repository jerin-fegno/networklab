from django.conf import settings as global_settings


def settings(request):
    """
    Add static-related context variables to the context.
    """
    return {"settings": global_settings}
