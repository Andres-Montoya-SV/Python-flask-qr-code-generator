# Simple QR Generator Site / API
This is a simple QR code generator site and API. It is built with Flask and uses the `qrcode` library to generate QR codes.

## Usage

### Site
The site is hosted at [http://127.0.0.1:5000/](http://127.0.0.1:5000/). You can use it to generate QR codes for URLs, text, and email addresses.

### API

#### Generate QR code
You can generate a QR code by sending a POST request to `/api/generate` with the following JSON payload:
```form-data
url: str
size: int
border: int
file_name: str
background: str
color: str
```

- `url`: The URL, text, or email address to encode in the QR code.

- `size`: The size of the QR code (in pixels).

- `border`: The width of the border around the QR code (in pixels).

- `file_name`: The name of the file to save the QR code as.

- `background`: The background color of the QR code (in hexadecimal).

- `color`: The color of the QR code (in hexadecimal).

The API will return a JSON response with the URL of the generated QR code.

#### Example
```python
import requests

url = 'http://123.com'
size = 200
border = 10
file_name = 'qr_code.png'
background = 'ffffff'
color = '000000'

payload = {
    'url': url,
    'size': size,
    'border': border,
    'file_name': file_name,
    'background': background,
    'color': color
}

response = requests.post('http://127.0.0.1:5000/api/generate', data=payload)
print(response.json())
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Andres-Montoya-SV/Python-flask-qr-code-generator.git
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.