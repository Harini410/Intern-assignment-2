# Chatbot Project

This project is a Flask-based chatbot that answers "how-to" questions related to Customer Data Platforms (CDPs) such as Segment, mParticle, Lytics, and Zeotap. It utilizes SpaCy for natural language processing to understand user queries.

## Project Structure

```
chatbot-project
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models
│   │   └── __init__.py
│   ├── static
│   └── templates
│       └── index.html
├── requirements.txt
├── README.md
└── config.py
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd chatbot-project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python app/main.py
   ```

5. **Access the chatbot:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage Guidelines

- Users can ask "how-to" questions related to the specified CDPs.
- The chatbot will process the queries and provide relevant answers based on the trained model.

## Dependencies

- Flask
- SpaCy

## Future Enhancements

- Implement more advanced NLP features.
- Expand the knowledge base for more comprehensive answers.
- Add user authentication and logging features.