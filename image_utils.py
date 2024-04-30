import cv2
import numpy as np

class ImageProcessor:
    def process_image(self, file_stream):
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

