import cv2
import mediapipe as pipe
import array as arr
import numpy as np
import queue as q


cam0 = cv2.VideoCapture(0)
pipe_hands = pipe.solutions.hands
hands = pipe_hands.Hands()
draw_utils = pipe.solutions.drawing_utils


class Hand_Detection_Module():

    def get_vision(self):
        success, window = cam0.read()  # shape is 640x480
        imgRGB = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
        return imgRGB

    def detection(self, dist, dept):

        while True:
            frame = self.get_vision()
            res = hands.process(frame)

            # RIGHT HAND
            dist.put(res.multi_hand_landmarks)
            dept.put(res)
