import pytest
from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book


@pytest.fixture
def all_my_books(book):
    book.add_new_book('День триффидов')
    book.add_new_book('Кэрри')
    book.add_new_book('Дьюма-Ки')
    book.add_new_book('Сияние')
    book.add_new_book('10 негритят')
    book.add_new_book('Кот в сапогах')
    book.add_new_book('12 стульев')
    book.set_book_genre('День триффидов', 'Фантастика')
    book.set_book_genre('Кэрри', 'Ужасы')
    book.set_book_genre('Дьюма-Ки', 'Ужасы')
    book.set_book_genre('Сияние', 'Ужасы')
    book.set_book_genre('10 негритят', 'Детективы')
    book.set_book_genre('Кот в сапогах', 'Мультфильмы')
    book.set_book_genre('12 стульев', 'Комедии')
    return all_my_books


@pytest.fixture
def my_favorite_books(book, all_my_books):
    book.add_book_in_favorites('День триффидов')
    book.add_book_in_favorites('10 негритят')
    book.add_book_in_favorites('12 стульев')
    return book.favorites
