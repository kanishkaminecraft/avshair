import math
import time
import tkinter as tk
from tkinter import ttk
import threading
import tkinter.font as tkFont

def total_hair_in_scalp(circumference, hair_density):
    radius = circumference / (2 * math.pi)
    surface_area = 2 * math.pi * radius**2
    total_hairs = surface_area * hair_density
    return total_hairs

class HairCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hair Counter")

        # Use the Play font if installed
        self.font = tkFont.Font(family="Play", size=12)
        self.answer_font = tkFont.Font(family="Play", size=40, weight="bold")

        self.label1 = tk.Label(root, text="Enter the circumference of the scalp (in cm):", font=self.font)
        self.label1.pack(pady=10)

        self.circumference_entry = tk.Entry(root, font=self.font)
        self.circumference_entry.pack(pady=5)

        self.label2 = tk.Label(root, text="Enter the total hair in 1 cm square area:", font=self.font)
        self.label2.pack(pady=10)

        self.hair_density_entry = tk.Entry(root, font=self.font)
        self.hair_density_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", font=self.font, command=self.start_process)
        self.submit_button.pack(pady=20)

        self.progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=20)

        self.step_label = tk.Label(root, text="", font=self.font)
        self.step_label.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=self.font)
        self.result_label.pack(pady=10)

    def start_process(self):
        try:
            circumference = float(self.circumference_entry.get())
            hair_density = int(self.hair_density_entry.get())
            self.progress['maximum'] = 100
            self.result_label.config(text="")
            self.step_label.config(text="")
            self.progress['value'] = 0
            threading.Thread(target=self.process_hairs, args=(circumference, hair_density)).start()
        except ValueError:
            self.result_label.config(text="Please enter valid numbers.")

    def process_hairs(self, circumference, hair_density):
        steps = [
            "Calculating the radius:",
            "Radius = Circumference / (2 * π)",
            f"Radius = {circumference:.2f} / (2 * π)",
            f"Radius ≈ {circumference / (2 * math.pi):.2f} cm",
            "Calculating the surface area of the scalp (hemisphere):",
            "Surface Area = 2 * π * Radius^2",
            f"Surface Area = 2 * π * {circumference / (2 * math.pi):.2f}^2",
            f"Surface Area ≈ {2 * math.pi * (circumference / (2 * math.pi))**2:.2f} cm²",
            "Calculating the total number of hairs:",
            "Total Hairs = Surface Area * Hair Density",
            f"Total Hairs ≈ {2 * math.pi * (circumference / (2 * math.pi))**2 * hair_density:.0f} hairs"
        ]

        step_delay = 0.5  # Time delay for each step in seconds
        fade_steps = 5  # Number of fade steps for each message

        for i in range(101):
            if i % (100 // len(steps)) == 0 and i // (100 // len(steps)) < len(steps):
                step_index = i // (100 // len(steps))
                for fade in range(fade_steps):
                    alpha = fade / fade_steps
                    fade_color = f'#{int(255 * (1 - alpha)):02x}{int(255 * (1 - alpha)):02x}{int(255 * (1 - alpha)):02x}'
                    self.step_label.config(text=steps[step_index], fg=fade_color)
                    self.root.update_idletasks()
                    time.sleep(step_delay / fade_steps)
            time.sleep(0.01)  # Simulating processing time
            self.progress['value'] = i
            self.root.update_idletasks()

        # Final calculation and result display
        radius = circumference / (2 * math.pi)
        surface_area = 2 * math.pi * radius**2
        total_hairs = surface_area * hair_density
        result_text = f"Total number of hairs in the scalp: "
        self.result_label.config(text=result_text)
        
        # Show the integer answer separately with the larger font size
        answer_label = tk.Label(self.root, text=f"{total_hairs:.0f} hairs", font=self.answer_font)
        answer_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HairCounterApp(root)
    root.mainloop()
