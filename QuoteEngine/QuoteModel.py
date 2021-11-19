import csv
import docx

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        string = f'"{self.body}" - {self.author}'

class CSVIngestor(IngestorInterface):
    allowed_extensions = [csv]

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

class DOCXIngestor(IngestorInterface):
    allowed_extensions = [docx]

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

class PDFIngestor(IngestorInterface):
    pass

class TextIngestor(IngestorInterface):
    allowed_extensions = [txt]

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
