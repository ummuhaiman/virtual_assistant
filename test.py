import cv2
import numpy as np
from keras.models import load_model
import tkinter as tk
from PIL import Image, ImageTk

# Load the pre-trained deep learning model
model = load_model('model_file_30epochs.h5')

# Create a Tkinter window
window = tk.Tk()
window.title("Emotion Detector")

# Create a canvas for displaying the video stream
canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()

# Create a label for displaying the predicted emotion
label = tk.Label(window, font=('Arial', 16))
label.pack()

# Start capturing video from the default camera
video = cv2.VideoCapture(0)

# Create a Haar Cascade classifier object for face detection
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define a dictionary that maps emotion labels to integer values
labels_dict = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Neutral', 5:'Sad', 6:'Surprise'}

def update():
    # Read a frame from the video stream
    ret, frame = video.read()
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = faceDetect.detectMultiScale(gray, 1.3, 3)

        for x, y, w, h in faces:
            # Crop the face region from the grayscale frame
            sub_face_img = gray[y:y+h, x:x+w]

            # Resize the cropped face to the required size
            resized = cv2.resize(sub_face_img, (48, 48))

            # Normalize the resized face pixel values to the range [0, 1]
            normalize = resized / 255.0

            # Reshape the normalized face to match the input shape of the deep learning model
            reshaped = np.reshape(normalize, (1, 48, 48, 1))

            # Use the model to predict the emotion on the face
            result = model.predict(reshaped)

            # Get the index of the predicted emotion with the highest probability
            label_idx = np.argmax(result, axis=1)[0]

            # Display the predicted emotion label
            label.config(text=labels_dict[label_idx])

            # Draw a rectangle around the detected face on the original color frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)

            # Convert the color frame to a PIL Image
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Display the image on the Tkinter canvas
            canvas_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=tk.NW, image=canvas_img)
            canvas.image = canvas_img

        # Schedule the next update after 10 milliseconds
        window.after(10, update)

# Schedule the first update
window.after(0, update)

# Start the Tkinter event loop
window.mainloop()

# Release the video capture resources
video.release()