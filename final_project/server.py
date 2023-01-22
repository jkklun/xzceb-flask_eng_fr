"""
Server Translator
"""
from flask import Flask, render_template, request
from machinetranslation import translator
#import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    Traanslate English to French
    """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = translator.english_to_french(textToTranslate)
    print(french_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    Traanslate French to English
    """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = translator.french_to_english(textToTranslate)
    print(english_text)
    return english_text

@app.route("/")
def renderIndexPage():
    """
    Display Index Page
    """
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
