
from .DOCXIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .IngestorInterface import IngestorInterface

class Ingestor(IngestorInterface):
    ingestors = [TextIngestor, DOCXIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
