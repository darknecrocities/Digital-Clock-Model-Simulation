
# ⏰ Digital Clock Simulation using Processing (Python Mode)

## 📘 Introduction
This project simulates a **real-time digital clock** using the Processing IDE in Python mode. It visually models a seven-segment digital display and updates in real-time using Python's `datetime` module.

---

## 🎯 Objectives
- 🕒 Simulate a real-time digital clock showing hours, minutes, and seconds.
- 🔢 Model a **seven-segment display** using geometric shapes.
- 🎨 Practice **graphical modeling** and basic animation in Processing.
- ⏱️ Manage and update time using Python’s `datetime` library.

---

## 🛠️ Tools and Environment
- **Processing IDE** (Python Mode) – for graphical rendering and animation.
- **Python datetime module** – for real-time clock data.
- 🚫 No external libraries used – everything built from scratch.

---

## 🧠 Methodology

### 1. 🔲 Seven-Segment Display Modeling
- Each digit (0-9) uses a bitmask to define which segments are on.
- Each segment is a polygon drawn from vertex coordinates.
- Segment mapping corresponds to top, upper-right, lower-right, bottom, lower-left, upper-left, and middle.

### 2. 🖼️ Graphical Rendering in Processing
- `draw_digit()` activates segments per digit using filled polygons.
- `draw_segment()` uses Processing’s `beginShape()` / `endShape()` to render each segment.
- `draw_colon()` displays separators using ellipses.

### 3. 🧩 Layout and Scaling
- Digits spaced with scaling factors and offsets.
- Ensures centered and proportionate layout.

### 4. ⏳ Time Acquisition and Update
- `datetime.now()` fetches system time.
- Zero-padded strings ensure consistent two-digit display.
- `draw()` loop updates once per second (`frameRate(1)`).

---

## ✅ Results
- A real-time **digital clock** simulation with accurate updates.
- Seven-segment digits are **clear, proportional, and aligned**.
- Updates every second to reflect current time.

---

## 🚧 Challenges
- Manual design of segment shapes and coordinates.
- Ensuring proper **spacing** and **layout** of digits and colons.
- Synchronizing Processing’s frame rate with system time.

---

## 🏁 Conclusion
This project showcases how **manual graphical modeling** and real-time simulation can be achieved using just the Processing IDE and Python's built-in tools. It emphasizes time management, mathematical modeling, and interactive design.

---

> Created with ❤️ using Processing + Python
