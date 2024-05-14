import os
import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib

def extract_features(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hog = cv2.HOGDescriptor()
	features = hog.compute(gray)
	return features.flatten()

def load_images_from_directory(directory):
    images = []
    labels = []
    class_names = []
    for class_name in os.listdir(directory):
        class_dir = os.path.join(directory, class_name)
        for filename in os.listdir(class_dir):
            img_path = os.path.join(class_dir, filename)
            image = cv2.imread(img_path)
            if image is not None:
                images.append(extract_features(image))
                labels.append(class_name)
                class_names.append(class_name)
    return images, labels, class_names

directory = 'pics/resized'
images, labels, class_names = load_images_from_directory(directory)

# Convert data to numpy arrays
X = np.array(images)
y = np.array(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
# Scale features (optional but recommended for SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)

# Save the trained SVM classifier to a file using joblib
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)  # Create the 'models' directory if it doesn't exist
model_filename = os.path.join(model_dir, 'svm_classifier.joblib')
joblib.dump(svm_classifier, model_filename)

# Make predictions
y_pred_svm = svm_classifier.predict(X_test)

# Evaluate accuracy
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy SVM:", accuracy_svm * 100)

input_image = cv2.imread('image1_mango-tree.jpg')

if input_image is not None:
    input_features = extract_features(input_image).reshape(1,-1)
    svm_pred = svm_classifier.predict(input_features)[0]

    print("SVM PRED:", svm_pred)
else:
    print("Error unable to read input image")

