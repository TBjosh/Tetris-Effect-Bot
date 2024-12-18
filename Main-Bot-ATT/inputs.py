import pyautogui

def make_move(best_column, rotations):
    for _ in range(rotations):
        pyautogui.press('up')  # Rotate piece
    if best_column > 0:
        for _ in range(best_column):
            pyautogui.press('right')  # Move right
    elif best_column < 0:
        for _ in range(abs(best_column)):
            pyautogui.press('left')  # Move left
    pyautogui.press('space')  # Hard drop
