import pandas as pd


def preprocess_raw_data(df):
    df = df[df["gender"] != "u"]
    return df


def raw_data_csv_to_first_name_text(csv_filepath, txt_filepath):
    print("Reading csv file " + str(csv_filepath) + " ...")
    df = pd.read_csv(csv_filepath)
    df = preprocess_raw_data(df)
    first_names = df["first_name"].tolist()

    # open file in write mode
    with open(txt_filepath, 'w', encoding='utf8') as fp:
        for name in first_names:
            # write each item on a new line
            fp.write("%s\n" % name)
        print('First names are written into the text file...')


def firstname_gender_text_to_output_csv(txt_filepath, csv_filepath):
    df = pd.read_csv(txt_filepath, delimiter="\t", names=["first_name", "gender"])
    df.to_csv(csv_filepath, encoding='utf-8', index=False)
    print("Firstnames and genders are written into the csv file...")
