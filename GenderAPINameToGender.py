import requests
import GenderAPIConstants

API_Key = Constants.API_Key


def get_gender(firstname, lastname):
    url = 'https://gender-api.com/get?split=' + firstname + '%20' + lastname + '&key=' + API_Key
    r = requests.get(url)
    response = r.json()
    gender = response["gender"]
    return gender
