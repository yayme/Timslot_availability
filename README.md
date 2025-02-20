# Time Slot Availability

**Time Slot Availability** is an interactive Python application that allows users to create and manage availability schedules for weekdays. The application offers an easy-to-use interface for defining 30-minute time slots, and the flexibility to toggle availability with a simple mouse click. You can export your customized schedule as an image for sharing or printing.

## Features

- **Interactive UI**: Create availability slots for weekdays (Monday to Friday) with a user-friendly interface built with Tkinter.
- **Custom Time Slots**: Define time slots in 30-minute increments between 9 AM to 10 PM.
- **Toggle Availability**: Click on any time slot to toggle availability between "available" and "unavailable."
- **Export to Image**: Save your schedule as an image (PNG/JPEG) for easy sharing or future reference.

## Files

1. **routine_plotting.py**: Contains the core logic for manually plotting the time slot availability grid.
2. **timeslot_ui.py**: A Tkinter-based UI that allows users to create and modify time slot availability with simple mouse interactions.
3. **timeslot_ui_export.py**: Enhances the UI by adding functionality to export the availability grid as an image.
4. **dist/timeslot_availability.exe**: A compiled desktop application created using PyInstaller, ready for distribution on Windows.
