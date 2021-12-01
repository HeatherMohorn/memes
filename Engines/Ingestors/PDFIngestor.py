from ..QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import subprocess

class PDFIngestor(IngestorInterface):
    pass
"""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest')

        tmp = f'./tmp.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, 'r')
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                elem = line.split(' - ')
                quote = QuoteModel(elem[0], elem[1])
                quotes.append(quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
        """
