# Third Party Libraries
from allauth.socialaccount import views as socialaccount_views
from turbo_response.mixins import TurboFormMixin


class SignupView(TurboFormMixin, socialaccount_views.SignupView):
    ...


signup = SignupView.as_view()
