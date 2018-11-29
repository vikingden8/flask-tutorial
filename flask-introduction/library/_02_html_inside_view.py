from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
            {authors_list}
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    # build an <ul> with authors
    authors_list = '<ul>'
    authors_list += '\n'.join(['<li>{author}</li>'.format(author=author) for author in authors])
    authors_list += '</ul>'

    return html.format(authors_list=authors_list)