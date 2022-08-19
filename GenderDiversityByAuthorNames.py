from GenderIdentification import gender_identification
from DiversityIndicator import get_diversity_indicator
import json


if __name__ == "__main__":
    input_file = "data/input/author_names.csv"
    gender_identification(input_file)
    gender_diversity_indicator = get_diversity_indicator()
    json_output = {
      "diversity_indicator": gender_diversity_indicator
    }

    with open("data/output/output.json", "w") as outfile:
        outfile.write(json.dumps(json_output, indent=4))
