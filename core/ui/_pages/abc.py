from abc import ABC, abstractmethod

from core.session import Session


class PageABC(ABC):
    def __init__(self, session: Session):
        self.session = session

    @property
    @abstractmethod
    def title(self) -> str:
        ...

    @abstractmethod
    def run(self) -> None:
        ...
