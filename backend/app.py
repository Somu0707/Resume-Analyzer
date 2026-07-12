from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import pdfplumber
import io
from analyzer import analyze_resume

app = Flask(__name__)
CORS(app)

# AWS Configuration
REGION = "us-east-1"
BUCKET_NAME = "uday-resume-analyzer-2026"

s3 = boto3.client("s3", region_name=REGION)


@app.route("/")
def home():
    return jsonify({
        "message": "AI Resume Analyzer Backend Running"
    })


@app.route("/upload", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["resume"]
    filename = file.filename

    try:

        # Read PDF
        pdf_bytes = file.read()

        # Upload to AWS S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=pdf_bytes
        )

        # Extract text
        extracted_text = ""

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

        # Analyze Resume
        analysis = analyze_resume(extracted_text)

        return jsonify({

            "message": "Resume Uploaded Successfully",

            "text": extracted_text,

            "score": analysis["score"],

            "skills": analysis["skills"],

            "missing": analysis["missing"],

            "suggestions": analysis["suggestions"]

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)