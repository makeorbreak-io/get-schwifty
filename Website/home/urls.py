from django.conf.urls import url
from home.views import HomeView, Train

urlpatterns = [
	url(r'^$', HomeView.as_view(), name = 'home'),
	url(r'^train', Train.as_view(), name = 'home')
]