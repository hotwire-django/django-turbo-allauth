# Third Party Libraries
from allauth.socialaccount import views as socialaccount_views

# Local
from ..mixins import TurboFormMixin


class SignupView(TurboFormMixin, socialaccount_views.SignupView):
    ...


signup = SignupView.as_view()
