import cv2
import mediapipe as pipe
import array as arr
import numpy as np
import queue as q
import time


cam0 = cv2.VideoCapture(0)
pipe_hands = pipe.solutions.hands
hands = pipe_hands.Hands()
draw_utils = pipe.solutions.drawing_utils




class Hand_Detection_Module():


    def __init__(self):

        self.landmark_positions = [0]
        self.delta_time = 0
        self.curr_time = 0
        self.hands = hands


    def get_vision(self):

        success, window = cam0.read()  # shape is 640x480
        imgRGB = cv2.cvtColor(window, cv2.COLOR_BGR2RGB)
        return imgRGB


    def detection(self, dist, dept):

        while True:
            frame = self.get_vision()
            res = self.hands.process(frame)

            # RIGHT HAND
            dist.put(res.multi_hand_landmarks)
            dept.put(res)

            # From MP Docs, Ready-to-use part
            with pipe_hands.Hands(
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
                while cam0.isOpened():
                    success, image = cam0.read()
                    if not success:
                        print("Ignoring empty camera frame.")
                        # If loading a video, use 'break' instead of 'continue'.
                        continue

                    # Flip the image horizontally for a later selfie-view display, and convert
                    # the BGR image to RGB.
                    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                    image.flags.writeable = False
                    results = hands.process(image)

                    # Draw the hand annotations on the image.
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            draw_utils.draw_landmarks(
                                image, hand_landmarks, pipe_hands.HAND_CONNECTIONS)
                    cv2.imshow('MediaPipe Hands', image)
                    if cv2.waitKey(5) & 0xFF == 27:
                        break
            cam0.release()

