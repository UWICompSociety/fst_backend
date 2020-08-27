from django.test import TestCase
from django.test import Client
from core.models import TestModel
from core.models import Event
# Create your tests here.



class  TestModelViewTest(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_get(self):
        # Create test models
        test_model1 = TestModel(first_name='John', last_name='Abbot')
        test_model1.save()
        test_model2 = TestModel(first_name='Jake', last_name='Randall')
        test_model2.save()
        
        #making a get request to test model endpoint
        response  = self.client.get('/testview/')

        #check status code
        self.assertEqual(response.status_code, 200)

        # get json data
        data = response.json()

        #check number of models returned
        self.assertEqual(len(data), 2)

        #check if api returns data stored
        expected_response = [{
                                'id': test_model1.id, 
                                'first_name': 'John', 
                                'last_name': 'Abbot'
                            }, 
                            {
                              'id': test_model2.id,
                              'first_name': 'Jake',
                              'last_name': 'Randall' 
                            }]
        self.assertEqual(data, expected_response)

class EventViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get(self):

        event1 = Event(name = 'General Orientation for New Undergraduate Students', start_date_time = '2020-08-28T09:00:00Z', end_date_time = '2020-08-28T15:00:00Z', location = 'Online', poster_image = 'assets/general_orientation_poster.JPG')
        event1.save()
        event2 = Event(name = 'FST Virtual Orientation', start_date_time = '2020-08-31T09:00:00Z', end_date_time = '2020-09-04T17:00:00Z', location = 'Online', poster_image = 'assets/fst_orientation_poster.JPG')
        event2.save()

        response = self.client.get('/events/')

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 2)

        expected_response = [{
                                'id': event1.id,
                                'name': 'General Orientation for New Undergraduate Students',
                                'start_date_time': '2020-08-28T09:00:00Z',
                                'end_date_time': '2020-08-28T15:00:00Z',
                                'location': 'Online',
                                'poster_image': 'assets/general_orientation_poster.JPG'
                            },
                            {
                                'id': event2.id,
                                'name': 'FST Virtual Orientation',
                                'start_date_time': '2020-08-31T09:00:00Z',
                                'end_date_time': '2020-09-04T17:00:00Z',
                                'location': 'Online',
                                'poster_image': 'assets/fst_orientation_poster.JPG'
                            }]

        self.assertEqual(data, expected_response)