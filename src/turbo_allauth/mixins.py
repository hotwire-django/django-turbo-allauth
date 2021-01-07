# Standard Library
import http

# Django
from django.http import HttpResponseRedirect


class TurboFormMixin:
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form),
            status=http.HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        if isinstance(response, HttpResponseRedirect):
            response.status_code = http.HTTPStatus.SEE_OTHER
        return response
