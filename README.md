# PetEcho 🐾

**Your Pet's Emotional Mirror**

> Every moment with your pet tells a story. PetEcho listens, understands, and reflects.

PetEcho is an AI-powered emotional companion that transforms your daily moments with your pet into deep emotional insights. Unlike health trackers that measure steps and calories, PetEcho focuses on what truly matters—the emotional bond between you and your companion.

## ✨ Features

### 💭 Emotional Intelligence
Share any moment from your day—a quirky behavior, a tender interaction, a funny accident—and PetEcho will decode the emotional narrative behind it. Understand what your pet is really feeling.

### 📊 Weekly Bond Reports
Get AI-generated weekly summaries that highlight patterns in your pet's emotional well-being, memorable moments you've shared, and actionable tips to strengthen your connection.

### 🎭 Mood Tracking
Tag your entries with emotional moods. Over time, PetEcho helps you see the emotional journey of your pet—and your relationship.

### 🔒 Privacy First
- All data stays local to your device
- No account required
- No tracking, no selling data
- Device ID-based storage

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- An OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/pet-echo.git
cd pet-echo

# Install dependencies
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=sk-your-key-here
```

### Run

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `SECRET_KEY` | Flask secret key for sessions | No (uses default) |
| `PORT` | Server port (default: 5000) | No |
| `FLASK_ENV` | Set to `development` for debug mode | No |

## 🏗️ Project Structure

```
pet-echo/
├── app.py              # Flask application
├── prompts.py          # AI prompts for emotional analysis
├── requirements.txt   # Python dependencies
├── templates/
│   └── index.html     # Frontend UI
├── static/            # Static assets (CSS, JS, images)
└── data/
    └── sample_entries.json  # Sample data (for reference)
```

## 🎨 How It Works

1. **Share a Moment**: Write about any interaction with your pet—a walk, a cuddle, a funny moment
2. **AI Analysis**: PetEcho's emotional intelligence analyzes the narrative for behavioral patterns, emotional signals, and bond indicators
3. **Get Insights**: Receive warm, actionable insights about your pet's emotional state and your relationship
4. **Track Progress**: Build a diary of moments and watch your pet's emotional journey unfold

## 💡 The Philosophy

We believe the most important data about your pet isn't measured in steps or calories—it's in the quality of the moments you share.

PetEcho is built on the insight that **pet owners are the best source of emotional data**. Your observations, your stories, your interpretations are more valuable than any sensor reading.

The result is a new kind of pet tech: one that starts with the heart, not the hardware.

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/api/journal` | POST | Create new diary entry |
| `/api/journal/<device_id>` | GET | Get all entries for a device |
| `/api/journal/<device_id>/weekly-summary` | GET | Get AI weekly summary |
| `/api/moods` | GET | Get available mood tags |

## 🌐 Deployment

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Railway, Render, Fly.io

Set the `OPENAI_API_KEY` environment variable in your dashboard and deploy.

## 📖 Documentation

- [English Documentation](README.md) ← You are here
- [中文文档](README_CN.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use, modify, and distribute.

---

**Made with 💕 for pet parents who believe every pet has a story worth understanding.**
