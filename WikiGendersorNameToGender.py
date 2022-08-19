import PackageInstaller
from WikiGendersortModule.Wiki_Gendersort import wiki_gendersort, build_dataset


def install_packages():
    PackageInstaller.install("unidecode")
    PackageInstaller.install("wikipedia")


def get_gender(first_name):
    WG = wiki_gendersort()
    print("Checking name: " + str(first_name))
    return WG.assign(first_name)


def get_gender_by_file(input_file, output_file):
    WG = wiki_gendersort()
    return WG.file_assign(input_file, output_file)


def build_new_dataset():
    build_dataset()
