from snowflake.snowpark import Session
from os import getenv


def get_snowpark_session() -> Session:
    connection_parameters = {
        "account": getenv("ACCOUNT"),
        "user": getenv("USER"),
        "__string": getenv("PASSWORD"),
        "database": getenv("DATABASE"),
        "schema": getenv("SCHEMA"),
    }
    session = Session.builder.configs(connection_parameters).create()
    return session
