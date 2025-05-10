# Sign Language Recognition and Voice Playback

This Flask application provides a platform to bridge communication gaps by converting **voice to sign** and **text to voice**.

---

## **Features**
1. **Voice to Sign**: Convert spoken words into text and display corresponding signs.
2. **Text to Voice**: Convert input text into voice playback.

---

## **Setup Instructions**

### **1. Prerequisites**
- **Python Version**: Python 3.8 or higher.
- **Required Libraries**:
  - Flask
  - TensorFlow
  - OpenCV
  - gTTS
  - pydub
  - SpeechRecognition
- **Trained Model**: Ensure the trained TensorFlow model (`keras_Model.keras`) is available in the project directory.

---

### **2. Installation**

1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-name
````
project/
│
├── app.py                  # Main Flask application
├── templates/
│   └── 1.html              # Frontend HTML file
├── keras_Model.keras       # Trained TensorFlow model
├── dataset/                # Dataset directory (if retraining is needed)
│   └── train/
│       ├── 0/
│       ├── 1/
│       ├── 2/
│       ├── 3/
│       ├── 4/
│       └── 5/
└── static/                 # Static files (e.g., images for signs)

TO TRAIN THE MODEL USE THIS 

python create_model.py