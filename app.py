from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language).text

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
