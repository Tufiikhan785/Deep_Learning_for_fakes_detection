# import tkinter as tk
# from PIL import Image, ImageTk
# import cv2
# import tensorflow as tf

# # Load your TensorFlow model
# model = tf.keras.models.load_model('E:\Models and validation\model.h5')

# # Create a Tkinter window
# window = tk.Tk()
# window.title("Video Classification")
# window.geometry("800x600")

# # Function to process the input video
# def process_video():
#     # Open the video file
#     video_path = filedialog.askopenfilename(filetypes=[("E:\Models and validation\real (4)", "*.mp4")])
#     video_capture = cv2.VideoCapture(video_path)

#     # Process each frame of the video
#     while True:
#         # Read the frame
#         ret, frame = video_capture.read()

#         if not ret:
#             break

#         # Preprocess the frame (resize, normalize, etc.)
#         # Your preprocessing code goes here

#         # Perform inference using your TensorFlow model
#         predictions = model.predict(frame)

#         # Display the result on the screen
#         # Your code to display the result goes here

#     # Release the video capture and destroy any OpenCV windows
#     video_capture.release()
#     cv2.destroyAllWindows()

# # Function to display the result on the screen
# def display_result():
#     # Your code to display the result goes here

# # Create a "Browse" button to select the input video
#   browse_button = tk.Button(window, text="Select Video", command=process_video)
#   browse_button.pack(pady=10)

# # Create a "Show Result" button to display the result
# result_button = tk.Button(window, text="Show Result", command=display_result)
# result_button.pack(pady=10)

# # Run the Tkinter event loop
# window.mainloop()
import tkinter as tk
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk
import cv2
import tensorflow as tf
# Load your TensorFlow model
model = tf.keras.models.load_model('E:/Models and validation/model.h5')

# Create a Tkinter window
window = tk.Tk()
window.title("Video Classification")
window.geometry("800x600")

# Function to process the input video
# Function to process the input video
def process_video():
    # Open the video file
    video_path = filedialog.askopenfilename(filetypes=[("E:/Models and validation/real (4)", "*.mp4")])
    video_capture = cv2.VideoCapture(video_path)

    # Process each frame of the video
    while True:
        # Read the frame
        ret, frame = video_capture.read()

        if not ret:
            break

        # Preprocess the frame (resize, normalize, etc.)
        resized_frame = cv2.resize(frame, (224, 224))  # Resize frame to (224, 224)
        normalized_frame = resized_frame / 255.0  # Normalize frame values between 0 and 1

        # Reshape the frame for model input
        input_frame = tf.expand_dims(normalized_frame, axis=0)  # Add batch dimension
        input_frame = tf.cast(input_frame, tf.float32)  # Convert to float32

        # Perform inference using your TensorFlow model
        predictions = model.predict(input_frame)

        # Display the result on the screen
        # Your code to display the result goes here

    # Release the video capture and destroy any OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Function to display the result on the screen
def display_result():
    # Your code to display the result goes here

# Create a "Browse" button to select the input video
 browse_button = tk.Button(window, text="Select Video", command=process_video)
 browse_button.pack(pady=10)

# Create a "Show Result" button to display the result
result_button = tk.Button(window, text="Show Result", command=display_result)
result_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
