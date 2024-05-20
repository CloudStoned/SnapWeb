import cv2
import numpy as np
from rembg import remove 
from skimage.feature import hog

class ImagePreProcessor:
    # def for_saving(self, file_stream):
    #     try:
    #         filestr = file_stream.read()
    #         npimg = np.frombuffer(filestr, np.uint8)
    #         img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    #         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #         return gray_img

    #     except Exception as e:
    #         print(f"Error processing image: {e}")
    #         return None 
    def rsize_rbg(self,img_data):
        if img_data is not None:
            resized_image = cv2.resize(img_data, (170, 200), fx=0.1, fy=0.1)
            removed_bg_image = remove(resized_image)
            gray_image = cv2.cvtColor(removed_bg_image, cv2.COLOR_BGR2GRAY)

            print(f"Preprocess Successful for {img_data}")
            return gray_image
        else:
            print(f"Failed to read {img_data}")
            return None
        
    def normalize_image(self, image):
        img_data = (image * 255).astype(np.uint8)
        return img_data

    def for_pred_hog(self, image):
        norm_img = self.normalize_image(image)
        
        hog_features, _ = hog(
            norm_img,
            orientations=3,
            pixels_per_cell=(6, 6),
            cells_per_block=(2, 2),
            block_norm='L2-Hys',
            visualize=True,
            transform_sqrt=True,
            feature_vector=True
        )
        return hog_features

    
    def preprocess_img(self,image ):
        if image is not None:
            grayimg = self.rsize_rbg(image)
            preprocess_img = self.for_pred_hog(grayimg)
            return preprocess_img
        else:
            print("Image is None, cannot extract HOG features")
            return None

    def for_predicting(self, file_stream):
        try:
            nparr = np.frombuffer(file_stream.read(), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if img is not None:
                hog_features = self.preprocess_img(img)
                return hog_features
    
            else:
                print("Error: Image could not be decoded.")
                return None
            
        except Exception as e:
            print(f"Error processing image for predicting: {e}")
            return None

