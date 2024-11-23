import gradio as gr
import face_recognition

def face_match(file1, file2, threshold):
    try:
        # Load the images
        image1 = face_recognition.load_image_file(file1)
        image2 = face_recognition.load_image_file(file2)

        # Encode the faces
        encodings1 = face_recognition.face_encodings(image1)
        encodings2 = face_recognition.face_encodings(image2)

        if len(encodings1) == 0 and len(encodings2) == 0:
            return {"error": "No faces detected in both images."}
        elif len(encodings1) == 0:
            return {"error": "No face detected in the first image."}
        elif len(encodings2) == 0:
            return {"error": "No face detected in the second image."}

        # Use the first face encoding from each image
        face_encoding1 = encodings1[0]
        face_encoding2 = encodings2[0]

        # Calculate the distance
        distance = face_recognition.face_distance([face_encoding1], face_encoding2)[0]

        # Determine match status
        match_status = "match" if distance <= threshold else "no_match"

        return {
            "status": match_status,
            "distance": round(distance, 4),
            "threshold": threshold
        }

    except Exception as e:
        print(e)
        return {"error": f"Unexpected error: {str(e)}"}

iface = gr.Interface(
    fn=face_match,
    inputs=[
        gr.Image(type="filepath", label="Image 1"),
        gr.Image(type="filepath", label="Image 2"),
        gr.Number(value=0.6, label="Threshold")
    ],
    outputs="json",
    title="Face Match App",
    description="Upload two images and set a threshold to check if the faces match."
)

iface.launch(server_name="0.0.0.0")