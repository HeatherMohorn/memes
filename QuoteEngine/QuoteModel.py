from abc import ABC, abstractmethod
import csv

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

class CSVIngestor(IngestorInterface):
    def parse(cls, path):
        quotes = []
        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for elem in reader:
                quote = QuoteModel(elem['body'], elem['author'])
                quotes.append(quote)
        return quotes

class DOCXIngestor(IngestorInterface):
    pass

class PDFIngestor(IngestorInterface):
    pass

class TXTIngestor(IngestorInterface):
    def parse(cls, path):
        quotes = []
        with open(path, 'r') as infile:
            contents = infile.read()
            lines = contents.split('\n')
        for line in lines:
            elements = line.split(' - ')
            quote = QuoteModel(elements[0], elements[1])
            quotes.append(quote)
        return quotes
