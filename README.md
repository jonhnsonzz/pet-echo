[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

# PetEcho 🐾 — Pet Symptom Helper

**"Something's wrong with my pet. Should I rush to the vet or wait?"**

> It's 2 AM. Your cat has diarrhea. You're not sure if it's an emergency or something you can monitor at home. You Google it and find nothing but vet ads. PetEcho tells you: what's likely causing it, when to see a vet, and what to watch for.

[中文说明](README_CN.md)

---

## 😰 The Problem

Every pet owner knows this feeling:

- Your pet is vomiting/diarrhea but still acting fine — is it an emergency?
- Dog suddenly won't eat — picky or actually sick?
- It's midnight, vet is closed — what can you do right now?
- You want to avoid an unnecessary vet bill, but you also don't want to delay real treatment

**PetEcho is built for these moments — helping you make a smarter decision when you're unsure.**

## ✨ Features

- **Symptom Assessment** — Describe what's happening, get an informed severity判断
- **Home Care Guidance** — What to monitor, when it can wait, when it can't
- **Trend Tracking** — Log over time so patterns become visible
- **Reduce Anxiety** — Not every late-night incident needs an ER run

## 📱 Compatibility

Works in any phone browser — **WeChat, Chrome, Safari**. No app download, no account needed.

## 🔒 Privacy

- All data stored **locally on your device** — nothing uploaded to any server
- No phone number, email, or account required
- No tracking, no data selling

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Installation

```bash
git clone https://github.com/jonhnsonzz/pet-echo.git
cd pet-echo
pip install -r requirements.txt
```

### Configuration

Copy the environment template and add your API key:

```bash
cp .env.example .env
# Edit .env and set: OPENAI_API_KEY=your_key_here
```

### Run

```bash
python app.py
```

Open `http://localhost:5000` in your phone browser.

---

## 📂 Project Structure

```
pet-echo/
├── app.py              # Flask application
├── prompts.py          # AI analysis prompts
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend UI (mobile-optimized)
└── data/
    └── sample_entries.json  # Sample data
```

---

## 💡 Philosophy

You are the best observer of your pet — you know them best.

What you lack is not expertise, but **a bridge between your observations and good judgment**.

PetEcho is not a medical device. It cannot replace a vet. What it does: help you make a more informed decision when you're unsure whether to seek care.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License — free to use, including commercially.

---

**Made for pet parents who want to make smarter care decisions.** 🐶🐱
