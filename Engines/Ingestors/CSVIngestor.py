import QuoteModel
import IngestorInterface

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
                quote = QuoteModel(elem['body'], elem['author'])
                quotes.append(quote)
        return quotes
