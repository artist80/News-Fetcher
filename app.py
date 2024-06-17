from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_NEWS_API_KEY' with your actual NewsAPI key
NEWS_API_KEY = 'Enter_Your_API_Key_From_NewsAPI_Website'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news', methods=['POST'])
def get_news():
    query = request.form.get('query')
    params = {
        'q': query,
        'apiKey': NEWS_API_KEY,
        'country': 'us'
    }
    response = requests.get(NEWS_API_URL, params=params)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
