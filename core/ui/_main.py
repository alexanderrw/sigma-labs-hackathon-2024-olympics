import streamlit as st

from ._pages import (
    LoginSignupPage,
)
from ._pages.abc import PageABC
from core.session import Session


class App:
    def __init__(self, session: Session) -> None:
        self._session = session
        kwargs = {"session": self._session}
        self._pages: list[PageABC] = [
            LoginSignupPage(**kwargs),
        ]

    def run(self) -> None:
        number_of_pages = len(self._pages)
        page_number = st.sidebar.selectbox(
            label="Select page",
            options=range(number_of_pages),
            format_func=lambda page_no: self._pages[page_no].title
        )
        page = self._pages[page_number]
        page.run()
