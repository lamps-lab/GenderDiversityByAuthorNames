import pandas as pd
from sklearn import metrics


def evaluate_wiki_gendersort():
    wg_df = pd.read_csv("Data/name_and_gender.csv")
    wg_df["gender"] = wg_df["gender"].map({"M": "m", "F": "f", "UNK": "u", "UNI": "UNI", "INI": "INI"})

    classified = wg_df["gender"].tolist()

    print("Wiki Gendersort Total Count")
    print(wg_df.groupby(["gender"])["gender"].count())

    raw_df = pd.read_csv('Data/raw_data/all.csv', usecols=["first_name", "gender"])
    raw_df = raw_df[raw_df["gender"] != "u"]

    print("Raw Data Total Count")
    print(raw_df.groupby(["gender"])["gender"].count())

    actual = raw_df["gender"].tolist()

    print(len(classified))
    print(len(actual))

    print(classified)
    print(actual)

    print(metrics.confusion_matrix(actual, classified, labels=["m", "f", "u", "UNI", "INI"]))


def evaluate_gender_api():
    ga_df = pd.read_csv("Data/all_gender_api.csv")
    ga_df = ga_df[ga_df["gender"] != "u"]
    ga_df["api_gender"] = ga_df["api_gender"].map({"male": "m", "female": "f", "unknown": "u"})

    classified = ga_df["api_gender"].tolist()

    print("Gender API Total Count")
    print(ga_df.groupby(["api_gender"])["api_gender"].count())

    raw_df = pd.read_csv('Data/raw_data/all.csv', usecols=["first_name", "gender"])
    raw_df = raw_df[raw_df["gender"] != "u"]

    print("Raw Data Total Count")
    print(raw_df.groupby(["gender"])["gender"].count())

    actual = raw_df["gender"].tolist()

    print(len(classified))
    print(len(actual))

    print(classified)
    print(actual)

    print(metrics.confusion_matrix(actual, classified, labels=["m", "f", "u"]))


# evaluate_wiki_gendersort()
# evaluate_gender_api()
