import cv2
import pyautogui
import time
from src.detector import HandGestureDetector

def main(camera_index=0):
    detector = HandGestureDetector(max_hands=1)
    cap = cv2.VideoCapture(camera_index)

    print("🎮 Gesture-Based Dino Game Controller Started!")
    print("➡️  👍  Thumbs Up = Jump")
    print("➡️  ✊  Fist = Duck")
    print("➡️  🖐️  Open Palm = Idle/Run")
    print("Press 'Q' to quit.\n")
    time.sleep(2)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gesture, annotated = detector.detect_gesture(frame)

        # Game control mapping
        if gesture == "Jump":
            pyautogui.press("space")
        elif gesture == "Duck":
            pyautogui.keyDown("down")
        else:
            pyautogui.keyUp("down")

        cv2.putText(
            annotated, f"Gesture: {gesture}", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )
        cv2.imshow("Dino game gesture control (press Q to exit)", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
