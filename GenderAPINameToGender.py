import requests
import GenderAPIConstants
import pandas as pd

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


def read_data():
    df = pd.read_csv("Data/all_gender_api.csv", usecols=["first_name", "last_name"])
    return df


def get_genders_for_name_gender_api(df):
    new_df = pd.DataFrame({"first_name": [], "last_name": [], "api_gender": []})
    for index, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        new_data = pd.DataFrame({
            "first_name": [first_name],
            "last_name": [last_name],
            "api_gender": [get_gender(first_name, last_name)]
        })
        new_df = pd.concat([new_df, new_data])

    new_df.to_csv("./Data/names_and_genders_gender_api.csv")


if __name__ == "__main__":
    df = read_data()
    get_genders_for_name_gender_api(df)
