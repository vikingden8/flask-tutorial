from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    # build an <ul> with authors
    return html