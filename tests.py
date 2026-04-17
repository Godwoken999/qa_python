import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_adds_book_to_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')

        assert 'Дюна' in collector.get_books_genre()

    def test_add_new_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')

        assert collector.get_book_genre('Дюна') == ''

    def test_set_book_genre_sets_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_book_genre_returns_genre_of_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_books_with_this_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Шрек')
        collector.add_new_book('Оно')

        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Шрек']

    def test_get_books_genre_returns_current_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Шрек')

        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        expected_result = {
            'Дюна': 'Фантастика',
            'Шрек': 'Мультфильмы'
        }

        assert collector.get_books_genre() == expected_result

    def test_get_books_for_children_returns_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Шрек')
        collector.add_new_book('Оно')

        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == ['Дюна', 'Шрек']

    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_get_list_of_favorites_books_returns_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_deletes_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('name', ['', 'а' * 41])
    def test_add_new_book_with_invalid_name_does_not_add_book(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_set_book_genre_does_not_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.set_book_genre('Дюна', 'Роман')

        assert collector.get_book_genre('Дюна') == ''

    def test_add_book_in_favorites_adds_book_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']
