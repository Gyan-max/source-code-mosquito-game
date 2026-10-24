import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision
from settings import *
import numpy as np
import os

# Path to the hand landmarker model
_MODEL_PATH = os.path.join(os.path.dirname(__file__), "hand_landmarker.task")

BaseOptions = mp_python.BaseOptions
HandLandmarker = mp_vision.HandLandmarker
HandLandmarkerOptions = mp_vision.HandLandmarkerOptions
RunningMode = mp_vision.RunningMode


class HandTracking:
    def __init__(self):
        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=_MODEL_PATH),
            running_mode=RunningMode.IMAGE,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )
        self.hand_landmarker = HandLandmarker.create_from_options(options)
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False

    def scan_hands(self, image):
        # Flip horizontally (selfie view) and convert BGR -> RGB
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        self.results = self.hand_landmarker.detect(mp_image)

        self.hand_closed = False

        if self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                # Landmark 9 = middle finger MCP (palm center proxy)
                lm9 = hand_landmarks[9]
                self.hand_x = int(lm9.x * SCREEN_WIDTH)
                self.hand_y = int(lm9.y * SCREEN_HEIGHT)

                # Landmark 12 = middle finger tip; if tip y > base y => closed
                lm12 = hand_landmarks[12]
                if lm12.y > lm9.y:
                    self.hand_closed = True

        return image  # return BGR frame (consistent with original)

    def get_hand_center(self):
        return (self.hand_x, self.hand_y)

    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_hand_closed(self):
        pass
