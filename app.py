"""
PetEcho - AI Pet Emotional Companion
A warm companion that listens to your pet stories and provides emotional insights.
"""

import os
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
from prompts import PET_EMOTION_ANALYSIS_PROMPT, WEEKLY_SUMMARY_PROMPT

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY', 'pet-echo-secret-2026')
CORS(app)

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# In-memory storage (for MVP simplicity)
# In production, this would be a proper database
entries_db = {}

def analyze_pet_emotion(pet_name, pet_species, pet_breed, pet_age, story):
    """Send story to AI and get emotional analysis."""
    
    prompt = PET_EMOTION_ANALYSIS_PROMPT.format(
        story=story,
        pet_name=pet_name,
        pet_species=pet_species,
        pet_breed=pet_breed,
        pet_age=pet_age
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are PetEcho, a warm and insightful pet emotional companion."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"PetEcho is taking a nap right now. Please try again in a moment. 💤"

def generate_weekly_summary(pet_name, pet_species, entries):
    """Generate weekly summary from recent entries."""
    
    entries_text = "\n\n".join([
        f"[{e['date']}] {e['story']}" 
        for e in entries
    ])
    
    prompt = WEEKLY_SUMMARY_PROMPT.format(
        entries=entries_text,
        pet_name=pet_name,
        pet_species=pet_species
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are PetEcho, a warm pet emotional companion."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return "PetEcho is reflecting on the week. Check back soon! 💭"

@app.route('/')
def index():
    """Landing page."""
    return render_template('index.html')

@app.route('/api/journal', methods=['POST'])
def create_entry():
    """Create a new pet diary entry with AI analysis."""
    data = request.json
    
    pet_name = data.get('petName', 'My Pet')
    pet_species = data.get('petSpecies', 'Pet')
    pet_breed = data.get('petBreed', 'Unknown')
    pet_age = data.get('petAge', 'Unknown')
    story = data.get('story', '')
    device_id = data.get('deviceId', 'anonymous')
    
    if not story or len(story.strip()) < 20:
        return jsonify({
            'success': False,
            'error': 'Please share a bit more about your moment with your pet (at least 20 characters).'
        }), 400
    
    entry_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    
    # Generate AI insight
    ai_insight = analyze_pet_emotion(
        pet_name, pet_species, pet_breed, pet_age, story
    )
    
    entry = {
        'id': entry_id,
        'petName': pet_name,
        'petSpecies': pet_species,
        'petBreed': pet_breed,
        'petAge': pet_age,
        'story': story,
        'deviceId': device_id,
        'createdAt': timestamp,
        'moodTags': data.get('moodTags', []),
        'aiInsight': ai_insight
    }
    
    # Store in memory (keyed by device for multi-pet support)
    if device_id not in entries_db:
        entries_db[device_id] = {}
    entries_db[device_id][entry_id] = entry
    
    return jsonify({
        'success': True,
        'entry': {
            'id': entry_id,
            'petName': pet_name,
            'petSpecies': pet_species,
            'story': story,
            'createdAt': timestamp,
            'aiInsight': ai_insight
        }
    })

@app.route('/api/journal/<device_id>', methods=['GET'])
def get_entries(device_id):
    """Get all entries for a device (pet parent)."""
    if device_id not in entries_db:
        return jsonify({'success': True, 'entries': []})
    
    entries = list(entries_db[device_id].values())
    entries.sort(key=lambda x: x['createdAt'], reverse=True)
    
    return jsonify({
        'success': True,
        'entries': entries
    })

@app.route('/api/journal/<device_id>/weekly-summary', methods=['GET'])
def get_weekly_summary(device_id):
    """Get AI-generated weekly summary."""
    if device_id not in entries_db:
        return jsonify({'success': False, 'error': 'No entries found'}), 404
    
    entries = list(entries_db[device_id].values())
    
    # Get last 7 entries
    entries.sort(key=lambda x: x['createdAt'], reverse=True)
    recent = entries[:7]
    
    if len(recent) < 2:
        return jsonify({
            'success': False, 
            'error': 'Share a few more moments to get your weekly insight!'
        }), 400
    
    pet_name = recent[0]['petName']
    pet_species = recent[0]['petSpecies']
    
    summary = generate_weekly_summary(pet_name, pet_species, recent)
    
    return jsonify({
        'success': True,
        'summary': summary,
        'entriesCount': len(recent)
    })

@app.route('/api/moods', methods=['GET'])
def get_mood_options():
    """Get available mood tags for the emotion selector."""
    moods = [
        {'id': 'happy', 'label': 'Happy', 'emoji': '☀️', 'color': '#FFD93D'},
        {'id': 'playful', 'label': 'Playful', 'emoji': '🎾', 'color': '#6BCB77'},
        {'id': 'anxious', 'label': 'Anxious', 'emoji': '😰', 'color': '#C9B1FF'},
        {'id': 'calm', 'label': 'Calm', 'emoji': '🧘', 'color': '#74C0FC'},
        {'id': 'attached', 'label': 'Attached', 'emoji': '💕', 'color': '#FF8787'},
        {'id': 'curious', 'label': 'Curious', 'emoji': '🔍', 'color': '#FFA94D'},
        {'id': 'sleepy', 'label': 'Sleepy', 'emoji': '😴', 'color': '#B197FC'},
        {'id': 'protective', 'label': 'Protective', 'emoji': '🛡️', 'color': '#63E6BE'},
    ]
    return jsonify({'success': True, 'moods': moods})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
