import os
import random
from Engines.MemeEngine.MemeGenerator import MemeGenerator
from Engines.Ingestors import Ingestor
import argparse


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    quotes = []
    if path is None:
        images = "./Engines/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path
    if body is None:
        quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                       './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                       './Engines/_data/DogQuotes/DogQuotesCSV.csv'
                       ]
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        quote = random.choice(quotes)
        path = MemeGenerator.make_meme(img, quote.body, quote.author)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        path = MemeGenerator.make_meme(img, body, author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enter details")
    parser.add_argument('--path', type=str)
    parser.add_argument('--body', type=str)
    parser.add_argument('--author', type=str)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
