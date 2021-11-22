import QuoteModel
import IngestorInterface
import docx

class DOCXIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')
        quotes = []
        doc = docx.Documents(path)

        for para in doc.paragraphs:
            elem = para.text.split(' - ')
            quote = QuoteModel(elem[0], elem[1])
            quotes.append(quote)
        return quotes
