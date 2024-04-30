import numpy as np
import cv2

def pre_process_image(file_stream, save_path):
    """
    Process the image file to convert it to grayscale and save it.

    Parameters:
    - file_stream: File stream of the uploaded image.
    - save_path: Path where the grayscale image should be saved.
    """
    
    # Read the image in memory using NumPy from the file stream
    filestr = file_stream.read()
    npimg = np.frombuffer(filestr, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(save_path, gray_img)
