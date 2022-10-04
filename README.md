# Full Stack Nanodegree Capstone Project

## Background

This project showcases many of the skills I've learned through the Udacity Full Stack Nanodgree curriculum. This entire api has been built from the ground up with no starter code. 

## Getting Started

This code is currently deployed on Heroku and accessible at the following URL.

    https://books-gallery-by-basshayr.herokuapp.com/

    
## Local Quick Start

###Prepare your environment and app

Start Postgresql

* install postgres if needed
* create a database (createdb booksByBashayr)
* save the database, username, and password someplace handy

####Clone the repository
```bash
https://github.com/BashayerGH/capstone
```


## Running the server
To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file as the application. 

### Roles and Permissions

There are two roles with different permissions setup for this api:

Client

- Can view books and categories, and search for a book

Client Authentication Token
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1Ra29JM192TGhjbDBqUEJqcTVzUiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MGp1bnotZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMzYjM1ZmQ2Yzk5ZDgxNjA3NjQyYjJmIiwiYXVkIjoiQm9va3NHYWxsZXJ5QVBJIiwiaWF0IjoxNjY0ODI0OTczLCJleHAiOjE2NjQ4MzIxNzMsImF6cCI6ImNOWFdOY3F0cjJCY1JYQ2RTS2pNM290N0lFbXNGRHd2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Ym9va3MiLCJnZXQ6Ym9va3NCeUNhdGVnb3J5IiwiZ2V0OmJvb2tzQnlTZWFyY2hUZXJtIiwiZ2V0OmNhdGVnb3JpZXMiXX0.tLSolulXU7weeB2RJLT5kI5n2W6Dt1ebIWLbdjy40bm15AeIz_CICknWcKXr9yvdCB19hfROXF11tv3OTiJd4iGnU-Bh051MQ-JVYGMo5qx8G6jG3ou2dBPFSP4vV725AF-qXmykrOxty2zd0_lBDpJfR0HVfsPsWeEHDzzrDzEE6-liP2QMZ6YQhsC0j0ghd9wJiMPxyPmNRw2KHbpSAHKgMZxs6iFP2vKOxaiXRnREpXYVSWTuIGfCX83XBlRDqd35shQM-c8KW0IcohDSVZA8pNo0mB3OEPWTttCBpiTwYpPLeUwFmZPqv-yVALus1br7A5Roaj1ZWdy0gc-ADg
```

Admin

- All permissions a client has and...
- Add, edit and delete a book from the database

Admin Authentication Token
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii1Ra29JM192TGhjbDBqUEJqcTVzUiJ9.eyJpc3MiOiJodHRwczovL2Rldi04MGp1bnotZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjMzYTNmYTU1ZTk2YzViMmQxYTUwZWQwIiwiYXVkIjoiQm9va3NHYWxsZXJ5QVBJIiwiaWF0IjoxNjY0ODUzNzYwLCJleHAiOjE2NjQ4NjA5NjAsImF6cCI6ImNOWFdOY3F0cjJCY1JYQ2RTS2pNM290N0lFbXNGRHd2Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Ym9va3MiLCJlZGl0OmJvb2tzIiwiZ2V0OmJvb2tzIiwiZ2V0OmJvb2tzQnlDYXRlZ29yeSIsImdldDpib29rc0J5U2VhcmNoVGVybSIsImdldDpjYXRlZ29yaWVzIiwicG9zdDpib29rcyJdfQ.eFQJDxl33XsgIx_TQm2KQbolWOGV9WHRiShKUunmTlYYk8ynUxcJDxBgwZmNab5lmx7THpwYaBfekttGdYI89lCu_Y2wNIhxhBVOhECjwU9-9-E1_dSJgW0IoMKOCyTc7z6TcMspXIL3-cxbXMudH72JmTpO7OkQPdCQCFHY9pYnxKncbNTJqZGNrr5sanpwPu-vBeqAysISqUk1YAjE0JYmrAVlIMvaPD5FB-9_-aIkevm4HV0iIFMR1tu2napaHhoJ5g2qafRN_Tz6bcXOHVVO-l8PetNMCrwLu381kLzqB08HwWCgCC3n6b8cEneWkrmrfrTvK0zAvfypgzsC6g
```

