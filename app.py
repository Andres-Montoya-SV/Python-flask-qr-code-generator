## import flask and qr code generator
from flask import Flask, render_template, request
import qrcode

## create a flask app
app = Flask(__name__)

## create a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

## create a route for the qr code generator
@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    size = request.form['size']
    border = request.form['border']
    file_name = request.form['file_name']
    background = request.form['background']
    color = request.form['color']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=int(size),
        border=int(border),
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=background)
    img.save(f'static/{file_name}.png')
    return render_template('index.html', file_name=f'/static/{file_name}.png')


## run the app

if __name__ == '__main__':
    app.run(debug=True)