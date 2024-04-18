import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # поверка на добавление нескольких книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '',
                                              'Что делать, если ваш кот хочет вас убить': ''}

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #добавляем уже добавленную книгу
    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}

    #не добавляются книги вне диапазона(название)
    @pytest.mark.parametrize('name', ['',
                                      'Удивительное путешествие Нильса Хольгерсс',
                                      'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0

    #добавляются книги из дипазона(название)
    @pytest.mark.parametrize('name', ['К югу от границы',
                                      'Любовь как роза, красива, но шипы больны',
                                      'Я'])
    def test_add_new_book_name_in_the_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert name in books_collection.get_books_genre()

    #устанавливаем жанр книге
    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение': 'Фантастика'}

    #проверяем, что нельзя установить жанр книге, которой нет в books_genre
    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()

        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}

    #проверяем, что нельзя добавить жанр вне списка книге из books_genre
    def test_set_book_genre_to_not_existing_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Трагикомедии')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    #вывод жанра книги по имени
    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    #вывод книг по жанру
    def test_get_books_with_specific_genre_by_genre(self, my_books_collection):
        assert my_books_collection.get_books_with_specific_genre('Мультфильмы') == ['Гадкий Я']

    #вывод книг по несуществующему жанру
    def test_get_books_with_specific_genre_by_wrong_genre(self, my_books_collection):
        assert len(my_books_collection.get_books_with_specific_genre('Трагикомедии')) == 0

    #вывод дестких книг
    def test_get_books_for_children(self, my_books_collection):
        assert len(my_books_collection.get_books_for_children()) == 3 and my_books_collection.get_books_for_children() == ['Симбиоз', 'Гадкий Я', 'Ревизор']

    #добавить в избранное
    def test_add_book_in_favorites_not_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')

        assert 'Симбиоз' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1

    #добавить в избранное одну и ту же книгу
    def test_add_book_in_favorites_added_in_favorites_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.add_book_in_favorites('Симбиоз')

        assert 'Симбиоз' in my_books_collection.get_list_of_favorites_books() and len(my_books_collection.get_list_of_favorites_books()) == 1

    #добавить в избранное книгу не из books_genre
    def test_add_book_in_favorites_not_added_dict_book(self, my_books_collection):
        book = 'Идиот'
        my_books_collection.add_book_in_favorites(book)

        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    #удалить из избранного
    def test_delete_book_from_favorites(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Симбиоз')

        assert len(my_books_collection.get_list_of_favorites_books()) == 0

    # удалить из избранного книгу не из избранного
    def test_delete_book_from_favorites_deleted_book(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.delete_book_from_favorites('Симбиоз')

        assert len(my_books_collection.get_list_of_favorites_books()) == 0 and 'Симбиоз' not in my_books_collection.get_list_of_favorites_books()

    #получить список избранных книг
    def test_get_list_of_favorites_books(self, my_books_collection):
        my_books_collection.add_book_in_favorites('Симбиоз')
        my_books_collection.add_book_in_favorites('Гадкий Я')

        assert my_books_collection.get_list_of_favorites_books() == ['Симбиоз', 'Гадкий Я']