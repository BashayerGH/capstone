import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Question, Category


BASE = '/api/booksgallery/v1';
class TriviaTestCase(unittest.TestCase):

    # TODO: Refactor the below end points
    # TODO: Includes tests demonstrating role-based access control, at least two per role.

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
            res = self.client().get(BASE+'/categories')
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['categories'])
            self.assertEqual(len(data['categories']), 6)


    def test_get_all_books_paginated(self):
            res = self.client().get(BASE+'/books')
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertTrue(data['books'])
            self.assertTrue(data['totalPerRequest'])
            self.assertTrue(data['total'])
            self.assertEqual(len(data['books']), 10)

    def test_get_books_with_invalid_page_number(self):
            res = self.client().get(BASE+'/books?page=240')
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Unprocessable')



        # TODO: insert a valid data
    def test_post_new_book(self):
            res = self.client().post(BASE+'/books', json={
                'category': '1',
                'title': 'Jupiter',
                'sub_title': '',
                'author': '',
                'publisher': '',
                'pages': 250,
                'publish_date': '15-08-1996',
                'description': ''
            })
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertIsNotNone(data['title'])

        # TODO: insert the rest data
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
            res = self.client().post(BASE+'/books', json=self.book_empty)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Unprocessable')    

    def test_delete_book(self):
            res = self.client().delete(BASE+'/books/15')
            data = json.loads(res.data)
            self.assertEqual(data['success'], True)

    def test_delete_invalid_book(self):
            res = self.client().delete(BASE+'/books/506')
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], 'Unprocessable')


    def test_find_books_by_category_id(self):
            res = self.client().get(BASE+'/categories/{}/books'.format(2))
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['category_id'], 2)
            self.assertTrue(data['category_id'])
            self.assertTrue(data['total'])
            self.assertTrue(data['books'])

    def test_get_questions_by_invalid_category_id(self):
            res = self.client().get('/categories/{}/books'.format(11))
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)


    def test_search_books(self):
            data_json = {
                'searchTerm': 'Why We Sleep'
            }
            res = self.client().post(BASE+'/books/search', json=data_json)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertIsNotNone(data['books'])


    def test_search_empty_books(self):
            res = self.client().post(BASE+'/books/search', json={'searchTerm': ''})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)


    def test_search_invalid_data_questions(self):
            res = self.client().post(BASE+'/books/search',
                                    json={'searchTerm': 'test121212'})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 422)
            self.assertEqual(data['success'], False)



    # TODO: Use a valid data
    def test_patch_existing_book(self):
            data_json = {
                'title': 'Why We Sleep',
                'subtitle': 'subtitle',
                'description': 'description'
            }
            res = self.client().patch(BASE+'books/9', json=data_json)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertIsNotNone(data['books'])

    # TODO: Use a valid data
    def test_patch_book_invalid_id(self):
            data_json = {
                'title': 'Why We Sleep',
                'subtitle': 'subtitle',
                'description': 'description'
            }
            res = self.client().patch(BASE+'books/320', json=data_json)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 404)
            self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()