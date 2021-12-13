from ..QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import docx


class DOCXIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                elem = para.text.split(' - ')
                elem[0] = elem[0].strip('"')
                quote = QuoteModel(elem[0], elem[1])
                quotes.append(quote)
        return quotes
