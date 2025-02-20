import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog

# Define time slots and weekdays
times = np.arange(9, 22, 0.5)  # 9 AM to 10 PM in 30-minute increments
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekdays.reverse()

# Initialize availability grid (0: unavailable, 1: available)
availability = np.zeros((len(weekdays)+1, len(times)))

def toggle_slot(event):
    """Handles slot selection on click."""
    global availability
    ax = event.inaxes
    if ax is None:
        return  # Click was outside the plot

    x, y = int(event.xdata), int(event.ydata)
    if 0 <= x < len(times) and 0 <= y < len(weekdays):
        availability[y, x] = 1 - availability[y, x]  # Toggle availability
        update_plot()

def update_plot():
    """Redraws the availability grid."""
    ax.clear()
    ax.set_xticks(np.arange(len(times)))
    ax.set_xticklabels([f"{int(t)}:{'30' if t % 1 else '00'}" for t in times], rotation=45)
    ax.set_yticks(np.arange(len(weekdays)) + 1)
    ax.set_yticklabels(weekdays)
    ax.set_xlabel("Time of Day")
    ax.set_title("Click to Toggle Availability")
    ax.grid(True)

    # Draw grid
    for i in range(len(weekdays)):
        for j in range(len(times)):
            color = "green" if availability[i, j] else "white"
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color, edgecolor="black"))

    canvas.draw()

def export_image():
    """Saves the current plot as an image."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if file_path:
        fig.savefig(file_path)
        print(f"Image saved as {file_path}")

# Create Tkinter window
root = tk.Tk()
root.title("Availability Scheduler")

# Create Matplotlib figure
fig, ax = plt.subplots(figsize=(10, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create Export button
export_button = tk.Button(root, text="Export Image", command=export_image)
export_button.pack(pady=10)

# Bind mouse click event
fig.canvas.mpl_connect("button_press_event", toggle_slot)
update_plot()

# Run Tkinter event loop
root.mainloop()
