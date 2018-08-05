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
            msg = 'Имя : ' + feedback.name + '\n '
            msg += 'Телефон : ' + feedback.phone + '\n '
            msg += 'Сообщение : ' + feedback.text + '\n'
            msg += 'Дата : ' + feedback.created_date.strftime(" %d.%m.Y %I:%M%p")
            send_mail('Заявка', msg, settings.EMAIL_HOST_USER, ['gts5660gio@gmail.com'])
            feedback.save()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.all()
        return context
