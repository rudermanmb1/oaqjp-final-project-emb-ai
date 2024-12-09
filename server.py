'''module providing missing documentation'''
#import flask module components
from flask import Flask, request, render_template
#import emotion detector function
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def send_detector():
    '''retrieves and outputs emotion detection
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotion_str = "For the given statement, the system response is 'anger': "
    emotion_str += str(f"{response['anger']}, 'disgust': {response['disgust']}, ")
    emotion_str += str(f"'fear':{response['fear']}, 'joy':{response['joy']}")
    emotion_str += str(f"and 'sadness': {response['sadness']}.  The dominant ")
    emotion_str += str(f"emotion is {response['dominant_emotion']}.")

    return emotion_str

@app.route("/")
def render_index_page():
    '''Renders the index html file when app is deployed
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
