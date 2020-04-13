from django.test import TestCase
from ..models import Author, Book
from django.db.models import ObjectDoesNotExist

class AuthorTest(TestCase):
    """
    Tests Model of Author
    @since 2020-04-13
    @author eliasssv
    """
    def setUp(self):
        Author.objects.create(name='API TEST 1')
        Author.objects.create(name='API TEST 2')

    def test_get(self):
        author_1 = Author.objects.get(name='API TEST 1')
        author_2 = Author.objects.get(name='API TEST 2')
        self.assertEqual(author_1.name, "API TEST 1")
        self.assertEqual(author_2.name, "API TEST 2")

    def test_update(self):
        author_1 = Author.objects.get(name='API TEST 1')
        author_1.name = "API TEST 1 UPDATED"
        author_1.save()
        author_1 = Author.objects.get(name='API TEST 1 UPDATED')
        self.assertEqual(author_1.name, "API TEST 1 UPDATED")

    def test_delete(self):
        author_2 = Author.objects.get(name='API TEST 2')
        author_2.delete()
        with self.assertRaisesMessage(ObjectDoesNotExist,'Author matching query does not exist.'):
            Author.objects.get(name='API TEST 2')

"""class BookTest(TestCase):

    def setUp(self):
        author_1 = Author.objects.create(name='API TEST 1')
        author_2 = Author.objects.create(name='API TEST 2')
        Book.objects.create(
            name='API TEST 1',
            publication_year=2020,
            edition=1,
            authors=[author_1,author_2] 
        )
        Book.objects.create(
            name='API TEST 2',
            publication_year=1900,
            edition=2,
            authors=[author_2] 
        )

    def test_get(self):
        book_1 = Book.objects.get(name='API TEST 1')
        book_2 = Book.objects.get(name='API TEST 2')
        self.assertEqual(book_1.name, "API TEST 1")
        self.assertEqual(book_2.name, "API TEST 2")

    def test_update(self):
        book_1 = Book.objects.get(name='API TEST 1')
        book_1.name = "API TEST 1 UPDATED"
        book_1.save()
        book_1 = Author.objects.get(name='API TEST 1 UPDATED')
        self.assertEqual(book_1.name, "API TEST 1 UPDATED")

    def test_delete(self):
        book_2 = Book.objects.get(name='API TEST 2')
        book_2.delete()
        with self.assertRaisesMessage(self.model.DoesNotExist):
            Book.objects.get(name='API TEST 2')
            """