## Resource endpoint library

Endpoints

- GET '/books'
- GET '/categories'
- POST '/books'
- DELETE '/books/<int:id>'
- GET '/categories/<int:category>/books'
- POST '/books/search'
- PATCH '/books/<int:book_id>'



GET '/books' 

- Fetches an list of books
- Returns:
    - books
    - Success value
    - The returning books in the request
    - The total books in the database

```bash
{
    "books": [
        {
            "author": "Simon Singh Dr",
            "category": 1,
            "description": "Throughout the text are clear technical and mathematical explanations, and portraits of the remarkable personalities who wrote and broke the world's most difficult codes. Accessible, compelling, and remarkably far-reaching, this book will forever alter your view of history and what drives it. It will also make you wonder how private that e-mail you just sent really is.",
            "id": 5,
            "pages": 432,
            "publish_date": "29-08-2000",
            "publisher": "Anchor Books",
            "sub_title": "The Science of Secrecy from Ancient Egypt to Quantum Cryptography",
            "title": "The Code Book"
        },
        {
            "author": "Natalie Walton",
            "category": 2,
            "description": "This Is Home Is About Simple Living - How To Focus On Our Values To Create Authentic Homes Full Of Meaning And Joy. Natalie Walton Steps Inside Fifteen Homes Across The World To Meet The People Who Made Them, And Discover Whether There Is Some Universality To What Makes Us Happy In The Spaces We Inhabit. Filled With Beautiful Photography, Transporting Stories And Practical Advice, This Is Home Reminds And Inspires Us To Nurture The Space That Helps Make Our Lives Possible.",
            "id": 8,
            "pages": 240,
            "publish_date": "01-04-2018",
            "publisher": "Hardie Grant Books",
            "sub_title": "The Art Of Simple Living",
            "title": "This Is Home"
        },
        {
            "author": "Lorna Scobie",
            "category": 2,
            "description": "365 Days Of Art Is An Inspiring Journal Designed To Help Readers And Budding Artists Nurture Their Creativity And Explore Their Feelings Through The Medium Of Art. Featuring An Activity For Every Day Of The Year, From Simple Tasks Like Drawing Shapes And Lines, To More Mindful Exercises Like Coloring-In, Painting With Primary Colors, And Drawing What You See. With Beautiful, Vibrant Hand-Lettering And Watercolor Illustrations, The Book Pairs Inspiring Quotes With Supportive Prompts And Exercises To Spark Reflection Through Your Drawing, Writing, Painting And More.",
            "id": 9,
            "pages": 352,
            "publish_date": "19-10-2017",
            "publisher": "Hardie Grant Books",
            "sub_title": "A Creative Exercise For Every Day Of The Year",
            "title": "365 Days Of Art"
        },
        {
            "author": "Dorling Kindersley",
            "category": 2,
            "description": "The entire history of the greatest works in painting, sculpture, and photography are included on this comprehensive and colourful tour through time.",
            "id": 10,
            "pages": 304,
            "publish_date": "01-08-2017",
            "publisher": "DK Publishing",
            "sub_title": "A Visual Encyclopedia",
            "title": "The Arts"
        }

    ],
    "success": true,
    "total": 21,
    "totalPerRequest": 10
}
```

GET '/categories' 

- Fetches an list of categories
- Returns:
    - categories
    - Success value

```bash
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Cooking",
        "4": "History",
        "5": "Fantasy",
        "6": "Childrens",
        "7": "self help"
    },
    "success": true
}
```


GET '/categories/<int:category>/books'

- Fetches an list of categories
- Returns:
    - books
    - Success value
    - category id
    - The total books in the database for the category

