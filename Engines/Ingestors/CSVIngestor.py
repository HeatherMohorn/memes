from ..QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import csv

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')
        quotes = []
        with open(path, 'r') as infile:
            reader = csv.DictReader(infile)
            for elem in reader:
                text = elem['body'].strip('"')
                quote = QuoteModel(text, elem['author'])
                quotes.append(quote)
        return quotes
