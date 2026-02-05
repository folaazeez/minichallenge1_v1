
def validate_environment(values: dict) -> None:
    env = values.get("environment")
    replicas = values.get("replicaCount", 1)

    if not env:
        fail("environment is missing")  
      
    if not isinstance(replicas,int):
        fail("replicaCount must be an integer")

    if env == "prod" and replicas < 3:
        fail("prod requires at least 3 replicas")
        sys.exit(1)
