# 📷 GradeLens AI — Teacher's Quick Grading Assistant

AI-assisted grading for teachers. Scan a student's answer sheet with your
phone camera, get an AI suggestion, then **you** decide the final score.

> ⚠️ AI assists · Teacher decides · Education stays human

## 🎯 Features

- 📷 Camera capture directly in the browser (phone or desktop)
- 🤖 AI suggestion with confidence score
- ✏️ Teacher override — the final decision is always yours
- 💾 Save and review past grades
- 📋 One-tap copy of the grade summary

## 🚀 Deploy in 5 minutes

### 1. Push to GitHub

```bash
git init gradelens-ai
cd gradelens-ai
# copy the files listed below
git add .
git commit -m "Initial GradeLens AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/gradelens-ai.git
git push -u origin main
```

### 2. Deploy on Streamlit Cloud

1. Go to <https://share.streamlit.io> and sign in with GitHub.
2. Click **Create app** → **Deploy a public app from GitHub**.
3. Fill in:
   - **Repository**: `YOUR_USERNAME/gradelens-ai`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy**.

Streamlit installs `requirements.txt` and your app is live in ~1 minute.

Any `git push` to `main` triggers an automatic rebuild.

## 📁 Project structure

```
gradelens-ai/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── config.toml
```

## 📞 Contact

**Gesner Deslandes · Software Engineer**
- 📞 (509)-47385663
- ✉️ deslandes78@gmail.com
