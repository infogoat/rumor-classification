
# Rumor Stance Detection

Detect the **stance** (support, deny, question, or neutral) of a rumor or news using a combination of deep learning models and web technologies.  
This project leverages a **Flask backend**, **TailwindCSS frontend**, and a **transformer-based** zero-shot classification model for production.

---

## 🚀 Project Structure

```bash
rumorStance/
├── flask-backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   ├── static/
│   ├── setup.sh / setup.bat
│   └── tailwind.config.js
├── Datasets/
│   ├── Fake News/
│       ├── fake_news.csv
│       └── true_news.csv
├── README.md
└── .gitignore
```

---

## ✨ Features

- **Zero-Shot Classification** using Transformer models (`facebook/bart-large-mnli`).
- **Foundational LSTM Model** for binary fake/real classification (early prototype).
- **Flask API** to handle model predictions efficiently.
- **Modern UI** built with TailwindCSS.
- **Authentication system** (Register, Login).
- **Opinion Section** for user feedback.
- **Multiple UI Pages** (About Us, FAQ, Contact).
- **Cross-platform setup scripts** (Windows and Linux).
- **Preprocessing of News Articles**.

---

## 🧠 Model Evolution

Initially, a custom **LSTM model** was developed for **binary classification** (Fake vs. Real news).  
However, during experimentation:

- **LSTM suffered from overfitting** on small datasets.
- To enhance performance and generalization, we **migrated** to a **Transformer-based Zero-Shot model**.
- **Final Production Model:** `facebook/bart-large-mnli` deployed via Hugging Face pipelines.

**Note:** The original LSTM architecture still exists inside the project as a reference.

---

## 📦 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/infogoat/rumorStance.git
cd rumorStance/flask-backend
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Install Frontend Dependencies (for Tailwind)

```bash
npm install
npm run dev
```

---

## 📈 Running the App

```bash
# Start Flask server
python app.py
```

- Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 🗄️ Datasets

- `Datasets/Fake News/fake_news.csv` — Fake news examples.
- `Datasets/Fake News/true_news.csv` — Real news examples.
- These datasets were used for initial model training and evaluation.
- **Important:** Files are large (above 50MB), which is why GitHub recommends Git Large File Storage (LFS).

---

## 📋 Available Pages

- **Home:** Main Prediction Interface
- **Login/Register:** User authentication
- **Opinion:** Submit your thoughts
- **FAQ:** Frequently Asked Questions
- **About Us:** Project Details
- **Contact:** Reach out form

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  
Please make sure to update tests as appropriate.

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to fork it, improve it, and use it in your own work.

---

## 🙏 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TailwindCSS](https://tailwindcss.com/)
- Special thanks to all open-source contributors whose packages made this project possible.

---

## 💬 Contact

If you have any questions or suggestions, feel free to reach out by creating an issue in the repository.

---
```

---

# ✅ Now, **what you should do**:

1. Create a new file in your project:  
`rumorStance/README.md`

2. Paste the above content exactly.

---

# ⚡ Bonus Tip:
Add a `.gitignore` like this inside `flask-backend/.gitignore`:

```bash
# Python
venv/
__pycache__/
*.pyc

# Node
node_modules/
package-lock.json

# Others
.DS_Store
*.log
.env
*.stackdump
```

👉 This will prevent you from accidentally uploading venv, node_modules, and other junk files.

---

Would you also like me to give a small "project logo/banner" you can put at the top of the README to make it even cooler? 🎨🚀 (optional but looks amazing)  
Want it?
