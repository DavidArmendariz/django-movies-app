import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Test Movie", genre="Test Genre", year="1980")
    movie.save()
    assert movie.title == "Test Movie"
    assert movie.genre == "Test Genre"
    assert movie.year == "1980"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title