import yaml

yaml_file = sys.argv[1] if len(sys.argv) > 1 else "values.yaml"

def fail(msg:str,code:int=1)->None:
    print(f"ERROR: {msg}")
    sys.exit(code)

def load_yaml(path: str) -> dict:
    try:
        with open(yaml_file,"r") as f:
            values = yaml.safe_load(f) or {}
    except FileNotFoundError:
        fail(f"{yaml_file} not found")
    except yaml.YAMLError as e:
        fail(f"Invalid YAML: {e}")
