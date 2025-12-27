# Quizzler-Tkinter-Quiz-App-API-Powered-
Quizzler is a desktop-based quiz application built with **Python** and **Tkinter**.   Instead of using hardcoded questions, the app dynamically fetches **True/False questions** from the **Open Trivia Database API**, providing a fresh quiz experience every time.

This project focuses on:
- API integration
- Object-Oriented Programming (OOP)
- GUI development with Tkinter
- Real-time user interaction and feedback

---

## 🚀 Features

- ✅ Fetches 50 True/False questions from Open Trivia Database API
- 🎨 Modern Tkinter UI using `Canvas`, image-based buttons, and labels
- 🧠 Object-oriented architecture (`Question`, `QuizBrain`, `QuizInterface`)
- 📊 Live score tracking
- 🟥🟩 Instant visual feedback for correct/incorrect answers
- 🧾 Handles HTML entities in API responses
- 🪟 Popup message when the quiz is finished
- 🔒 Buttons automatically disabled after quiz completion

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Requests** (API calls)
- **Open Trivia Database API**
- **HTML entity handling** via `html` module

---

## 📡 API Used

Questions are fetched from:


The API returns quiz data in JSON format, which is parsed and converted into Python objects at runtime.

---

## 📁 Project Structure
├── main.py # Entry point
├── data.py # API call and question data preparation
├── question_model.py # Question class
├── quiz_brain.py # Quiz logic and state management
├── ui.py # Tkinter user interface
├── images/
│ ├── true.png
│ └── false.png


---

## ▶️ How It Works

1. Questions are fetched from the Open Trivia Database API.
2. Each question is converted into a `Question` object.
3. `QuizBrain` manages question flow, scoring, and answer validation.
4. `QuizInterface` handles the UI, user input, and feedback.
5. When the quiz ends, a popup message is displayed and buttons are disabled.

---

## 🖥️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/quizzler.git
pip install requests
python main.py

! Important
To load photos, you need to enter the image file path in the `#load images` section of the UI code. Pay attention to the "\" escape sequence. You can write 'r' to make it a raw file, or use the backslash "/".






