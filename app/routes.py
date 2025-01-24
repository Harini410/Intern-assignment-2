import spacy
from flask import Blueprint, request, jsonify

nlp = spacy.load("en_core_web_sm")

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
def home():
    return "Welcome to the Customer Data Platform Chatbot!"

@chatbot_bp.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    # Process the question using SpaCy
    doc = nlp(user_question)
    response = generate_response(doc)

    return jsonify({"response": response})

def generate_response(doc):
    # Logic to extract relevant information from the documentation
    # This is a placeholder for the actual implementation
    question_text = doc.text.lower()
    
    # Example logic for handling specific questions
    if "set up a new source" in question_text:
        return "To set up a new source in Segment, go to the Sources section in your dashboard and click on 'Add Source'."
    elif "create a user profile" in question_text:
        return "To create a user profile in mParticle, navigate to the Users section and click on 'Create User'."
    elif "build an audience segment" in question_text:
        return "To build an audience segment in Lytics, go to the Audiences tab and click on 'Create Segment'."
    elif "integrate my data" in question_text:
        return "To integrate your data with Zeotap, follow the integration guide in the documentation."
    else:
        return "I'm sorry, I cannot assist with that question."
