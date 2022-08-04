import pandas as pd
import GenderAPINameToGender


def read_data():
    df = pd.read_csv("Data/names.csv", usecols=["first_name", "last_name"])
    return df


def get_genders_for_name(df):
    new_df = pd.DataFrame({"first_name": [], "last_name": [], "api_gender": []})
    for index, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        new_data = pd.DataFrame({
            "first_name": [first_name],
            "last_name": [last_name],
            "api_gender": [GenderAPINameToGender.get_gender(first_name, last_name)]
        })
        new_df = pd.concat([new_df, new_data])

    new_df.to_csv("./Data/names_and_genders.csv")


df = read_data()
get_genders_for_name(df)

