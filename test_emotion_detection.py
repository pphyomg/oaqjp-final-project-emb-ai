""" This module is to test the EmotionDetection functionality
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """ Test class for EmotionDetection module """
    def test_emotion_detector(self):
        """ Function to do multiple test cases on emotion_detector function """
        # test case for dominant emotion joy
        test1 = emotion_detector("I am glad this happened")
        self.assertEqual(test1.get('dominant_emotion'), "joy")
        # test case for dominant emotion anger
        test2 = emotion_detector("I am really mad about this")
        self.assertEqual(test2.get('dominant_emotion'), "anger")
        # test case for dominant emotion disgust
        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test3.get('dominant_emotion'), "disgust")
        # test case for dominant emotion sadness
        test4 = emotion_detector("I am so sad about this")
        self.assertEqual(test4.get('dominant_emotion'), "sadness")
        # test case for dominant emotion fear
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test5.get('dominant_emotion'), "fear")

unittest.main()
