import cv2
import mediapipe as mp

class HandGestureDetector:
    """
    Detects hand gestures using MediaPipe Hands:
      👍 Thumbs up  -> Jump
      ✊ Fist       -> Duck
      🖐️ Open palm  -> Idle
    """

    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.gesture = None

    def detect_gesture(self, frame):
        h, w, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)
        gesture = "Idle"

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

                # Landmark indices (see MediaPipe Hands documentation)
                thumb_tip = hand_landmarks.landmark[4]
                thumb_ip = hand_landmarks.landmark[3]
                index_tip = hand_landmarks.landmark[8]
                middle_tip = hand_landmarks.landmark[12]
                ring_tip = hand_landmarks.landmark[16]
                pinky_tip = hand_landmarks.landmark[20]

                # Convert to pixel coordinates
                t_y = int(thumb_tip.y * h)
                ti_y = int(thumb_ip.y * h)
                i_y = int(index_tip.y * h)
                m_y = int(middle_tip.y * h)
                r_y = int(ring_tip.y * h)
                p_y = int(pinky_tip.y * h)

                # --- Gesture Logic ---
                # Thumbs Up: thumb tip above thumb IP, other fingers down
                if (t_y < ti_y) and (i_y > ti_y) and (m_y > ti_y) and (r_y > ti_y) and (p_y > ti_y):
                    gesture = "Jump"

                # Fist: all fingertips close together (down)
                elif abs(i_y - m_y) < 20 and abs(m_y - r_y) < 20 and abs(r_y - p_y) < 20:
                    gesture = "Duck"

                else:
                    gesture = "Idle"

        self.gesture = gesture
        return gesture, frame
