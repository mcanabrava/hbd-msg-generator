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
def get_birthday_messages():
    # Return a list of all birthday messages (simulated database)
    return jsonify({"messages": birthday_messages})

if __name__ == "__main__":
    app.run(debug=True)




