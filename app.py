import random
import os
import requests
from flask import Flask, render_template, abort, request, url_for
from Engines.MemeEngine.MemeGenerator import MemeGenerator
from Engines.Ingestors import Ingestor
import PIL


app = Flask(__name__)


def setup():
    """ Load all resources """

    quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                   './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                   './Engines/_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        list = Ingestor.parse(file)
        for item in list:
            quotes.append(item)

    images_path = "./Engines/_data/photos/dog/"
    imgs = []
    files = os.listdir(images_path)
    for file in files:
        if file.split('.')[-1] == 'jpg':
            imgs.append(file)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    im_path = "./Engines/_data/photos/dog/" + img
    quote = random.choice(quotes)
    path = MemeGenerator.make_meme(im_path, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    try:
        r = requests.get(url, allow_redirects=True)
        open('tmp.jpg', 'wb').write(r.content)
        path = MemeGenerator.make_meme('tmp.jpg', body, author)
        print(path)
        os.remove('tmp.jpg')
        return render_template('meme.html', path=path)
    except:
        print("Invalid URL")
        return render_template('meme_error.html')


if __name__ == "__main__":
    app.run()
