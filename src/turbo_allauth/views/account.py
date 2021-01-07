# Third Party Libraries
from allauth.account import views as account_views

# Local
from ..mixins import TurboFormMixin


class LoginView(TurboFormMixin, account_views.LoginView):
    ...


login = LoginView.as_view()


class SignupView(TurboFormMixin, account_views.SignupView):
    ...


signup = SignupView.as_view()


class EmailView(TurboFormMixin, account_views.EmailView):
    ...


email = EmailView.as_view()


class PasswordChangeView(TurboFormMixin, account_views.PasswordChangeView):
    ...


password_change = PasswordChangeView.as_view()


class PasswordSetView(TurboFormMixin, account_views.PasswordSetView):
    ...


password_set = PasswordSetView.as_view()


class PasswordResetView(TurboFormMixin, account_views.PasswordResetView):
    ...


password_reset = PasswordResetView.as_view()


class PasswordResetFromKeyView(TurboFormMixin, account_views.PasswordResetFromKeyView):
    ...


password_reset_from_key = PasswordResetFromKeyView.as_view()
