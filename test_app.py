import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Book, Category


BASE = '/api/booksgallery/v1';
TOKEN_ADMIN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1Ra29JM192TGhjbDBqUEJqcTVzUiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MGp1bnotZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMzYTNmYTU1ZTk2YzViMmQxYTUwZWQwIiwiYXVkIjoiQm9va3NHYWxsZXJ5QVBJIiwiaWF0IjoxNjY0ODY3MDU0LCJleHAiOjE2NjQ4NzQyNTQsImF6cCI6ImNOWFdOY3F0cjJCY1JYQ2RTS2pNM290N0lFbXNGRHd2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Ym9va3MiLCJlZGl0OmJvb2tzIiwiZ2V0OmJvb2tzIiwiZ2V0OmJvb2tzQnlDYXRlZ29yeSIsImdldDpib29rc0J5U2VhcmNoVGVybSIsImdldDpjYXRlZ29yaWVzIiwicG9zdDpib29rcyJdfQ.XkVchtGBFU7hWIUC9W4-f8Zok7q6tauvJX-M5MnukDDGwg4nzinpXn4JyjojczPsWrBCJzMsEN4oRDQMIoG80qdKLGPFKlv5kCJnj2YZ5vCzubiJLkvhzBwCQtZ1JQT5T9LasCpv-bJqyueqscChS7RYaxinQL7UQh-Fcd-BOS6DtGEu1Fjo-_0lTA4tJmE-k9trDgUJRhboOvk8Zo8nxKmc6gdfDqrE_2TBf2uBx4ClP6N-i2MXPOKM9rmcMhR7_ZIVHKqUbN9IWt-xfxzak1mWD3tvX2flQUGu03aNRkRR9NbmVUwLQBZCxJQFWxBLllSqYEPGEcyHfG8r7aaGcA'
TOKEN_CLIENT = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1Ra29JM192TGhjbDBqUEJqcTVzUiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MGp1bnotZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMzYjM1ZmQ2Yzk5ZDgxNjA3NjQyYjJmIiwiYXVkIjoiQm9va3NHYWxsZXJ5QVBJIiwiaWF0IjoxNjY0ODY2ODUwLCJleHAiOjE2NjQ4NzQwNTAsImF6cCI6ImNOWFdOY3F0cjJCY1JYQ2RTS2pNM290N0lFbXNGRHd2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Ym9va3MiLCJnZXQ6Ym9va3NCeUNhdGVnb3J5IiwiZ2V0OmJvb2tzQnlTZWFyY2hUZXJtIiwiZ2V0OmNhdGVnb3JpZXMiXX0.yl5X6XqPcXTp3O8T8O7h-howd2M3ephOYT0YNSb8v59H0jaxEgrRDQb5a7fL6jdPxgOGOgoBzJkoNPR-jupjMYD7dM2KJI7bebUx_fQN7ukkpAB9fING9km6Vc9XCfD0GUbFHEnCgYLe1mAUpiTPeHXVSeT-dn3LrqrQ-e7cP3X2TyZiImatFvltIFxn1Htruag38BHL5ze-ozW2KrXAzHaLoehkV2AX_TSJMTJqjAl42AX6Nn_i7khcEiyBZKTt18Ws-V4HORZlKEmUrCQ4W7QHsgCWbBm_gRrPC5J7SWe74HxfA8ptrqjbEubuDtjXW4z3-RBQOxZjHmc4_sAKJQ'

class BooksGalleryTestCase(unittest.TestCase):

    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
        self.DB_USER = os.getenv('DB_USER', 'postgres')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
        self.DB_NAME = os.getenv('DB_NAME', 'trivia')
        self.DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME)
        setup_db(self.app, self.DB_PATH)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_all_categories(self):
            res = self.client().get(BASE+'/categories', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['categories'])
            self.assertEqual(len(data['categories']), 6)


    def test_get_all_books_paginated(self):
            res = self.client().get(BASE+'/books', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_CLIENT})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['books'])
            self.assertTrue(data['totalPerRequest'])
            self.assertTrue(data['total'])
            self.assertEqual(len(data['books']), 10)

    def test_get_books_with_invalid_page_number(self):
            res = self.client().get(BASE+'/books?page=240', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_CLIENT})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 500)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Internal server error')




    def test_post_new_book(self):
            self.book_data = {
                'category': '7',
                'title': 'Think And Grow Rich',
                'sub_title': 'The Landmark Bestseller Now Revised And Updated For The 21St Century',
                'author': 'Napoleon Hill',
                'publisher': 'Tarcherperigee',
                'pages': 320,
                'publish_date': '01-09-2005',
                'description': 'Think And Grow Rich Has Been Called The Granddaddy Of All Motivational Literature.'
            }
            res = self.client().post(BASE+'/books', json=self.book_data, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertIsNotNone(data['title'])

    def test_post_empty_books(self):
            self.book_empty = {
                'category': '1',
                'title': '',
                'sub_title': '',
                'author': '',
                'publisher': '',
                'pages': 250,
                'publish_date': '15-08-1996',
                'description': ''
            }
            res = self.client().post(BASE+'/books', json=self.book_empty, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Unprocessable')    

    def test_delete_book(self):
            res = self.client().delete(BASE+'/books/10', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(data['success'], True)

    def test_delete_invalid_book(self):
            res = self.client().delete(BASE+'/books/506', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Unprocessable')


    def test_find_books_by_category_id(self):
            res = self.client().get(BASE+'/categories/3/books', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_CLIENT})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['category_id'], 2)
            self.assertTrue(data['category_id'])
            self.assertTrue(data['total'])
            self.assertTrue(data['books'])

    def test_get_books_by_invalid_category_id(self):
            res = self.client().get('/categories/11/books', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)


    def test_search_books(self):
            data_json = {
                'searchTerm': 'The Way Of Kings'
            }
            res = self.client().post(BASE+'/books/search', json=data_json, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_CLIENT})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertIsNotNone(data['books'])


    def test_search_empty_books(self):
            res = self.client().post(BASE+'/books/search', json={'searchTerm': ''}, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)


    def test_search_invalid_data_books(self):
            res = self.client().post(BASE+'/books/search',
                                    json={'searchTerm': 'test121212'}, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)




    def test_patch_existing_book(self):
            data_json = {
                'title': 'Harry Potter and the Sorcerers Stone',
                'subtitle': 'Book 1',
                'description': 'Harry Potter has never been the star of a Quidditch team'
            }
            res = self.client().patch(BASE+'books/17', json=data_json, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertIsNotNone(data['books'])

    def test_patch_book_invalid_id(self):
            data_json = {
                'title': 'Why We Sleep',
                'subtitle': 'Unlocking The Power Of Sleep And Dreams',
                'description': 'Fascinating Book'
            }
            res = self.client().patch(BASE+'books/320', json=data_json, headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_ADMIN})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)



    def test_patch_existing_book_NA(self):
        ##No Authorization

        self.info = {
                'category': '1',
                'title': 'Jupiter',
                'sub_title': 'Test',
                'author': '',
                'publisher': '',
                'pages': 250,
                'publish_date': '15-08-1996',
                'description': 'Test'
            }
        res = self.client().post(BASE+'/books', json=self.info, headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_delete_book_NA(self):
        ##No Role assigned
            res = self.client().delete(BASE+'/books/10', headers = {'Content-Type': 'application/json', 'Authorization': TOKEN_CLIENT})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()