import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import base64
from io import BytesIO
from PIL import Image
import time

# Preprocess the image
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    value_channel = hsv[:, :, 2]
    combined = cv2.addWeighted(gray, 0.5, value_channel, 0.5, 0)
    blurred = cv2.GaussianBlur(combined, (5, 5), 0)
    return blurred

# Detect edges using Canny Edge Detection
def detect_edges(preprocessed_image, t1=50, t2=150):
    edges = cv2.Canny(preprocessed_image, threshold1=t1, threshold2=t2)
    return edges

# Capture game window dynamically
def get_game_window(title="Tetris® Effect: Connected"):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]  # Return the first match
    return None

# Main function
def main():
    print("Looking for the Tetris® Effect: Connected game window...")
    time.sleep(3)

    while True:
        # Find and update the game window dynamically
        game_window = get_game_window()
        if not game_window:
            print("Game window not found. Retrying...")
            time.sleep(1)
            continue

        try:
            GAME_REGION = (game_window.left, game_window.top, game_window.width, game_window.height)
            frame = pyautogui.screenshot(region=GAME_REGION)
            frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

            # Process the frame
            preprocessed = preprocess_image(frame)
            edges = detect_edges(preprocessed)

            # Display results
            cv2.imshow("Edges", edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting...")
                break

            time.sleep(0.01)  # Slight delay to optimize CPU usage
        except Exception as e:
            print(f"Error: {e}")

    cv2.destroyAllWindows()

# Run the script
if __name__ == "__main__":
    main()