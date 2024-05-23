from snowflake.snowpark import Session as SnowparkSession
from dataclasses import dataclass, field
from typing import Optional

from core.connections import get_snowpark_session


@dataclass
class Session:
    snowpark_session: SnowparkSession = field(default_factory=get_snowpark_session)
    current_user_id: Optional[int] = None

    def __post_init__(self):
        print("Making new session...")
