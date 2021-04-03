from allauth.socialaccount import views as socialaccount_views
from turbo_response.mixins import TurboFormAdapterMixin


class SignupView(TurboFormAdapterMixin, socialaccount_views.SignupView):
    ...


signup = SignupView.as_view()
