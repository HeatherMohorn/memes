import csv
import docx

class QuoteModel():
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        string = f'"{self.body}" - {self.author}'
