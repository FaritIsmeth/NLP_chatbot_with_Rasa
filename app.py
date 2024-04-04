from flask import Flask, render_template, request, jsonify, url_for
from pathlib import Path
import requests

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')


def download_image(image_url, save_folder):
    # Make the directory if it doesn't exist
    Path(save_folder).mkdir(parents=True, exist_ok=True)

    # Define the path for the saved image
    save_path = Path(save_folder) / 'saved.png'

    # Get the image from the URL
    response = requests.get(image_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the image content to the file
        with open(save_path, 'wb') as image_file:
            image_file.write(response.content)
        print(f"Image saved to {save_path}")
    else:
        print(f"Failed to download the image. Status Code: {response.status_code}")

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Response:", rasa_response_json)
    if len(rasa_response_json) == 1:
        get_text = rasa_response_json[0]['text']
        return jsonify({'response': get_text})
    elif len(rasa_response_json) == 2 and 'image' in rasa_response_json[1]:
        get_image_url = rasa_response_json[1]['image']
        return jsonify({"response": '<img src="' + get_image_url + '" alt="image"/>'})
    elif len(rasa_response_json) == 2:
        get_text = rasa_response_json[1]['text']
        return jsonify({'response': get_text})
    else:
        return jsonify({'response': 'Sorry, I could not understand that.'})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
