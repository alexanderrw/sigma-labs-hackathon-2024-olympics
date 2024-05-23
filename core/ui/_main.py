import streamlit as st

from ._pages import (
    LoginSignupPage,
    LeaderboardPage,
    HomePage,
)
from ._pages.abc import PageABC
from core.session import Session


class App:
    def __init__(self, session: Session) -> None:
        self.session = session

        kwargs = {"session": self.session}
        self._pages: list[PageABC] = [
            HomePage(**kwargs),
            LoginSignupPage(**kwargs),
            LeaderboardPage(**kwargs),
        ]

    def run(self) -> None:
        number_of_pages = len(self._pages)
        page_number = st.sidebar.selectbox(
            label="Select page",
            options=range(number_of_pages),
            format_func=lambda page_no: self._pages[page_no].title,
        )
        page = self._pages[page_number]
        print(f"{self.session.current_user_id=}")
        page.run()
