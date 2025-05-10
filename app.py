from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os
import speech_recognition as sr

app = Flask(__name__)

# Load the full TensorFlow model
model = tf.keras.models.load_model("keras_Model.keras")
print("Keras model loaded successfully.")

# Load the labels for sign representation
labels_path = "labels.txt"
if os.path.exists(labels_path):
    with open(labels_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    print(f"Loaded {len(classes)} labels from {labels_path}.")
else:
    print(f"Error: {labels_path} not found.")
    exit()

@app.route('/')
def index():
    return render_template('1.html')

# Voice to Text and Sign
@app.route('/voice_to_text', methods=['POST'])
def voice_to_text():
    recognizer = sr.Recognizer()

    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Listening for voice input...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds

        # Recognize speech using Google Web Speech API
        recognized_text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {recognized_text}")

        # Initialize lists for character GIFs and word images
        sign_gifs = []
        word_images = []

        # Check for word-level images in the filtered_data directory
        words = recognized_text.split()
        for word in words:
            word_image_path = f"static/filtered_data/{word.lower()}.webp"
            if os.path.exists(word_image_path):
                word_images.append(f"/{word_image_path}")
            else:
                print(f"No image found for word: {word}")

        # Check for character-level GIFs in the alphabet directory
        for char in recognized_text:
            if char.isalnum():  # Only process alphanumeric characters
                gif_path = f"static/alphabet/{char.lower()}_small.gif"  # Convert to lowercase and append '_small'
                if os.path.exists(gif_path):
                    sign_gifs.append(f"/{gif_path}")  # Add the GIF URL
                else:
                    print(f"No GIF found for character: {char}")

        return jsonify({'text': recognized_text, 'sign_gifs': sign_gifs, 'word_images': word_images})
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand the audio.'}), 400
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
        return jsonify({'error': 'Speech recognition service failed.'}), 500
    except Exception as e:
        print(f"Error processing voice input: {e}")
        return jsonify({'error': 'Failed to process voice input.'}), 500

@app.route('/text_sign_to_voice', methods=['POST'])
def text_sign_to_voice():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided.'}), 400

    try:
        # Generate voice for the provided text
        tts = gTTS(text=text, lang='en')
        print("Generating voice for text...")
        tts.write_to_fp(temp_audio := tempfile.SpooledTemporaryFile())
        temp_audio.seek(0)
        audio = AudioSegment.from_file(temp_audio, format="mp3")
        play(audio)

        return jsonify({'message': 'Text converted to voice successfully.'})
    except Exception as e:
        print(f"Error generating voice: {e}")
        return jsonify({'error': 'Failed to convert text to voice.'}), 500


