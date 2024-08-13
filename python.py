from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/like', methods=['POST'])
def like():
    # Handle the like button press
    return "You liked the image!"

if __name__ == '__main__':
    app.run(debug=True)
