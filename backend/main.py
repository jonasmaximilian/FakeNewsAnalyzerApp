from flask import Flask, request, jsonify, render_template
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from flask_cors import CORS

import logging

app = Flask(__name__)
CORS(app)

# load the pre-trained model and vectorizer
model, vectorizer = None, None


@app.route("/")
def home():
    return "<h1>Text Prediction</h1>"


#     return """<!DOCTYPE html>
# <html>
# <head>
#     <title>Text Prediction</title>
# </head>
# <body>
#     <h1>Text Prediction</h1>
#     <form method="POST" action="/predict">
#         <label for="text">Enter text:</label><br>
#         <textarea name="text" rows="4" cols="50"></textarea><br><br>
#         <input type="submit" value="Submit">
#     </form>
# </body>
# </html>
#     """


@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    # return "Hello cross-origin-world!"
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}

    # ensure text was properly submitted to our endpoint
    if request.method == "POST":
        # if request.form.get("text"):
        # read the text from the form
        # text = request.form.get("text")
        text = request.get_json()["inputField"]
        print(text)
        # since we are using just one text sample, we need to convert it to a list and then to a numpy array for vectorization

        try:
            # preprocess the text
            text_vector = vectorizer.transform([text])

            # classify the input text and then initialize the list of predictions to return to the client
            prediction = model.predict(text_vector)
            data["prediction"] = str(prediction[0])

            # indicate that the request was a success
            data["success"] = True

        except Exception as e:
            # log the error
            logging.error(str(e))

            # indicate that an error occurred
            data["error"] = "An error occurred while making the prediction."

    # return the data dictionary as a JSON response
    return data


def load_model():
    global model
    # load the pre-trained model
    model = joblib.load("model/pa_model.pkl")


def load_vectorizer():
    global vectorizer
    # load the pre-trained vectorizer
    vectorizer = joblib.load("model/vectorizer.pkl")


if __name__ == "__main__":
    print(
        (
            "* Loading model and starting Flask server..."
            "please wait until the server has fully started"
        )
    )
    # load the model and vectorizer
    load_model()
    load_vectorizer()
    app.run()
