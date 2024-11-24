import os
if not os.getcwd().endswith('gdpr-helpers'):
    os.chdir('gdpr-helpers')

import glob
from gdpr_helpers import Anonymizer

search_pattern = "data/adventure-works-bike-buying.csv"

am = Anonymizer(
    project_name="gdpr-workflow",
    run_mode="cloud",
    transforms_config="src/config/transforms_config.yaml",
    synthetics_config="src/config/synthetics_config.yaml",
    endpoint="https://api.gretel.cloud"
    )

for dataset_path in glob.glob(search_pattern):
    am.anonymize(dataset_path=dataset_path)