from core.connections import get_snowpark_session
from core.ui import App


def main() -> None:
    session = get_snowpark_session()
    app = App(session=session)
    app.run()


if __name__ == "__main__":
    main()
