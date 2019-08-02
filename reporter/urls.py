from django.conf.urls import url

from reporter.views import HomePageView, county_datasets, point_datasets

urlpatterns = [
	url('', HomePageView.as_view(), name='home'),
	url('county_data', county_datasets, name='county'),
	url('incidence_data', point_datasets, name='incidences'),
]