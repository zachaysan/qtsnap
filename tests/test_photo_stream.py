import unittest
import os
from fhp.models.photo_stream import PhotoStream
from fhp.helpers.json_finder import _parse_json
from tests.settings import test_settings

class Test_photo_stream(unittest.TestCase):
    """ This tests the photo_stream class. """
    
    def setUp(self):
        self.test_settings = test_settings
        self.popular_photos = PhotoStream()
    
    def test_init(self):
        self.assertTrue(self.popular_photos.first().name)
        
    def test_photo_is_actually_popular(self):
        self.assertTrue(self.popular_photos.first().rating > 99.0)
