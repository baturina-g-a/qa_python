import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, book):
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(book.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_book_added_just_once(self, book):
        book.add_new_book('Гордость и предубеждение')
        book.add_new_book('Гордость и предубеждение')
        assert len(book.get_books_genre()) == 1

    def test_set_book_genre_if_genre_out_of_the_list_it_not_set(self, book):
        book.add_new_book('Гордость и предубеждение')
        book.set_book_genre('Гордость и предубеждение', 'Роман')
        assert book.get_book_genre('Гордость и предубеждение') == ''

    @pytest.mark.parametrize('name, genre', [
        ['Призрак дома на холме', 'Ужасы'], ['Дюна', 'Фантастика'], ['Трое в лодке, не считая собаки', 'Комедии']
    ])
    def test_get_book_genre_add_genre_for_book_true(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_books_with_the_horror_genre(self, book, all_my_books):
        assert book.get_books_with_specific_genre('Ужасы') == ['Кэрри', 'Дьюма-Ки', 'Сияние']

    @pytest.mark.parametrize('name, genre', [
        ['День триффидов', 'Фантастика'], ['12 стульев', 'Комедии']
    ])
    def test_get_books_genre_get_existing_dictionary_books_genre(self, book, name, genre):
        book.add_new_book(name)
        book.set_book_genre(name, genre)
        assert book.books_genre == {name: genre}

    def test_get_books_for_children_get_list_without_books_with_genre_age_rating(self, book, all_my_books):
        assert book.get_books_for_children() == ['День триффидов', 'Кот в сапогах', '12 стульев']

    def test_add_book_in_favorites_books_really_did_add(self, book, all_my_books):
        book.add_book_in_favorites('День триффидов')
        book.add_book_in_favorites('12 стульев')
        assert book.favorites == ['День триффидов', '12 стульев']

    def test_add_book_in_favorites_book_do_not_add_if_book_do_not_in_dictionary(self, book, all_my_books):
        book.add_book_in_favorites('День триффидов')
        book.add_book_in_favorites('Книжный вор')
        assert book.favorites == ['День триффидов']

    def test_delete_book_from_favorites_books_really_did_delete(self, book, my_favorite_books):
        book.delete_book_from_favorites('10 негритят')
        assert '10 негритят' not in book.favorites

    def test_get_list_of_favorites_books_get_existing_list_favorites(self, book, my_favorite_books):
        assert book.get_list_of_favorites_books() == my_favorite_books
