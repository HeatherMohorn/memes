import QuoteModel
import IngestorInterface

class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')
        quotes = []
        with open(path, 'r') as infile:
            contents = infile.read()
            lines = contents.split('\n')
        for line in lines:
            elements = line.split(' - ')
            quote = QuoteModel(elements[0], elements[1])
            quotes.append(quote)
        return quotes
