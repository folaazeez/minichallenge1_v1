import yaml
import sys

yaml_file = sys.argv[1] if len(sys.argv) > 1 else "values.yaml"

def load_yaml(path: str) -> dict:
    try:
        with open(yaml_file,"r") as f:
            values = yaml.safe_load(f) or {}
    except FileNotFoundError:
        fail(f"{yaml_file} not found")
    except yaml.YAMLError as e:
        fail(f"Invalid YAML: {e}")
