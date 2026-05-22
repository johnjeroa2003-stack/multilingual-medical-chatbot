# 🩺 Multilingual Medical Support Chatbot

## 📌 Project Overview

The Multilingual Medical Support Chatbot is an AI-powered healthcare assistance system developed using Streamlit and Hugging Face Transformers.

This chatbot can:

- Detect user language automatically
- Translate non-English queries into English
- Generate medical-related responses using an AI model
- Translate the response back into the user’s original language

The project aims to provide basic healthcare guidance and multilingual medical assistance through a user-friendly web application.

---

# 🚀 Features

✅ Multilingual Support

✅ Automatic Language Detection

✅ Translation to English

✅ AI-Powered Medical Response Generation

✅ Response Translation to User Language

✅ Interactive Streamlit Web Interface

✅ Error Handling

✅ Modular Code Structure

✅ Beginner-Friendly Architecture

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Application UI |
| Hugging Face Transformers | AI Model Integration |
| FLAN-T5 | Medical Response Generation |
| Deep Translator | Language Translation |
| LangDetect | Language Detection |
| PyTorch | Backend Framework |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```bash
medical-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── chatbot.py
│   ├── translator.py
│   └── language_detector.py
│
├── notebooks/
│   └── fine_tuning.ipynb
│
└── data/
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2: Navigate to Project Folder

```bash
cd medical-chatbot
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Application

```bash
streamlit run app.py
```

---

# 🔄 Project Workflow

```text
User Input
   ↓
Language Detection
   ↓
Translation to English
   ↓
Medical AI Response Generation
   ↓
Translate Response Back
   ↓
Display Final Output
```

---

# 🌍 Supported Languages

The chatbot supports multiple languages including:

- English
- Tamil
- Hindi
- French
- Spanish
- German
- And many more...

---

# 🧠 AI Model Used

## FLAN-T5 Small

The project uses the FLAN-T5 Small model from Hugging Face for generating medical-related responses.

Model Link:
https://huggingface.co/google/flan-t5-small

---

# 📊 Dataset Information

The project references medical QA datasets such as:

- MedQuAD
- PubMedQA
- HealthCareMagic

These datasets are commonly used for healthcare-related NLP tasks.

---

# ⚠️ Disclaimer

This chatbot is for educational purposes only and should NOT be considered a substitute for professional medical advice, diagnosis, or treatment.

---

# 📌 Future Improvements

- Voice-based interaction
- Doctor appointment integration
- Medical report analysis
- Chat history storage
- Advanced healthcare recommendations

---

# 👨‍💻 Author

Johnson Jerald

---

# 📜 License

This project is developed for educational and learning purposes.