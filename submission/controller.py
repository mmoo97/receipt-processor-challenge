from flask import Flask, request
import receipt_services as rs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.post("/receipts/process")
def process_receipt():
    return rs.process_receipt(request)

@app.get("/receipts/<id>/points")
def get_points(id):
    return rs.get_points(id)