from cvzone.ClassificationModule import Classifier
import cv2

# url="http://192.168.232.16"
cap = cv2.VideoCapture(0)
classifier = Classifier("C:/Users/apraj/OneDrive/Desktop/MINI PROJECT/converted_keras (1)/keras_model.h5","C:/Users/apraj/OneDrive/Desktop/MINI PROJECT/converted_keras (1)/labels.txt")

while True:

    _, img = cap.read()
    pred =classifier.getPrediction(img)
    print(pred)
    cv2.imshow("image",img)
    if cv2.waitKey(2) & 0xff == ord('a'):
        break
   
    
    