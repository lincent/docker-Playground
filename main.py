import os
from dotenv import load_dotenv


def main():
    load_dotenv()

    mongo_uri = os.environ.get("MONGO_DB_URI")
    mongo_db_name = os.environ.get("MONGO_DB_NAME")
    openaq = os.environ.get("OPEN_AQ_API_KEY")
    cds_uri = os.environ.get("CDSAPI_URL")
    cds_key = os.environ.get("CDSAPI_KEY")

    print("I'm running over here on a docker container")
    print(f"mongo_uri = {mongo_uri}")
    print(f"mongo_db_name = {mongo_db_name}")
    print(f"openaq = {openaq}")
    print(f"cds_uri = {cds_uri}")
    print(f"cds_key = {cds_key}")


if __name__ == "__main__":
    main()
