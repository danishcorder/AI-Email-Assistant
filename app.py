from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import nltk
import re
import json
from text_processor import TextProcessor

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Initialize text processor
text_processor = TextProcessor()

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/api/rewrite', methods=['POST'])
def rewrite_text():
    try:
        data = request.get_json()
        original_text = data.get('text', '')
        tone = data.get('tone', 'formal')
        
        if not original_text.strip():
            return jsonify({'error': 'Text cannot be empty'}), 400
        
        # Process the text based on tone
        rewritten_text = text_processor.process_text(original_text, tone)
        
        return jsonify({
            'original': original_text,
            'rewritten': rewritten_text,
            'tone': tone,
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tones', methods=['GET'])
def get_available_tones():
    tones = {
        'formal': 'Professional business language',
        'friendly': 'Warm and conversational tone',
        'urgent': 'Concise and action-oriented',
        'marketing': 'Persuasive and benefit-focused'
    }
    return jsonify(tones)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
