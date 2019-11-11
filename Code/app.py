from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
from histogram import read_file, histogram_dictonary
from sample import better_words
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/csmarkov')

client = MongoClient(host=host)
client = MongoClient(host=f'{host}?retryWrites=false')
#Database associated with Client
db = client.get_default_database()



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    words = read_file('hist_test.txt')
    number_of_words = 10
    histogram = histogram_dictonary(words)

    #user has inputed a number for the sentence length
    if request.method == 'POST':
        number_of_words = request.form.get('word_count')

    sentence = better_words(number_of_words, len(words), histogram)
    return render_template('index.html', sentence=sentence)