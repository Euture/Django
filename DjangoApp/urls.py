from django.conf.urls import url
from .views import FeedbackFormView
urlpatterns = [
    url(r'^', FeedbackFormView.as_view(success_url=r' '), name='FeedbackFormView'),
]
