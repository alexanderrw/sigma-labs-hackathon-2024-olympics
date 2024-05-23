import pandas as pd
import streamlit as st


from .abc import PageABC


class HomePage(PageABC):
    @property
    def title(self) -> str:
        return "Home Page"

    def run(self) -> None:
        st.title("Olympic Fantasy Games Paris 2024")

        if self.session.current_user_id:
            st.subheader("Fantasy Home Section")
            st.write("Fantasy home details go here...")
        else:
            st.error("You need to be logged in to view the fantasy home section.")
