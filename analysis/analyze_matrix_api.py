from pathlib import Path
import yaml

DATASETS_PATH = Path("analysis/datasets")
CURRENT_DATASET = "matrix-org_open-api_19-12-2024_CET16h-14m/data"
CURRENT_DATASET_PATH = DATASETS_PATH / CURRENT_DATASET

def print_all_clientserver_endpoints():
    path = CURRENT_DATASET_PATH / "client-server"
    endpoints = []
    for yaml_file in path.glob("**/*.yaml"):
        read_yaml = yaml.safe_load(yaml_file.read_text())
        try:
            for endpoint in read_yaml["paths"].keys():
                endpoints.append(endpoint)
        except:
            pass
    
    for ep in endpoints:
        print(ep)

if __name__ == '__main__':
    print_all_clientserver_endpoints()
