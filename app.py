import random
import os
import requests
from flask import Flask, render_template, abort, request, url_for
from Engines.MemeEngine.MemeGenerator import MemeGenerator
from Engines.Ingestors import Ingestor

# @DONE Import your Ingestor and MemeEngine classes

app = Flask(__name__)

#meme = MemeGenerator('./static')


def setup():
    """ Load all resources """

    quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                   './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                   #'./Engines_data/DogQuotes/DogQuotesPDF.pdf',
                   './Engines/_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for file in quote_files:
        list = Ingestor.parse(file)
        for item in list:
            quotes.append(item)

    # DONE: Use the Ingestor class to parse all files in the
    # quote_files variable


    images_path = "./Engines/_data/photos/dog/"
    imgs = []

    # DONE: Use the pythons standard library os class to find all
    # images within the images images_path directory
    files = os.listdir(images_path)
    for file in files:
        if file.split('.')[-1] == 'jpg':
            imgs.append(file)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @DONE:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array

    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    im_path = "./Engines/_data/photos/dog/" + img
    quote = random.choice(quotes)
    path = MemeGenerator.make_meme(im_path, quote.body, quote.author)
    #path = 'shoe-shopping_meme.jpg'
    #path = url_for('static', filename=path)
    #print(path)
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
    r = requests.get(url, allow_redirects=True)
    open('tmp.jpg', 'wb').write(r.content)
    path = MemeGenerator.make_meme('tmp.jpg', body, author)
    print(path)
    os.remove('tmp.jpg')
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
