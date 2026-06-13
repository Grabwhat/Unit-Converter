# Unit Converter (HTML/CSS/JavaScript + Flask)

A simple and lightweight unit converter web application built using **HTML, CSS, JavaScript** for the frontend and **Flask (Python)** for backend logic. This project demonstrates basic full-stack integration and unit conversion handling through a web interface.

---

## Features

- Convert between common units (length, weight, temperature, etc.)
- Simple and responsive user interface
- Frontend validation using JavaScript
- Backend processing using Flask
- Clean and minimal design for easy use
- Lightweight and fast

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **Templating Engine:** Jinja2 (Flask default)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/unit-converter.git
cd unit-converter
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
```
Activate it:

## Windows:
```bash
venv\Scripts\activate
```

## macOS/Linux:
```bash
source venv/bin/activate
```
### 3. Run the Flask app
```bash
flask run --debug
```

### 4. Open in browser
```bash
http://127.0.0.1:5000/
```
---
### How It Works
- User enters a value and selects units in the frontend.
- JavaScript handles input validation and sends data to Flask.
- Flask processes the conversion logic.
- Result is returned and displayed on the page.
---
