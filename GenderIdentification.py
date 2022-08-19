import requests
import Constants
import pandas as pd

API_Key = Constants.API_Key


def validate_api_key():
    if API_Key == "API_KEY_CONSTANT" or None:
        print("[ERROR] Invalid API Key")
        print("        Please replace the `API_KEY_CONSTANT` in the `Constants.py` file with the API_Key obtained from"
              " Gender-API. \n"
              "        To get an API Key, go to https://gender-api.com/ and sign up.")


def read_input_data(input_file):
    df = pd.read_csv(input_file, usecols=["first_name", "last_name"])
    return df


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


def get_genders_for_name_gender_api(df):
    new_df = pd.DataFrame({"first_name": [], "last_name": [], "gender": []})
    for index, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        new_data = pd.DataFrame({
            "first_name": [first_name],
            "last_name": [last_name],
            "gender": [get_gender(first_name, last_name)]
        })
        new_df = pd.concat([new_df, new_data])

    new_df.to_csv("data/output/author_names_and_genders.csv", index=False)


def gender_identification(input_file):
    validate_api_key()
    df = read_input_data(input_file)
    get_genders_for_name_gender_api(df)
