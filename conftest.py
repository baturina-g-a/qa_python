import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def all_my_books(collector):
    collector.add_new_book('День триффидов')
    collector.add_new_book('Кэрри')
    collector.add_new_book('Дьюма-Ки')
    collector.add_new_book('Сияние')
    collector.add_new_book('10 негритят')
    collector.add_new_book('Кот в сапогах')
    collector.add_new_book('12 стульев')
    collector.set_book_genre('День триффидов', 'Фантастика')
    collector.set_book_genre('Кэрри', 'Ужасы')
    collector.set_book_genre('Дьюма-Ки', 'Ужасы')
    collector.set_book_genre('Сияние', 'Ужасы')
    collector.set_book_genre('10 негритят', 'Детективы')
    collector.set_book_genre('Кот в сапогах', 'Мультфильмы')
    collector.set_book_genre('12 стульев', 'Комедии')
    return all_my_books


@pytest.fixture
def my_favorite_books(collector, all_my_books):
    collector.add_book_in_favorites('День триффидов')
    collector.add_book_in_favorites('10 негритят')
    collector.add_book_in_favorites('12 стульев')
    return collector.favorites
