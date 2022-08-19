import requests
import GenderAPIConstants

API_Key = GenderAPIConstants.API_Key


def get_gender(firstname, lastname):
    url = 'https://gender-api.com/get?split=' + firstname + '%20' + lastname + '&key=' + API_Key
    r = requests.get(url)
    if r.status_code == 200:
        response = r.json()
        gender = response["gender"]
        return gender
    else:
        print("[ERROR] Error in gender-api.com GET API request")
        print("[ERROR] Status Code " + str(r.status_code))
        exit(0)
