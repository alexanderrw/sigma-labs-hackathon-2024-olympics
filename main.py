from dotenv import load_dotenv

import streamlit as st

from core.session import Session
from core.ui import App

load_dotenv()


@st.cache_resource
def get_new_session():
    return Session()


def main() -> None:
    session = get_new_session()
    app = App(session=session)
    app.run()


if __name__ == "__main__":
    main()
