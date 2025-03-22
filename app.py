from flask import Flask, request, render_template
import boto3
import os

app = Flask(__name__)

AWS_REGION = "ap-south-1"
S3_BUCKET = "winston-terraform-s3-bucket"  
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        s3.upload_fileobj(file, S3_BUCKET, file.filename)
        return f"File {file.filename} uploaded successfully to S3!"
    return "No file uploaded."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)
