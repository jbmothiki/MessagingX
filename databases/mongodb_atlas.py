import os
import logging
from pymongo import MongoClient


def establish_mongodb_connection():
    """
    Establishes a connection to the MongoDB database.
    Return: A MongoClient object representing the MongoDB database connection.
    Raises Exception: If the connection to the MongoDB database fails.
    """

    MONGO_CONNECTION_STRING = "mongodb+srv://{}:{}@{}"
    mongo_db_user = os.getenv('MONGO_DB_USER')
    mongo_db_password = os.getenv('MONGO_DB_PASSWORD')
    mongo_db_cluster = os.getenv('MONGO_DB_CLUSTER')

    if not all([mongo_db_user, mongo_db_password, mongo_db_cluster]):
        logging.fatal("Unable to get all MongoDB details from the environment.")
        raise ValueError("Incomplete MongoDB Details")

    try:
        client = MongoClient(MONGO_CONNECTION_STRING.format(mongo_db_user, mongo_db_password, mongo_db_cluster))
        client.admin.command('ping')
        return client
    except Exception as e:
        logging.fatal("Failed to establish MongoDB connection: %s", e)
        raise
