import re
import random
from typing import Dict, List

class TextProcessor:
    def __init__(self):
        # Tone transformation rules and patterns
        self.tone_transformations = {
            'formal': {
                'greetings': ['Dear', 'Good day', 'Greetings'],
                'closings': ['Best regards', 'Sincerely', 'Yours faithfully'],
                'transitions': ['Furthermore', 'Moreover', 'Additionally', 'In conclusion'],
                'fillers_to_remove': ['um', 'uh', 'like', 'you know', 'basically', 'actually'],
                'style_adjustments': {
                    'contractions': False,
                    'casual_language': False,
                    'exclamation_marks': False
                }
            },
            'friendly': {
                'greetings': ['Hi', 'Hello', 'Hey there', 'Good to hear from you'],
                'closings': ['Best', 'Cheers', 'Take care', 'Looking forward to hearing from you'],
                'transitions': ['Also', 'By the way', 'Speaking of which', 'On another note'],
                'fillers_to_remove': ['um', 'uh'],
                'style_adjustments': {
                    'contractions': True,
                    'casual_language': True,
                    'exclamation_marks': True
                }
            },
            'urgent': {
                'greetings': ['Hello', 'Hi', 'Attention'],
                'closings': ['Urgently required', 'Immediate action needed', 'Time-sensitive'],
                'transitions': ['Immediately', 'Right away', 'As soon as possible', 'ASAP'],
                'fillers_to_remove': ['um', 'uh', 'like', 'you know', 'basically', 'actually', 'perhaps', 'maybe'],
                'style_adjustments': {
                    'contractions': False,
                    'casual_language': False,
                    'exclamation_marks': True
                }
            },
            'marketing': {
                'greetings': ['Dear valued customer', 'Hello', 'Hi there'],
                'closings': ['Don\'t miss out', 'Act now', 'Limited time offer', 'Best value for you'],
                'transitions': ['Moreover', 'Additionally', 'What\'s more', 'But wait', 'Here\'s the best part'],
                'fillers_to_remove': ['um', 'uh', 'like', 'you know', 'basically', 'actually'],
                'style_adjustments': {
                    'contractions': True,
                    'casual_language': True,
                    'exclamation_marks': True
                }
            }
        }
        
        # Common email templates and phrases
        self.email_phrases = {
            'requests': {
                'formal': 'I would like to request your assistance with',
                'friendly': 'Could you help me with',
                'urgent': 'I need immediate assistance with',
                'marketing': 'We have an exclusive opportunity for you to'
            },
            'appreciations': {
                'formal': 'Thank you for your time and consideration',
                'friendly': 'Thanks so much for',
                'urgent': 'Thank you for your prompt attention to this matter',
                'marketing': 'We appreciate your business and'
            }
        }

    def process_text(self, text: str, tone: str) -> str:
        """Process and rewrite text based on the specified tone"""
        if tone not in self.tone_transformations:
            raise ValueError(f"Unsupported tone: {tone}")
        
        # Clean and prepare the text
        cleaned_text = self._clean_text(text)
        
        # Apply tone-specific transformations
        rewritten_text = self._apply_tone_transformations(cleaned_text, tone)
        
        # Apply final formatting
        formatted_text = self._apply_formatting(rewritten_text, tone)
        
        return formatted_text

    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Fix common issues
        text = re.sub(r'\.{2,}', '...', text)  # Fix multiple dots
        text = re.sub(r'\s*\.\s*', '. ', text)  # Fix spacing around periods
        
        return text

    def _apply_tone_transformations(self, text: str, tone: str) -> str:
        """Apply tone-specific transformations to the text"""
        transformation_rules = self.tone_transformations[tone]
        
        # Split into sentences for processing
        sentences = re.split(r'(?<=[.!?])\s+', text)
        processed_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                # Apply tone-specific modifications
                modified_sentence = self._modify_sentence(sentence.strip(), transformation_rules, tone)
                processed_sentences.append(modified_sentence)
        
        return ' '.join(processed_sentences)

    def _modify_sentence(self, sentence: str, rules: Dict, tone: str) -> str:
        """Modify individual sentences based on tone rules"""
        # Remove filler words
        for filler in rules['fillers_to_remove']:
            sentence = re.sub(r'\b' + re.escape(filler) + r'\b', '', sentence, flags=re.IGNORECASE)
            sentence = re.sub(r'\s+', ' ', sentence).strip()
        
        # Handle contractions based on tone
        if not rules['style_adjustments']['contractions']:
            # Convert contractions to full form for formal tone
            contractions = {
                "I'm": "I am", "you're": "you are", "he's": "he is", "she's": "she is",
                "it's": "it is", "we're": "we are", "they're": "they are",
                "I'll": "I will", "you'll": "you will", "he'll": "he will",
                "she'll": "she will", "we'll": "we will", "they'll": "they will",
                "I've": "I have", "you've": "you have", "we've": "we have",
                "they've": "they have", "can't": "cannot", "won't": "will not",
                "don't": "do not", "doesn't": "does not", "didn't": "did not",
                "isn't": "is not", "aren't": "are not", "wasn't": "was not",
                "weren't": "were not", "haven't": "have not", "hasn't": "has not",
                "hadn't": "had not", "shouldn't": "should not", "wouldn't": "would not",
                "couldn't": "could not", "mustn't": "must not"
            }
            for contraction, full_form in contractions.items():
                sentence = re.sub(r'\b' + re.escape(contraction) + r'\b', full_form, sentence, flags=re.IGNORECASE)
        else:
            # Convert some formal phrases to contractions for friendly/marketing tones
            contractions_reverse = {
                "I am": "I'm", "you are": "you're", "he is": "he's",
                "she is": "she's", "it is": "it's", "we are": "we're",
                "they are": "they're", "do not": "don't", "cannot": "can't",
                "will not": "won't"
            }
            for full_form, contraction in contractions_reverse.items():
                sentence = re.sub(r'\b' + re.escape(full_form) + r'\b', contraction, sentence, flags=re.IGNORECASE)
        
        # Add tone-appropriate punctuation
        if rules['style_adjustments']['exclamation_marks']:
            # Add enthusiasm where appropriate
            if any(word in sentence.lower() for word in ['great', 'excellent', 'amazing', 'wonderful']):
                sentence = sentence.rstrip('.') + '!'
        
        return sentence

    def _apply_formatting(self, text: str, tone: str) -> str:
        """Apply final formatting based on tone"""
        rules = self.tone_transformations[tone]
        
        # Capitalize first letter of each sentence
        sentences = re.split(r'(?<=[.!?])\s+', text)
        formatted_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                # Capitalize first letter
                formatted_sentence = sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper()
                formatted_sentences.append(formatted_sentence.strip())
        
        formatted_text = ' '.join(formatted_sentences)
        
        # Add tone-appropriate greeting if it looks like an email start
        if self._looks_like_email_start(formatted_text):
            greeting = random.choice(rules['greetings'])
            if not formatted_text.lower().startswith(tuple(g.lower() for g in rules['greetings'])):
                formatted_text = f"{greeting}, {formatted_text}"
        
        # Add appropriate closing if it looks like an email end
        if self._looks_like_email_end(formatted_text):
            closing = random.choice(rules['closings'])
            if not formatted_text.lower().endswith(tuple(c.lower() for c in rules['closings'])):
                formatted_text = f"{formatted_text}\n\n{closing}"
        
        return formatted_text

    def _looks_like_email_start(self, text: str) -> bool:
        """Check if text looks like the beginning of an email"""
        email_start_indicators = ['i would', 'i am', 'i need', 'i want', 'could you', 'please', 'thank you', 'regarding']
        return any(indicator in text.lower() for indicator in email_start_indicators)

    def _looks_like_email_end(self, text: str) -> bool:
        """Check if text looks like the end of an email"""
        email_end_indicators = ['thank you', 'look forward', 'appreciate', 'regards', 'sincerely', 'best']
        return any(indicator in text.lower() for indicator in email_end_indicators)
