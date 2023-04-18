from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_books_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две книги
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_exact_book_is_added(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')

        assert 'Война и мир' in collector.get_books_rating()

    def test_add_new_book_add_one_book_twice_book_is_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('1984')

        collector.add_new_book('1984')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_one_non_existance_book_impossible_to_set_rating(self):
        collector = BooksCollector()

        collector.set_book_rating('Book', 5)

        assert 'Book' not in collector.get_books_rating()

    def test_set_book_rating_one_book_impossible_to_set_rating_less_than_min(self):
        collector = BooksCollector()

        collector.add_new_book('Улисс')
        collector.set_book_rating('Улисс', 0)

        assert collector.get_book_rating('Улисс') != 0

    def test_set_book_rating_one_book_impossible_to_set_rating_more_than_max(self):
        collector = BooksCollector()

        collector.add_new_book('Лолита')
        collector.set_book_rating('Лолита', 11)

        assert collector.get_book_rating('Лолита') != 11

    def test_set_book_rating_one_book_rating_is_set(self):
        collector = BooksCollector()

        collector.add_new_book('Над пропастью во ржи')
        collector.set_book_rating('Над пропастью во ржи', 10)

        assert collector.get_book_rating('Над пропастью во ржи') == 10

    def test_get_book_rating_one_book_no_rating_for_non_exist_book(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Book1') is None

    def test_add_book_in_favorites_one_book_added_to_favorite(self):
        collector = BooksCollector()

        collector.add_new_book('Человек-невидимка')

        collector.add_book_in_favorites('Человек-невидимка')

        assert 'Человек-невидимка' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_one_book_impossible_to_add_non_exist_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Илиада')

        assert 'Илиада' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_deleted_from_favorite(self):
        collector = BooksCollector()

        collector.add_new_book('Божественная комедия')
        collector.add_book_in_favorites('Божественная комедия')
        collector.delete_book_from_favorites('Божественная комедия')

        assert 'Божественная комедия' not in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_rating_three_books_two_books_in_spec_list(self):
        collector = BooksCollector()

        collector.add_new_book('Сто лет одиночества')
        collector.add_new_book('Великий Гэтсби')
        collector.add_new_book('Уловка-22')

        collector.set_book_rating('Сто лет одиночества', 9)
        collector.set_book_rating('Великий Гэтсби', 7)
        collector.set_book_rating('Уловка-22', 9)

        assert 'Сто лет одиночества' and 'Уловка-22' in collector.get_books_with_specific_rating(9)