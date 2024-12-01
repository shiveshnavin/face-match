import gradio as gr
import face_recognition
import os

def face_match_batch(original_file, threshold, files):
    try:
        if not files or len(files) == 0:
            return {"error": "At least one file is required to match against the original."}

        # Load the original image
        original_image = face_recognition.load_image_file(original_file)
        original_encodings = face_recognition.face_encodings(original_image)

        if len(original_encodings) == 0:
            return {"error": "No face detected in the original image."}

        original_encoding = original_encodings[0]

        response = []

        # Iterate through the files to match
        for file in files:
            try:
                # Load the target image
                target_image = face_recognition.load_image_file(file)
                target_encodings = face_recognition.face_encodings(target_image)

                # Extract the file name from the full path
                file_name = os.path.basename(file)

                if len(target_encodings) == 0:
                    # No face found in the target image
                    response.append({
                        "status": "no_face",
                        "distance": 1.0,
                        "confidence": 0.0,
                        "file": file_name
                    })
                else:
                    # Use the first face encoding from the target image
                    target_encoding = target_encodings[0]

                    # Calculate the distance
                    distance = face_recognition.face_distance([original_encoding], target_encoding)[0]

                    # Confidence percentage
                    confidence = (1 - distance) * 100

                    # Determine match status
                    match_status = "match" if distance <= threshold else "no_match"

                    response.append({
                        "status": match_status,
                        "distance": round(distance, 4),
                        "confidence": round(confidence, 2),
                        "file": file_name
                    })

            except Exception as e:
                response.append({
                    "status": "error",
                    "distance": 1.0,
                    "confidence": 0.0,
                    "file": file_name
                })

        return response

    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}

iface = gr.Interface(
    fn=face_match_batch,
    inputs=[
        gr.File(file_types=[".jpg", ".jpeg", ".png"], type="filepath", label="Original Image"),
        gr.Number(value=0.6, label="Threshold"),
        gr.File(file_types=[".jpg", ".jpeg", ".png"], type="filepath", label="Images to Match", file_count="multiple")
    ],
    outputs="json",
    title="Batch Face Match App",
    description="Upload an original image, set a threshold, and upload multiple images to match against the original."
)

iface.launch(server_name="0.0.0.0")
