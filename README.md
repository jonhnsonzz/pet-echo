# PetEcho 🐾 — Pet Symptom Helper

**"Something's wrong with my pet. Should I rush to the vet or wait?"**

> It's 2 AM. Your cat has diarrhea. You're not sure if it's an emergency or something you can monitor at home. You Google it and find nothing but vet ads. PetEcho tells you: what's likely causing it, when to see a vet, and what to watch for.

## 😰 Sound familiar?

- Your pet is vomiting/diarrhea but still acting fine — ER or wait?
- Dog suddenly won't eat — picky or actually sick?
- Pet is hiding, lethargic, or acting weird — bad mood or something serious?
- It's midnight, vet is closed — what can you do right now?
- You want to avoid an unnecessary vet visit, but you also don't want to wait if it's serious

**PetEcho is built for exactly these moments.**

## What PetEcho Does

After you describe what's going on with your pet:

1. **Assess severity** — Is this common and minor, or does it warrant immediate vet attention?
2. **Home care guidance** — What can you do at home, how long to monitor, what symptoms are red flags
3. **Track over time** — Log changes so patterns emerge and decisions get easier
4. **Reduce anxiety** — Not every late-night incident needs an ER run, but you want to be sure

## 📱 Works On

Any phone browser — WeChat, Chrome, Safari. No app download, no account needed.

## 🔒 Your Data, Your Device

- Everything stays local on your device — nothing uploaded to any server
- No phone number, email, or account required
- No tracking, no data selling

## 🚀 Quick Start

### Requirements
- Python 3.8+
- OpenAI API Key

### Install

```bash
git clone https://github.com/jonhnsonzz/pet-echo.git
cd pet-echo
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env:
# OPENAI_API_KEY=your_key_here
```

### Run

```bash
python app.py
```

Then open `http://your-server-ip:5000` in your phone browser.

## Project Structure

```
pet-echo/
├── app.py              # Flask application
├── prompts.py          # AI analysis prompts
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend (mobile-optimized)
└── data/
    └── sample_entries.json  # Sample data
```

## Philosophy

You are the best observer of your pet — you live with them every day, you know what's normal for them.

What you lack is a bridge between your observations and medical judgment.

PetEcho is not a medical device. It cannot replace a vet. What it does: **help you make a more informed decision when you're unsure whether to seek care.**

## 📄 License

MIT License — free to use, including commercially.
