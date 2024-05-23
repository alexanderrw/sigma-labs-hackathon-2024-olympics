from snowflake.snowpark import Session

import streamlit as st

from ._pages import (
    LoginSignupPage,
)
from ._pages.abc import PageABC


class App:
    def __init__(self, session: Session) -> None:
        self._session = session
        self._pages = [
            LoginSignupPage()
        ]

    def run(self) -> None:
        page: PageABC = st.sidebar.selectbox(
            title="App Navigation",
            options=self._pages,
            format_func=lambda p: p.title
        )
        page.run()
