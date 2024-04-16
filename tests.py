import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '',
                                              'Что делать, если ваш кот хочет вас убить': ''}

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #добавляем книгу с названием в 41 символ
    #def test_add_new_book_name_41_symbols(self):
        #collector = BooksCollector()

       #collector.add_new_book('Удивительное путешествие Нильса Хольгерсс')
        #assert collector.get_books_genre() == {}

    #добавляем книгу без названия
    #def test_add_new_book_without_name(self):
        #collector = BooksCollector()

        #collector.add_new_book('')
        #assert collector.get_books_genre() == {}

    #добавляем уже добавленную книгу
    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}

    #не добавляются книги вне диапазона(название)
    @pytest.mark.parametrize('name', ['', 'Удивительное путешествие Нильса Хольгерсс'])
    def test_add_new_book(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        assert collector.get_books_genre() == {}
