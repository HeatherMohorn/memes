import csv
import docx


class QuoteModel():
    def __init__(self, body, author):
        self.body = str(body)
        self.author = str(author)

    def __str__(self):
        string = 'QuoteModel ' + self.body + ' - ' + self.author
        return string
