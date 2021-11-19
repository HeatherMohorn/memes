from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path): -> boolean
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]
        pass

class Ingestor(IngestorInterface):
    ingestors = [TextIngestor, DOCXIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return imporser.parse(path)
