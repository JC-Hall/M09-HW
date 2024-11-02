import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        test_user.add_book("One Piece", 5)
        self.assertIn("One Piece", test_user.book_list["book_name"].values)
    def test_2_add_book(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        test_user.add_book("One Piece", 5)
        test_user.add_book("One Piece", 5)
        self.assertEqual(test_user.book_list['book_name'].value_counts().get("One Piece", 0), 1)
    def test_3_has_read(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        test_user.add_book("One Piece", 5)
        self.assertTrue(test_user.has_read("One Piece"))
    def test_4_has_read(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        self.assertFalse(test_user.has_read("The Book"))
    def test_5_num_books_read(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        test_user.add_book("One Piece", 5)
        test_user.add_book("Solo Leveling", 4)
        self.assertEqual(test_user.num_books_read(), 2)
    def test_6_fav_books(self):
        test_user = BookLover("Josh", "jch7aa@virginia.edu", "manga")
        test_user.add_book("One Piece", 5)
        test_user.add_book("Solo Leveling", 4)
        test_user.add_book("Coding for Dummies", 1)
        fav_books = test_user.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)