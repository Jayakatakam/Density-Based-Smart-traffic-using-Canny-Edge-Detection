import cv2

def apply_canny(image_path):
    img = cv2.imread(image_path, 0)
    blur = cv2.GaussianBlur(img, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges
