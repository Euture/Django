from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail

class FeedbackFormView(TemplateView, FormView):
    template_name = "main.html"
    form_class = FeedbackForm

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            feedback.save()
            #send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['gts5660gio@gmail.com'])
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.all()
        return context
