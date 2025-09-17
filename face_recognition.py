import face_recognition

# --- Step 1: Load known images and encode faces ---
# Load an image of a known person
known_image_path = "known_person.jpg"  # Replace with your image file
try:
    known_image = face_recognition.load_image_file(known_image_path)
    known_face_encodings = face_recognition.face_encodings(known_image)
    if not known_face_encodings:
        print(f"No face found in {known_image_path}. Please check the image.")
        exit()
    known_face_encoding = known_face_encodings[0]  # Assuming one prominent face
except FileNotFoundError:
    print(f"Error: {known_image_path} not found. Please provide a valid path.")
    exit()

# --- Step 2: Load an unknown image and encode its faces ---
# Load an image with an unknown person to compare
unknown_image_path = "unknown_person.jpg"  # Replace with your image file
try:
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_face_encodings = face_recognition.face_encodings(unknown_image)
    if not unknown_face_encodings:
        print(f"No face found in {unknown_image_path}. Please check the image.")
        exit()
    unknown_face_encoding = unknown_face_encodings[0]  # Assuming one prominent face
except FileNotFoundError:
    print(f"Error: {unknown_image_path} not found. Please provide a valid path.")
    exit()

# --- Step 3: Compare faces ---
# Compare the known face encoding with the unknown face encoding
# The 'compare_faces' function returns a list of booleans indicating if each unknown face matches any of the known faces.
results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

# --- Step 4: Interpret results ---
if results[0]:
    print("It's a match! The unknown person is the known person.")
else:
    print("No match found. The unknown person is different from the known person.")
    
    print("the project is to be completed %")
