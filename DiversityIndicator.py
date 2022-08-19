import pandas as pd
from scipy.stats import entropy


def read_data():
    df = pd.read_csv("data/output/author_names_and_genders.csv", usecols=["first_name", "last_name", "gender"])
    return df


def get_number_of_male_female_count(df):
    df = df.groupby(['gender'])["gender"].count()
    female = df.get("female")
    male = df.get("male")
    unknown = df.get("unknown")
    return female, male, unknown


def get_gender_diversity(female, male):
    total = female + male
    m = male/total  # proportion of male
    f = female/total  # proportion of female
    print("Proportion of Male: " + str(m))
    print("Proportion of Female: " + str(f))
    cross_entropy_metric = entropy([m, f], base=2)
    return cross_entropy_metric


def get_diversity_indicator():
    df = read_data()
    female, male, unknown = get_number_of_male_female_count(df)
    # ignore unknown genders
    gender_diversity_indicator = get_gender_diversity(female, male)
    return gender_diversity_indicator
