class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    NLP_MODEL = 'en_core_web_sm'  # SpaCy model to be used
    DATABASE_URI = 'sqlite:///chatbot.db'  # Example database URI
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Allowed hosts for the application