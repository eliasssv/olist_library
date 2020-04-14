from django.test import TestCase
from library.models import Author, Book
from .model_tests_generic import generic_setUp, generic_get, generic_delete

class AuthorTest(TestCase):
    """
    Tests Model of Author
    \n@since 2020-04-13
    \n@author eliasssv
    """
    def setUp(self):
        generic_setUp([Author(name='API TEST 1'), Author(name='API TEST 2')])

    def test_get(self):
        generic_get(self, Author, [
            {
                "search_field": "name",
                "search_value": "API TEST 1",
                "compare_field": "name",
                "compare_value":  "API TEST 1",
            }
        ])

    def test_update(self):
        author_1 = Author.objects.get(name='API TEST 1')
        author_1.name = "API TEST 1 UPDATED"
        author_1.save()
        author_1 = Author.objects.get(name='API TEST 1 UPDATED')
        self.assertEqual(author_1.name, "API TEST 1 UPDATED")

    def test_delete(self):
        generic_delete(self, Author, [Author.objects.get(name='API TEST 2')])

class BookTest(TestCase):
    """
    Tests Model of Book
    \n@since 2020-04-13
    \n@author eliasssv
    """
    def setUp(self):
        author_1 = Author.objects.create(name='API TEST 1')
        author_2 = Author.objects.create(name='API TEST 2')
        book_1 = Book.objects.create(
            name='API TEST 1',
            publication_year=2020,
            edition=1
        )
        book_1.authors.set([author_1, author_2])

        book_2 = Book.objects.create(
            name='API TEST 2',
            publication_year=1900,
            edition=145
        )
        book_2.authors.set([author_2])

        generic_setUp([book_1, book_2])


    def test_get(self):
        book_1 = Book.objects.get(name='API TEST 1')
        book_2 = Book.objects.get(name='API TEST 2')
        self.assertEqual(book_1.name, "API TEST 1")
        self.assertEqual(book_2.name, "API TEST 2")

    def test_update(self):
        book_1 = Book.objects.get(name='API TEST 1')
        book_1.name = "API TEST 1 UPDATED"
        book_1.save()
        book_1 = Book.objects.get(name='API TEST 1 UPDATED')
        self.assertEqual(book_1.name, "API TEST 1 UPDATED")

    def test_delete(self):
        generic_delete(self, Book, [Book.objects.get(name='API TEST 2')])

    