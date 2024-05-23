from dotenv import load_dotenv

from core.session import Session
from core.ui import App

load_dotenv()


def main() -> None:
    session = Session()
    app = App(session=session)
    app.run()


if __name__ == "__main__":
    main()
