from django.contrib.auth import views as contrib_auth_views
from django.urls import path, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']


class PlaceHolderMixin:

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field_name in form.fields:
            form.fields[field_name].widget.attrs['placeholder'] = (form.fields[field_name].label or '').lower()
            form.fields[field_name].label = False
        return form


class LoginView(PlaceHolderMixin, contrib_auth_views.LoginView):
    extra_context = {'submit_button_text': 'Start'}


class LogoutView(PlaceHolderMixin, contrib_auth_views.LogoutView):
    extra_context = {'submit_button_text': 'Logout'}


class SignUpView(PlaceHolderMixin, SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
    extra_context = {'submit_button_text': 'Join The Team'}


class PasswordResetView(PlaceHolderMixin, contrib_auth_views.PasswordResetView):
    extra_context = {'submit_button_text': 'Send Me The Link'}


class PasswordResetDoneView(PlaceHolderMixin, contrib_auth_views.PasswordResetDoneView):
    extra_context = {'submit_button_text': 'Back To Login!'}


class PasswordResetConfirmView(PlaceHolderMixin, contrib_auth_views.PasswordResetConfirmView):
    extra_context = {'submit_button_text': 'Verify!'}


class PasswordResetCompleteView(PlaceHolderMixin, contrib_auth_views.PasswordResetCompleteView):
    extra_context = {'submit_button_text': 'Back To Login!'}


urlpatterns = [
    path("login.html", LoginView.as_view(), name="login"),
    path("registeration.html", SignUpView.as_view(), name="registeration"),
    path("logout.html", LogoutView.as_view(), name="logout"),
    path("password_change.html", contrib_auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done.html", contrib_auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done", ),
    path("password_reset.html", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done.html", PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(),
         name="password_reset_confirm", ),
    path("reset/done.html", PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
]
