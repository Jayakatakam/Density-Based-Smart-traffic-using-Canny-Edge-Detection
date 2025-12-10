import tkinter as tk
from image_processing import apply_canny
from density_calculation import calculate_density
from signal_controller import get_signal_time

def start_app():
    root = tk.Tk()
    root.title("Density Based Smart Traffic Control")

    label = tk.Label(root, text="Traffic Control System Using Image Processing")
    label.pack()

    def process():
        edges = apply_canny("dataset/traffic_high.jpg")
        density = calculate_density(edges)
        time = get_signal_time(density)
        result.config(text=f"Density: {density} | Green Time: {time}s")

    btn = tk.Button(root, text="Process Image", command=process)
    btn.pack()

    result = tk.Label(root, text="")
    result.pack()

    root.mainloop()
