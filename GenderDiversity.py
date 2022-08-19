import pandas as pd
from scipy.stats import entropy


def read_data():
    df = pd.read_csv("Data/all_gender_api.csv", usecols=["first_name", "last_name", "api_gender"])
    return df


def get_number_of_male_female_count(df):
    df = df.groupby(['api_gender'])["api_gender"].count()
    female = df.get("female")
    male = df.get("male")
    unknown = df.get("unknown")
    return female, male, unknown


def get_gender_diversity_indicator(female, male):
    total = female + male
    m = male/total  # proportion of male
    f = female/total  # proportion of female
    print("Proportion of Male: " + str(m))
    print("Proportion of Female: " + str(f))
    cross_entropy_metric = entropy([m, f], base=2)
    print("Gender Diversity Indicator: " + str(cross_entropy_metric))
    return cross_entropy_metric


df = read_data()
female, male, unknown = get_number_of_male_female_count(df)
# ignore unknown genders
gender_diversity_indicator = get_gender_diversity_indicator(female, male)