```bash
{
    "books": [
        {
            "author": "Natalie Walton",
            "category": 2,
            "description": "This Is Home Is About Simple Living - How To Focus On Our Values To Create Authentic Homes Full Of Meaning And Joy. Natalie Walton Steps Inside Fifteen Homes Across The World To Meet The People Who Made Them, And Discover Whether There Is Some Universality To What Makes Us Happy In The Spaces We Inhabit. Filled With Beautiful Photography, Transporting Stories And Practical Advice, This Is Home Reminds And Inspires Us To Nurture The Space That Helps Make Our Lives Possible.",
            "id": 8,
            "pages": 240,
            "publish_date": "01-04-2018",
            "publisher": "Hardie Grant Books",
            "sub_title": "The Art Of Simple Living",
            "title": "This Is Home"
        },
        {
            "author": "Lorna Scobie",
            "category": 2,
            "description": "365 Days Of Art Is An Inspiring Journal Designed To Help Readers And Budding Artists Nurture Their Creativity And Explore Their Feelings Through The Medium Of Art. Featuring An Activity For Every Day Of The Year, From Simple Tasks Like Drawing Shapes And Lines, To More Mindful Exercises Like Coloring-In, Painting With Primary Colors, And Drawing What You See. With Beautiful, Vibrant Hand-Lettering And Watercolor Illustrations, The Book Pairs Inspiring Quotes With Supportive Prompts And Exercises To Spark Reflection Through Your Drawing, Writing, Painting And More.",
            "id": 9,
            "pages": 352,
            "publish_date": "19-10-2017",
            "publisher": "Hardie Grant Books",
            "sub_title": "A Creative Exercise For Every Day Of The Year",
            "title": "365 Days Of Art"
        },
        {
            "author": "Dorling Kindersley",
            "category": 2,
            "description": "The entire history of the greatest works in painting, sculpture, and photography are included on this comprehensive and colourful tour through time.",
            "id": 10,
            "pages": 304,
            "publish_date": "01-08-2017",
            "publisher": "DK Publishing",
            "sub_title": "A Visual Encyclopedia",
            "title": "The Arts"
        }
    ],
    "category_id": 2,
    "success": true,
    "total": 5
}
```


POST '/books'

- Creates a new book
- Returns:
    - Success value
    - The book
    - Category id
    - The description of the book

```bash
{
    "book": "The power of now",
    "category": 1,
    "description": "A Guide to Spiritual Enlightenment is a book by Eckhart Tolle",
    "success": true
}
```


POST '/books/search'

- Search for a book by `searchTerm` in the database
- Returns:
    - Success value
    - The books that its title matches the searchTerm
    - Category id
    - The total number of results


```bash
{
    "books": [
        {
            "author": "Simon Singh Dr",
            "category": 1,
            "description": "Throughout the text are clear technical and mathematical explanations, and portraits of the remarkable personalities who wrote and broke the world's most difficult codes. Accessible, compelling, and remarkably far-reaching, this book will forever alter your view of history and what drives it. It will also make you wonder how private that e-mail you just sent really is.",
            "id": 5,
            "pages": 432,
            "publish_date": "29-08-2000",
            "publisher": "Anchor Books",
            "sub_title": "The Science of Secrecy from Ancient Egypt to Quantum Cryptography",
            "title": "The Code Book"
        }
    ],
    "category_id": 1,
    "success": true,
    "total": 1
}
```

DELETE '/books/<int:id>'

- Deletes a book with a given id
- Returns:
    - Success value

```bash
{
    "success": true
}
```



PATCH '/books/<int:book_id>'

- Updates a movie with a given id and any included values
- Returns:
    - Success value
    - Updated data for that book

```bash
{
    "book": {
        "author": "Natalie Walton",
        "category": 2,
        "description": "This Is Home Is About Simple Living - How To Focus On Our Values To Create Authentic Homes Full Of Meaning And Joy. Natalie Walton Steps Inside Fifteen Homes Across The World To Meet The People Who Made Them, And Discover Whether There Is Some Universality To What Makes Us Happy In The Spaces We Inhabit. Filled With Beautiful Photography, Transporting Stories And Practical Advice, This Is Home Reminds And Inspires Us To Nurture The Space That Helps Make Our Lives Possible.",
        "id": 8,
        "pages": 240,
        "publish_date": "01-04-2018",
        "publisher": "Hardie Grant Books",
        "sub_title": "The Art Of Simple Living",
        "title": "This Is Home"
    },
    "success": true
}x
```


### Errors Handled

Errors that will be handled are:

- 422 - Unprocessable
- 404 - Resource not found
- 401 - Unauthorized
- 500 - Internal server error

Errors will include a success value, message, and error value.

Example error response
```bash
{
    "error": 404,
    "message": "Resource not found",
    "success": False
}

```