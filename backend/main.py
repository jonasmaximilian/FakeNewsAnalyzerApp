from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('model/pa_model.pkl')

