from allauth.account import views as account_views
from turbo_response.mixins import TurboFormAdapterMixin


class LoginView(TurboFormAdapterMixin, account_views.LoginView):
    ...


login = LoginView.as_view()


class SignupView(TurboFormAdapterMixin, account_views.SignupView):
    ...


signup = SignupView.as_view()


class EmailView(TurboFormAdapterMixin, account_views.EmailView):
    ...


email = EmailView.as_view()


class PasswordChangeView(TurboFormAdapterMixin, account_views.PasswordChangeView):
    ...


password_change = PasswordChangeView.as_view()


class PasswordSetView(TurboFormAdapterMixin, account_views.PasswordSetView):
    ...


password_set = PasswordSetView.as_view()


class PasswordResetView(TurboFormAdapterMixin, account_views.PasswordResetView):
    ...


password_reset = PasswordResetView.as_view()


class PasswordResetFromKeyView(
    TurboFormAdapterMixin, account_views.PasswordResetFromKeyView
):
    ...


password_reset_from_key = PasswordResetFromKeyView.as_view()
