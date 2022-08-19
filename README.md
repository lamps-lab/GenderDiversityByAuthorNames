# GenderIdentificationByAuthorName
This repository contains all the approaches tried out and their libraries used for identifying the gender of the authors by using their name. 

## Approaches
1. NLTK
2. Gender Guesser
3. Gender API
4. Wiki GenderSort

To evaluate the performance a benchmark dataset with 7,076 names was used. 

Benchmark dataset: https://github.com/GenderGapSTEM-PublicationAnalysis/name_gender_inference/tree/main/name_gender_inference/test_data

Paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7924484/

## Gender Identification by Name using NLTK

In this approach we train a new "Naive Bayes" classifier using last letter of the given name/ first name as the gender feature. The names ending in a, e, and i are likely to be female, while names ending in k, o, r, s, and t are likely to be male. In this approach, we download male and female names from nltk corpus, use the last letter of names along with their gender label for training set.


### Instructions
* Run the following pip install command in the terminal
```commandline
pip install nltk
```

```commandline
import nltk
nltk.download()
```

* Run `NLTKNameToGender.py` script

## Gender Identification by Name using Gender Guesser

In this approach we used the gender-guesser PyPI https://pypi.org/project/gender-guesser/

This gender-guesser package has a dictionary which contains a list of names and identify name based on that.
Latest release was done 2016.


### Instructions
* Run the following pip install command in the terminal
```commandline
pip install gender-guesser
```
* Run `GenderGuesserNameToGender.py` script

## Gender Identification by Name using Gender API

### Instructions
1. Sign up for Gender-API at https://gender-api.com/ and get an API_Key.


3. Subscribe for relevant package based your requirements. Check the price at https://gender-api.com/en/pricing
* Note: Free subscription only contains 500 credits (only 500 names per month)
3. Replace the `API_KEY_CONSTANT` in the `GenderAPIConstants.py` file with the API_Key.


4. Run the `GenderAPINameToGender.py` code. This code will
   1. read the `data/raw_data/all.csv` file which contains benchmark dataset with 7,076 names, 
   2. get the gender for each name by invoking Gender API endpoint, and
   3. write the first name, last name, and identified gender for all the names in the benchmark dataset into `./Data/names_and_genders_gender_api.csv` file
   
    * Note: Since this dataset had 7,076 names, you need to have BASIC II subscription with 10,000 credits in Gender API.

5. The benchmark dataset has already identified genders for these names using Gender API tool. To evaluate the performance of Gender API, 
   1. go to `Evaluation.py` script,
   2. uncomment line that invoke `evaluate_gender_api()` function, and
   3. run the script

6. Run the `GenderDiversity.py` code to get the diversity indicator or authors based on their gender

# Gender Identification by Name using WikiGendersort

This approach based on the WikiGendersort code which can be found at 
https://github.com/nicolasberube/Wiki-Gendersort. The code is last updated 2 years ago.

Required:
* Python 3.9

### Instruction

1. Run `WikiGendersorNameToGender.py` script. This code will,
   1. install required packages if they are not installed already,
   2. read all `./Data/raw_data/all.csv` file which contains benchmark dataset with 7,076 names,
   3. get the first names and write them into a text file named `./Data/all_names.txt`,
   4. identify the gender of the first names using Wiki Gendersort,
   5. convert the result text file into csv file `./Data/name_and_gender.csv`
2. To evaluate the performance of Wiki Gendersort, 
   1. go to `Evaluation.py` script,
   2. uncomment line that invoke `evaluate_wiki_gendersort()` function, and
   3. run the script
