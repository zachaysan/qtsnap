from fhp.helpers.json_finder import _parse_json, _dump_json
import os

# Rename this file to authentication.py

CONSUMER_KEY = "oXI2LhTKUdJnzThtxOLpt8XFSpRPhHU1yfrpmvNb"
CONSUMER_SECRET = "g4eE6Fq71PvcagiFwfRn7uyj8ch27SuMiWDRwU4Q"
VERIFY_URL = "http://qtsnap.com"

def root_dir():
    return os.path.join(os.path.dirname(__file__), "..")

def get_consumer_key():
    """ For more info on the API visit developer.500px.com.
    If you are logged in to your 500px account you can 
    go to: http://500px.com/settings/applications to retrieve
    your key.
    """
    return CONSUMER_KEY

def get_consumer_secret():
    """ For more info on the API visit developer.500px.com.
    If you are logged in to your 500px account you can 
    go to: http://500px.com/settings/applications to retrieve
    your key.
    """
    return CONSUMER_SECRET

def get_verify_url():
    """ Used for non-server applications """
    return VERIFY_URL
