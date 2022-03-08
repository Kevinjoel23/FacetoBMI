import face_recognition
import joblib
import numpy as np

def get_face_encoding(image_path):
    picture_of_me = face_recognition.load_image_file(image_path)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)
    if not my_face_encoding:
        print("no face found !!!")
        return np.zeros(128).tolist()
    return my_face_encoding[0].tolist()

def predict_BMI(test_image,bmi_model):
    test_array = np.expand_dims(np.array(get_face_encoding(test_image)),axis=0)
    bmi = np.asscalar(np.exp(bmi_model.predict(test_array)))
    return bmi

def predict_fat(BMI, gender, age):
    fat_percentage = ((1.20*BMI) + (0.23*age) - (10.8*gender) - 5.4)
    return fat_percentage
