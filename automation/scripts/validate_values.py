
import sys
from lib.fail import fail
from lib.loader import load_yaml
from lib.validators import validate_environment


def main() -> None:
    try:
        values = load_yaml("values.yaml")
        validate_environment(values)
        print("File validated successfully ✅")
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
