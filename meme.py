import os
import random
from Engines.MemeEngine.MemeGenerator import MemeGenerator
from Engines.Ingestors import Ingestor
import argparse
# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    quotes = []
    if path is None:
        images = "./Engines/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
            #make random
        img = random.choice(imgs)
        #img = "./Engines/_data/photos/dog/xander_1.jpg"
    else:
        img = path[0]
    print("img: " + img)
    if body is None:
        quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                       #'./Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                       #'./Engines/_data/DogQuotes/DogQuotesPDF.pdf',
                       #'./Engines/_data/DogQuotes/DogQuotesCSV.csv'
                       ]
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        #change this to random
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    path = MemeGenerator.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description = "Enter details")
    parser.add_argument('--path', type = str)
    parser.add_argument('--body', type = str)
    parser.add_argument('--author', type = str)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
