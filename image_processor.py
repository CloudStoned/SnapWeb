import cv2
import numpy as np

class ImagePreProcessor:
    def for_saving(self, file_stream):
        try:
            # Read the image in memory using NumPy from the file stream
            filestr = file_stream.read()
            npimg = np.frombuffer(filestr, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

            # Convert to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            return gray_img

        except Exception as e:
            print(f"Error processing image: {e}")
            return None 
    
    def extract_features(self, image):
        try:
            # Convert image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Compute HOG features
            hog = cv2.HOGDescriptor()
            features = hog.compute(gray)
            return features.flatten()
        except Exception as e:
            print(f"Error extracting features: {e}")
            return None
        
    def for_predicting(self, file_stream):
        try:
            # Read the file stream using OpenCV
            nparr = np.frombuffer(file_stream.read(), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img is not None:
                # Extract features from the image
                features = self.extract_features(img)
                return features
            else:
                print("Error: Image could not be decoded.")
                return None
            
        except Exception as e:
            print(f"Error processing image for predicting: {e}")
            return None
