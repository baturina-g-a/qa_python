import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test:
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_book_added_just_once(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_if_genre_out_of_the_list_it_not_set(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение') == ''

    @pytest.mark.parametrize('name, genre', [
        ['Призрак дома на холме', 'Ужасы'], ['Дюна', 'Фантастика'], ['Трое в лодке, не считая собаки', 'Комедии']
    ])
    def test_get_book_genre_add_genre_for_book_true(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_books_with_the_horror_genre(self, collector, all_my_books):
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кэрри', 'Дьюма-Ки', 'Сияние']

    @pytest.mark.parametrize('name, genre', [
        ['День триффидов', 'Фантастика'], ['12 стульев', 'Комедии']
    ])
    def test_get_books_genre_get_existing_dictionary_books_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre == {name: genre}

    def test_get_books_for_children_get_list_without_books_with_genre_age_rating(self, collector, all_my_books):
        assert collector.get_books_for_children() == ['День триффидов', 'Кот в сапогах', '12 стульев']

    def test_add_book_in_favorites_books_really_did_add(self, collector, all_my_books):
        collector.add_book_in_favorites('День триффидов')
        collector.add_book_in_favorites('12 стульев')
        assert collector.favorites == ['День триффидов', '12 стульев']

    def test_add_book_in_favorites_book_do_not_add_if_book_do_not_in_dictionary(self, collector, all_my_books):
        collector.add_book_in_favorites('День триффидов')
        collector.add_book_in_favorites('Книжный вор')
        assert collector.favorites == ['День триффидов']

    def test_delete_book_from_favorites_books_really_did_delete(self, collector, my_favorite_books):
        collector.delete_book_from_favorites('10 негритят')
        assert '10 негритят' not in collector.favorites

    def test_get_list_of_favorites_books_get_existing_list_favorites(self, collector, my_favorite_books):
        assert collector.get_list_of_favorites_books() == my_favorite_books
