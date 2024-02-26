from flask import Flask, request, jsonify
import os
import PyPDF2

app = Flask(__name__)

def extract_info_and_text_from_pdf(file_path):
    try:
        # Open the PDF file
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            reader = PyPDF2.PdfReader(file)

            # Accessing metadata
            metadata = reader.metadata

            # Extraction of metadata
            title = metadata.title if metadata.title else 'No title found'

            # Extraction of text
            text = ""
            for page_num in range(len(reader.pages)):
                page_text = reader.pages[page_num].extract_text()
                text += page_text

            # Return extracted title and text as dictionary
            return {
                "title": title,
                "extracted_text": text.strip()
            }

    except Exception as e:
        return {"error": str(e)}

@app.route('/extract_pdf_info_and_text', methods=['POST'])
def extract_pdf_info_and_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    pdf_file = request.files['file']
    if pdf_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily
    temp_file_path = 'temp.pdf'
    pdf_file.save(temp_file_path)

    # Extract info and text from the PDF
    result = extract_info_and_text_from_pdf(temp_file_path)

    # Remove the temporary file
    os.remove(temp_file_path)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
