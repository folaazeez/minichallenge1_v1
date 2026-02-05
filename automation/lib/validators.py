def validate_environment(values: dict) -> None:
    env = values.get("environment")
    replicas = values.get("replicaCount", 1)

    if not env:
        raise ValueError("environment is missing")

    if not isinstance(replicas, int):
        raise ValueError("replicaCount must be an integer")

    if env == "prod" and replicas < 3:
        raise ValueError("prod requires at least 3 replicas")
