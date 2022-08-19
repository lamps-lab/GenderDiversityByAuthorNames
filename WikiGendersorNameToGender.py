import PackageInstaller
from WikiGendersortModule.Wiki_Gendersort import wiki_gendersort, build_dataset
from FileConversion import raw_data_csv_to_first_name_text, firstname_gender_text_to_output_csv


def install_packages():
    PackageInstaller.install("unidecode")
    PackageInstaller.install("wikipedia")


def get_gender(first_name):
    WG = wiki_gendersort()
    print("Checking name: " + str(first_name))
    return WG.assign(first_name)


def gender_identification(input_firstname_file, output_firstname_gender_file):
    WG = wiki_gendersort()
    WG.file_assign(input_firstname_file, output_firstname_gender_file)
    print("Gender identification is completed...")


def build_new_dataset():
    build_dataset()


if __name__ == "__main__":
    install_packages()
    raw_data_file = 'Data/raw_data/all.csv'
    input_firstname_file = 'Data/all_names.txt'
    output_firstname_gender_file = 'Data/name_and_gender.txt'
    output_data_file = './Data/name_and_gender.csv'
    raw_data_csv_to_first_name_text(raw_data_file, input_firstname_file)
    gender_identification(input_firstname_file, output_firstname_gender_file)
    firstname_gender_text_to_output_csv(output_firstname_gender_file, output_data_file)
