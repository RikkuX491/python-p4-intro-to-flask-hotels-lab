import io
import sys

from app import app, hotels

class TestApp:

    '''Flask application in app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert(response.status_code == 200)

    def test_index_text_with_three_hotels(self):
        '''displays "Welcome to the Hotels website! We have 3 hotels available" in h1 in browser when there are 3 dictionaries with hotel information in the hotels list.'''
        hotels.clear()
        hotels.append({
            "id": 1,
            "name": "Wyndham Hotel"
        })
        hotels.append({
            "id": 2,
            "name": "The Chanler at Cliff Walk"
        })
        hotels.append({
            "id": 3,
            "name": "Waikiki Resort"
        })
        response = app.test_client().get('/')
        assert(response.data.decode() == f'<h1>Welcome to the Hotels website! We have 3 hotels available</h1>')

    def test_index_text_with_four_hotels(self):
        '''displays "Welcome to the Hotels website! We have 4 hotels available" in h1 in browser when there are 4 dictionaries with hotel information in the hotels list.'''
        hotels.clear()
        hotels.append({
            "id": 1,
            "name": "Wyndham Hotel"
        })
        hotels.append({
            "id": 2,
            "name": "The Chanler at Cliff Walk"
        })
        hotels.append({
            "id": 3,
            "name": "Waikiki Resort"
        })
        hotels.append({
            "id": 4,
            "name": "Bahamas Resort"
        })
        response = app.test_client().get('/')
        assert(response.data.decode() == f'<h1>Welcome to the Hotels website! We have 4 hotels available</h1>')

    def test_all_hotels_route(self):
        '''has a resource available at "/hotels".'''
        response = app.test_client().get('/hotels')
        assert(response.status_code == 200)

    def test_all_hotels_text(self):
        '''displays text of route in browser.'''
        hotels.clear()
        hotels.append({
            "id": 7,
            "name": "Wyndham Hotel"
        })
        hotels.append({
            "id": 14,
            "name": "The Chanler at Cliff Walk"
        })
        hotels.append({
            "id": 21,
            "name": "Waikiki Resort"
        })
        response = app.test_client().get('/hotels')
        hotels_string = ""
        hotels_string += "<li>Hotel # 7: Wyndham Hotel</li>"
        hotels_string += "<li>Hotel # 14: The Chanler at Cliff Walk</li>"
        hotels_string += "<li>Hotel # 21: Waikiki Resort</li>"
        assert(response.data.decode() == f"<ul>{hotels_string}</ul>")

    def test_hotel_by_id_route(self):
        '''has a resource available at "/hotels/<id>".'''
        response = app.test_client().get('/hotels/1')
        assert(response.status_code == 200)

    def test_hotel_by_id_text_for_first_hotel(self):
        '''displays text of route in browser for hotel with id of 1'''
        hotels.clear()
        hotels.append({
            "id": 1,
            "name": "Wyndham Hotel"
        })
        response = app.test_client().get('/hotels/1')
        assert(response.data.decode() == "<h1>Hotel # 1: Wyndham Hotel</h1>")

    def test_hotel_by_id_text_for_second_hotel(self):
        '''displays text of route in browser for hotel with id of 2'''
        hotels.clear()
        hotels.append({
            "id": 2,
            "name": "The Chanler at Cliff Walk"
        })
        response = app.test_client().get('/hotels/2')
        assert(response.data.decode() == "<h1>Hotel # 2: The Chanler at Cliff Walk</h1>")

    def test_hotel_by_id_text_for_hotel_not_found(self):
        '''displays text of route in browser when hotel not found'''
        hotels.clear()
        hotels.append({
            "id": 1,
            "name": "Wyndham Hotel"
        })
        hotels.append({
            "id": 2,
            "name": "The Chanler at Cliff Walk"
        })
        hotels.append({
            "id": 3,
            "name": "Waikiki Resort"
        })
        response = app.test_client().get('/hotels/4')
        assert(response.data.decode() == "<h1>Error: Hotel Not Found!</h1>")