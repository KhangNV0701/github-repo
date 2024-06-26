import os
from dotenv import load_dotenv
load_dotenv()


class GeminiAiCFG:
    API_KEY = os.environ["GEMINI_API_KEY"]
    API_MODEL = os.getenv("GEMINI_API_MODEL", "gemini-pro")
    API_EMBEDDING_MODEL = os.getenv("GEMINI_API_EMBEDDING_MODEL", "models/embedding-001")


class Neo4jCFG:
    URL = os.environ["NEO4J_URL"]
    USERNAME = os.environ["NEO4J_USERNAME"]
    PASSWORD = os.environ["NEO4J_PASSWORD"]


class MongodbCFG:
    MONGODB_USERNAME = os.environ["MONGODB_USERNAME"]
    MONGODB_PASSWORD = os.environ["MONGODB_PASSWORD"]
    MONGODB_HOST = os.environ["MONGODB_HOST"]
    MONGODB_NAME = os.environ["MONGODB_NAME"]
    MONGODB_COLLECTION_NAME_RELATED_EVENT = os.environ["MONGODB_COLLECTION_NAME_RELATED_EVENT"]
    MONGODB_INDEX_NAME_RELATED_EVENT = os.environ["MONGODB_INDEX_NAME_RELATED_EVENT"]

class ZillizCFG:
    ZILLIZDB_USERNAME = os.environ["ZILLIZDB_USERNAME"]
    ZILLIZDB_PASSWORD = os.environ["ZILLIZDB_PASSWORD"]
    ZILLIZDB_HOST = os.environ["ZILLIZDB_HOST"]
    ZILLIZDB_PORT = os.environ["ZILLIZDB_PORT"]
    ZILLIZDB_COLLECTION_NAME_RELATED_EVENT = os.environ["ZILLIZDB_COLLECTION_NAME_RELATED_EVENT"]

class MysqlCFG:
    MYSQL_HOST = os.environ["MYSQL_HOST"]
    MYSQL_USER = os.environ["MYSQL_USER"]
    MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
    MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]
    MYSQL_PORT = os.environ["MYSQL_PORT"]
