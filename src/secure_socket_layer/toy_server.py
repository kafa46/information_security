from flask import Flask, make_response, render_template, request
import os

BASE_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

print(TEMPLATES_DIR)


app = Flask(__name__, template_folder=TEMPLATES_DIR)

@app.route('/')
def main():
    return render_template(
        'index.html'
    )

if __name__=='__main__':
    # app.run()
    app.run(host='0.0.0.0', port='5001', debug=True)