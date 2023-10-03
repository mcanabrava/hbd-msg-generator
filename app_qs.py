from flask import Flask, request, jsonify
import configparser
import openai

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('creds.cfg')
openai.api_key = config['creds']['api_key']

# Sample data to simulate a database of birthday messages
birthday_messages = []

# Define your get_completion function here
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9,
    )
    return response.choices[0].message["content"]

@app.route('/birthday-messages', methods=['POST'])
def create_birthday_message():
    # Retrieve query parameters from the URL
    friend_name = request.args.get('friend_name', 'Friend')
    relationship_type = request.args.get('relationship_type', 'relationship')
    words = request.args.getlist('words')  # Use getlist to retrieve multiple values
    max_words = request.args.get('max_words', 100)
    style = request.args.get('style', 'poem')
    language = request.args.get('language', 'en')

    prompt = f"Today is the birthday of my friend {friend_name}, which is my {relationship_type}. Generate a happy birthday message with the words from the following list: {words} and maximum {max_words} characters. Write the text like a {style} and in the {language} language."

    # Call get_completion to generate the message
    generated_message = get_completion(prompt)
    
    # Add the generated message to the list of birthday messages (simulating storage)
    birthday_messages.append(generated_message)
    
    # Return the generated message as the API response
    return jsonify({"message": generated_message.strip()}), 201  # Use 201 Created status code

@app.route('/birthday-messages', methods=['GET'])
def get_birthday_messages():
    # Return a list of all birthday messages (simulated database)
    return jsonify({"messages": birthday_messages})

if __name__ == "__main__":
    app.run(debug=True)
