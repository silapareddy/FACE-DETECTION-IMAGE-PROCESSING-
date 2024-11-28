import cv2
import mediapipe as mp
import os

def function_1(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))

def function_2(image_name):
    if not os.path.exists(image_name):
        return False
    if not function_1(image_name):
        return False
    return True

def function_3(image_name):
    function_2(image_name)
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    face_detection = mp_face_detection.FaceDetection()

    image = cv2.imread(image_name)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_image)

    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
    output_path = "output.jpg"
    cv2.imwrite(output_path, image)
    return True

def function_4():
    files = [file for file in os.listdir() if function_1(file)]
    return files

def function_5(image_name):
    if function_2(image_name):
        image = cv2.imread(image_name)
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        output_path = "grayscale_output.jpg"
        cv2.imwrite(output_path, grayscale_image)
        return output_path
    return False

def main():
    image_name = input("Enter the image name: ").strip()
    if function_2(image_name):
        output_path = function_3(image_name)
        print("Face detection completed. Output saved.")
    else:
        print("File not found")

if __name__ == "__main__":
    main()
