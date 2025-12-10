import numpy as np

def calculate_density(edge_img):
    white_pixels = np.sum(edge_img > 0)
    return white_pixels
