from abc import ABC, abstractmethod

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

class IngestorInterface(ABC):

    @classmethod
    @abstractmethod
    def can_ingest(cls, path): -> boolean
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]
        pass
