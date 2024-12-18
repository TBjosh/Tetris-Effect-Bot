import cv2
import numpy as np
import mss
import pygetwindow as gw
import time

# Load templates for Tetriminos
TEMPLATES = {
    "I": cv2.imread("templates/I_piece.png", cv2.IMREAD_GRAYSCALE),
    "O": cv2.imread("templates/O_piece.png", cv2.IMREAD_GRAYSCALE),
    "T": cv2.imread("templates/T_piece.png", cv2.IMREAD_GRAYSCALE),
    "L": cv2.imread("templates/L_piece.png", cv2.IMREAD_GRAYSCALE),
    "J": cv2.imread("templates/J_piece.png", cv2.IMREAD_GRAYSCALE),
    "S": cv2.imread("templates/S_piece.png", cv2.IMREAD_GRAYSCALE),
    "Z": cv2.imread("templates/Z_piece.png", cv2.IMREAD_GRAYSCALE),
}

# Function to match templates and recognize the active piece
def recognize_piece(frame, templates):
    best_match = None
    highest_score = 0

    for piece_name, template in templates.items():
        result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > highest_score:
            highest_score = max_val
            best_match = piece_name

    if highest_score > 0.8:  # Confidence threshold
        return best_match
    return None

# Capture the game window
def capture_window(region):
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        frame = np.array(screenshot)
        return cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

# Main function
def main():
    print("Looking for Tetris® Effect: Connected window...")
    game_region = find_game_window("Tetris® Effect: Connected")

    if not game_region:
        print("Exiting: Game window not found.")
        return

    print("Game window found. Starting capture...")
    capture_region = {
        "top": game_region["top"],
        "left": game_region["left"],
        "width": game_region["width"],
        "height": game_region["height"]
    }

    try:
        while True:
            # Capture the grayscale frame
            frame = capture_window(capture_region)

            # Recognize the active piece
            current_piece = recognize_piece(frame, TEMPLATES)

            if current_piece:
                print(f"Active piece detected: {current_piece}")
            else:
                print("No active piece detected.")

            # Display the frame for debugging
            cv2.imshow("Tetris Detection - Grayscale", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting detection...")
                break

    except KeyboardInterrupt:
        print("Interrupted. Closing capture...")
    finally:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
