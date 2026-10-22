""" Flask backend server to bridge the functions to the web interface.
"""

# import libraries
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """ This function outputs the dictionary of the emotion and covert it
        into a string format and return.
    """
    # retrieve text input from the html
    text_to_analyze = request.args.get("textToAnalyze")
    # get the result by passing emotion_detector function
    response = emotion_detector(text_to_analyze)
    # get dominant_emotion value only
    dominant_emotion = response.get("dominant_emotion")
    # copy response dictionary without dominant emotion key
    remove_dominant_response = {k: v for k, v in response.items() if k != "dominant_emotion"}
    # covert the dictionary into list
    convert_list = [f"'{k}': {v}" for k, v in remove_dominant_response.items()]
    # join the items in the list into string without the last item 'sadness'
    output = ", ".join(convert_list[:-1])

    return f"For the given statement, the system response is {output} and " \
        f"{convert_list[-1]}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def index():
    """ Default return page for http GET """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
