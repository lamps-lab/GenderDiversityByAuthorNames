# I think we can use a diversity indicator, which looks like the cross entropy metric.
#
# H=-(p x logp + (1-p)log(1-p))
#
# The log base is 2.
#
# The idea is that when p=0 or 1, H=0, meaning that there is no diversity.
# When p=0.5, H=1, when the diversity reaches the max.
#
# p is the proportion of male authors of a paper.

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
