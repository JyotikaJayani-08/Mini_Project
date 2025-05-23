# Mini Project: Bidirectional Image Generation

This project explores **bi-directional image and sketch conversion** using a combination of **Pix2Pix GAN** for sketch-to-image synthesis and **OpenCV-based edge detection** for image-to-sketch transformation. RenderX is a web-based platform that makes advanced image processing accessible to users without technical expertise.

## 🧠 Objective

* Develop a secure Express backend with user authentication
* Create a Flask service for ML inference with Pix2Pix models
* Integrate both services for seamless image enhancement
* Deploy on Render for global accessibility
* Ensure support for multiple enhancement models (faces, flowers, shoes, etc.)

## 🛠 Methods

* **Pix2Pix GAN** (paired image-to-image translation):
  * Generator: U-Net architecture for mapping sketches to realistic images
  * Discriminator: PatchGAN for distinguishing real from generated images

* **Image-to-Sketch Conversion**:
  * Implemented using **OpenCV edge detection techniques** (grayscale + Gaussian blur + Laplacian/Canny filters)

* **Architecture**:
  * Express.js backend for authentication and frontend management
  * Flask server for ML inference and image processing
  * MongoDB for user data storage

## 📊 Results Summary

* Pix2Pix-generated images became clearer and more label-consistent over time
* The CNN classifier achieved high accuracy (>95%) on real data and performed competitively with generated data
* OpenCV-based sketches retained key outlines, enabling round-trip sketch-image-sketch tests
* The system successfully demonstrates bidirectional conversion between sketches and realistic images

## 📁 Directory Structure
```
📦 Mini_Project
├─ .env
├─ .gitattributes
├─ README.md
├─ app.py
├─ index.js
├─ models
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-310.pyc
│  │  ├─ __init__.cpython-312.pyc
│  │  ├─ pix2pix.cpython-310.pyc
│  │  └─ pix2pix.cpython-312.pyc
│  ├─ birds.pth
│  ├─ cats.pth
│  ├─ face_gen_ep10.pth
│  ├─ faces.pth
│  ├─ flower.pth
│  ├─ palceholder_Creater.py
│  ├─ pix2pix.py
│  ├─ shoes.pth
│  └─ user.js
├─ package-lock.json
├─ package.json
├─ public
│  ├─ Logo3.png
│  ├─ av1.png
│  ├─ av2.png
│  ├─ av3.png
│  ├─ av4.png
│  ├─ av5.png
│  ├─ av6.png
│  ├─ av7.png
│  ├─ av8.png
│  ├─ choseModel.css
│  ├─ choseModel.js
│  ├─ choseModelBackground.png
│  ├─ enhance.js
│  ├─ icon.png
│  ├─ imagemain.png
│  ├─ landingPage.css
│  ├─ landingPageBackground.png
│  ├─ landingPageImage.png
│  ├─ login.js
│  ├─ loginRegister.css
│  ├─ loginRegisterBackground.png
│  ├─ mainPage.css
│  ├─ payment.css
│  ├─ payment.js
│  ├─ real.jpg
│  ├─ register.js
│  ├─ sketch.jpg
│  ├─ support.css
│  └─ support.js
├─ requirements.txt
├─ static
│  ├─ images
│  │  └─ background.jpg
│  ├─ ml_model.css
│  ├─ ml_model.js
│  ├─ output
│  ├─ placeholder
│  └─ uploads
└─ views
   ├─ choseModel.ejs
   ├─ landing.ejs
   ├─ login.ejs
   ├─ mainPage.ejs
   ├─ payment.ejs
   ├─ register.ejs
   └─ support.ejs
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## ⚙️ Requirements

* Python 3.7+
* Node.js 14+
* MongoDB
* PyTorch
* OpenCV
* Express.js
* Flask

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install
```

## 🚀 Usage

1. **Start the Express server**:
   ```bash
   node index.js
   ```

2. **Start the Flask server**:
   ```bash
   python app.py
   ```

3. **Access the application**:
   * Open your browser and navigate to `http://localhost:3000`
   * Register/login to your account
   * Choose between sketch-to-image or image-to-sketch conversion
   * Upload your image and select a model (faces, flowers, shoes, etc.)
   * View and download your enhanced image

## 📌 Key Takeaways

* **Pix2Pix GANs** effectively generate class-conditional realistic images from sketches
* **OpenCV** enables fast and lightweight sketch extraction without training
* The integrated Express-Flask architecture provides a seamless user experience
* Multiple pre-trained models support diverse image domains (faces, flowers, shoes, birds, cats)
* The project demonstrates practical applications in design tools, digital art, and image processing

---
