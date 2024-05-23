from snowflake.snowpark import Session
from os import getenv


def get_snowpark_session() -> Session:
    connection_parameters = {
        "account": getenv("ACCOUNT"),
        "user": getenv("USER"),
        "password": getenv("PASSWORD"),
        "database": getenv("DATABASE"),
        "schema": getenv("SCHEMA"),
    }
    builder = Session.builder.configs(options=connection_parameters)
    session = builder.create()
    return session
