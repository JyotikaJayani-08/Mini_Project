from flask import Flask, render_template, request, jsonify, send_from_directory
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def convert_to_sketch(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    def dodge_v2(x, y):
        return cv2.divide(x, 255 - y, scale=256)

    sketch = dodge_v2(gray_image, blurred_image)

    sketch_path = os.path.join(UPLOAD_FOLDER, "sketch.jpg")
    cv2.imwrite(sketch_path, sketch)
    return sketch_path

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(image_path)

    sketch_path = convert_to_sketch(image_path)
    return jsonify({"sketch_url": sketch_path})

@app.route("/static/<filename>")
def send_sketch(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
