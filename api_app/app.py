"""
app.py

This module contains a Flask application for generating birthday messages using OpenAI's GPT-3 model.
"""

from flask import Flask, request, jsonify
from flask_limiter import Limiter
import configparser
import openai
import time
from functools import wraps
from functions import *

app = Flask(__name__)
limiter = Limiter(app)

config = configparser.ConfigParser()
config.read('creds.cfg')
openai.api_key = config['creds']['api_key']

config.read('auth.cfg')
authorized_api_keys = set(config['api_keys'].values())

# Sample data to simulate a database of birthday messages
birthday_messages = []

# Defining custom error message for rate limit
@limiter.request_filter
def custom_response(limiter, error):
    """
    Custom response handler for rate limiting errors.

    Args:
        error: The rate limiting error.

    Returns:
        flask.Response: A JSON response with a rate limit exceeded message and status code 429.
    """
    response = jsonify({
        "error": "Rate limit exceeded. Please try again later.",
    })
    return response, 429

@app.route('/birthday-messages', methods=['POST'])
@limiter.limit("2 per minute")
@throttle(1)  # Throttle to x request per second
def create_birthday_message():
    """
    Create a birthday message based on user input.

    Returns:
        flask.Response: A JSON response with the generated birthday message or an error message.
    """
    # Verify the API key in the request headers
    api_key = request.headers.get('Authorization')

    if api_key not in authorized_api_keys:
        return jsonify({"error": "Unauthorized"}), 401  # 401 Unauthorized

    data = request.get_json()
    
    friend_name = data.get('friend_name', 'John')
    relationship_type = data.get('relationship_type', 'Work Colleague')
    words = data.get('words', [])
    max_words = data.get('max_words', 100)
    style = data.get('style', 'poem')
    language = data.get('language', 'english')

    prompt = f"Today is the birthday of my friend {friend_name}, which is my {relationship_type}. Generate a happy birthday message with the words from the following list: {words} and maximum {max_words} characters. Write the text like a {style} and in the {language} language."

    # Call get_completion to generate the message
    generated_message = get_completion(prompt)

    # Check if the message generation was successful
    if generated_message:
        # Message generation successful
        birthday_messages.append(generated_message)
        return jsonify({"message": generated_message}), 201  # 201 Created
    else:
        # Handle the case where message generation failed
        return jsonify({"error": "Message generation failed"}), 500  # 500 Internal Server Error

@app.route('/birthday-messages', methods=['GET'])
@throttle(1)  # Throttle to x request per second
def get_birthday_messages():
    """
    Get a list of all birthday messages.

    Returns:
        flask.Response: A JSON response with a list of birthday messages.
    """
    # Verify the API key in the request headers
    api_key = request.headers.get('Authorization')

    if api_key not in authorized_api_keys:
        return jsonify({"error": "Unauthorized"}), 401  # 401 Unauthorized

    # Return a list of all birthday messages (simulated database)
    return jsonify({"messages": birthday_messages})

if __name__ == "__main__":
    app.run(debug=True)




