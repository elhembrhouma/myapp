import requests

# URL of your Flask API endpointp
url = 'http://127.0.0.1:5000/extract_pdf_info_and_text'

# Path to the PDF file you want to upload
pdf_file_path = r"C:\Users\LENOVO-PC\Downloads\elhem ben rhouma.pdf"

# Send POST request with the PDF file attached as form data
with open(pdf_file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# Print the response
print(response.json())
