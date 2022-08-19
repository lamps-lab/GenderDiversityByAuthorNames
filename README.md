# GenderDiversityByAuthorNames
This repository contains all the libraries used for getting a diversity indicator based on the gender of authors which are identified using their names. 

This module contains two parts,
1. Identifying the gender of the authors by using their names (first name and last name)
2. Getting a diversity indicator using the identified genders.

## Gender Identification

The gender identification is based on a name-to-gender inference service called Gender API. 

## Diversity Indicator

We will calculate a diversity indicator based on genders of the authors using the cross entropy metric.

**Cross Entropy Metric** 

_H=-(p x log p + (1-p)log(1-p))_

* _The log base is 2._
* _When p=0 or 1, H=0, meaning that there is no diversity. When p=0.5, H=1, when the diversity reaches the max._
* _p is the proportion of male authors of a paper._

## Instructions

### Setup
* **Python Version: 3.9**

### Subscribe to Gender API
1. Sign up for Gender-API at https://gender-api.com/ and get an API_Key.


2. Subscribe for relevant package based on the requirements. Check the price at https://gender-api.com/en/pricing
* Note: Free subscription only contains 500 credits (only 500 names per month)


### Sample Input

The sample input can be found at data/input/author_names.csv file. The input should be comma separated first name and last name values of author names.

eg:
```commandline
first_name,last_name
pierre,grivel
raul,serapioni
catherine,marquet
sabina,pannek
ralf,kemper
```

### Run code

1. Replace the `API_KEY_CONSTANT` in the `Constants.py` file with the API_Key obtained from Gender API.
2. Go to `GenderDiversityByAuthorNames.py` file.
3. Add the author names input file path as the `input_file`. (eg: `"data/input/author_names.csv"`)
4. Run the `GenderDiversityByAuthorNames.py` code.
5. Output json file can be found at `data/output/output.json` which includes the diversity indicator of authors based on their genders
6. output.json should look like,
```commandline
{
    "diversity_indicator": 0.9709505944546688
}
```