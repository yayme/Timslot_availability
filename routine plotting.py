import matplotlib.pyplot as plt
import numpy as np

# Define time intervals (x-axis)
times = np.arange(9, 22)  # 9 AM to 10 PM

# Define weekdays (y-axis, skipping Monday)
weekdays = [ "Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
weekdays=weekdays[::-1]
# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 5))

# Plot schedule with green highlighting as per request
for i, day in enumerate(weekdays):
    if day == "Friday":
        ax.barh(i, 4.5, left=11.5, color="green", alpha=0.5, label="preferred")# 10 AM - 10 PM
        ax.barh(i, 6, left=16, color="blue", alpha=0.5)
        # ax.barh(i, 12, left=10, color="green", alpha=0.5)
    elif day in ["Monday", "Wednesday"]:  # Shouldn't be included in y-axis
        ax.barh(i, 1, left=11, color="blue", alpha=0.5)  # 11 AM - 12 PM
        ax.barh(i, 1.5, left=13.5, color="blue", alpha=0.5)  # 1:30 PM - 3 PM
        ax.barh(i, 5.5, left=16.5, color="blue", alpha=0.5)
    elif day in ["Thursday"]:
        ax.barh(i, 2.5, left=9.5, color="blue", alpha=0.5, label="also free")  # 9:30 AM - 12 PM
        ax.barh(i, 1.5, left=13.5, color="blue", alpha=0.5)  # 1:30 PM - 3 PM
        ax.barh(i, 5.5, left=16.5, color="blue", alpha=0.5)  # 4:30 PM - 10 PM
    elif day in ["Tuesday"]:
        ax.barh(i, 2.5, left=9.5, color="blue", alpha=0.5)  # 9:30 AM - 12 PM
        ax.barh(i, 1.5, left=13.5, color="blue", alpha=0.5)  # 1:30 PM - 3 PM
        ax.barh(i, 5.5, left=16.5, color="blue", alpha=0.5)  # 4:30 PM - 10 PM

# Formatting the plot
ax.set_yticks(range(len(weekdays)))
ax.set_yticklabels(weekdays)
ax.set_xticks(times)
ax.set_xticklabels([f"{t}:00" for t in times])
ax.set_xlabel("Time of Day Hong kong time")
ax.set_title("Weekday availability, Feb 24- March 7")
ax.legend()
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.show()
