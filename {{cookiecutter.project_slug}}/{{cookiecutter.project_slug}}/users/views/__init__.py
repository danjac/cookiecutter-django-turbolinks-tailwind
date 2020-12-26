# Standard Library
import datetime

# Django
from django.utils import timezone
from django.views.decorators.http import require_POST

from {{cookiecutter.project_slug}}.common.turbo.response import (
    TurboStreamResponse,
)


@require_POST
def accept_cookies(request):
    response = TurboStreamResponse(action="remove", target="accept-cookies")
    response.set_cookie(
        "accept-cookies",
        value="true",
        expires=timezone.now() + datetime.timedelta(days=30),
        samesite="Lax"
    )
    return response
