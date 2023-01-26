from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<slug:slug >/", views.MovieDetailViews.as_view())
]