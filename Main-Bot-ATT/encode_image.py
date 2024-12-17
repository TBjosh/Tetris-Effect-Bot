import os
import base64

# Get the absolute path to the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Dynamically build the path to the image
image_path = os.path.join(script_dir, "Tetris_Effect_Grid.png")

# Print the path to verify
print("Looking for the file at:", image_path)

# Convert the image to Base64
try:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        print("Base64 Encoded String:")
        print(encoded_string.decode("utf-8"))
except FileNotFoundError:
    print("Error: Image file not found. Make sure the file exists in the script directory.")
except Exception as e:
    print(f"Error: {e}")
