import streamlit as st


from .abc import PageABC


class AthletePickerPage(PageABC):
    EVENTS_TABLE: str = "TOKYO_EVENTS"

    @property
    def title(self) -> str:
        return "Athlete Picker"

    def run(self) -> None:
        st.title("Athlete Picker")



    def _get_available_events(self):
        self.session.snowpark_session.sql(
            """
            SELECT 
            """
        )
