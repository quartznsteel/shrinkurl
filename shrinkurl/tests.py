from django.test import TestCase
from django.test import Client
from shrinkurl.models import URLPair

class TestApiEndPoint(TestCase):

    #test_database_insert_delete
    #this will test that data can be saved and deleted
    def test_database_insert_delete(self):
        newURLPair = URLPair(short_url="abc123", long_url="https://www.hotels.com/Hotel-Search?destination=United%20States%20of%20America&regionId=201&latLong=37.090241%2C-95.712891&rooms=1&adults=2&startDate=2024-11-14&d1=2024-11-14&endDate=2024-11-16&d2=2024-11-16&lodging=CABIN&sort=RECOMMENDED&useRewards=false&semdtl=&userIntent=&theme=")
        newURLPair.save()

        URLPair2 = URLPair.objects.get(pk = newURLPair.pk)
        self.assertTrue(newURLPair == URLPair2)

        URLPair.objects.filter(pk=newURLPair.pk).delete()
        self.assertFalse(URLPair.objects.filter(pk=newURLPair.pk).exists())

    #test_returns_response
    #this will test that get and post requests return proper data
    def test_returns_response(self):
        client = Client()
        url = "/api/"
        longdata = {"longurl": "https://www.hotels.com/Hotel-Search?destination=United%20States%20of%20America&regionId=201&latLong=37.090241%2C-95.712891&rooms=1&adults=2&startDate=2024-11-14&d1=2024-11-14&endDate=2024-11-16&d2=2024-11-16&lodging=CABIN&sort=RECOMMENDED&useRewards=false&semdtl=&userIntent=&theme="}

        #Test POST request
        postresponse = client.post(url, longdata)
        self.assertEqual(postresponse.status_code, 200)
        self.assertEqual(len(postresponse.content), 6)

        #Test GET request
        newshorturl = postresponse.content.decode('UTF-8')
        shortdata = {'shorturl': newshorturl}
        getresponse = client.get(url, shortdata)
        self.assertEqual(postresponse.status_code, 200)
        self.assertTrue(len(getresponse.content) > 6)