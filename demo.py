from flask import Flask
from src.logger import logging

app = Flask(__name__)
@app.route ("/" , methods = ['GET' , 'POST'])

def index():
    logging.info("We are just testing the code logging moduls")
    return "Hello, This Project is Conduct by Krish Naik Youtube Channel"

if __name__ == "__main__":
    app.run(debug=True)