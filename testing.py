import pytest
import requests
import json

def main_url():
    return "https://reqres.in"

def test_valid_login(main_url):
    url = main_url + "/api/login/"
    data =  