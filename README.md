# Multilingual Medical Chatbot (Beginner-friendly)

## What this project contains
- `app.py` - Streamlit frontend
- `chatbot.py` - Chat logic (loads HF model `google/flan-t5-small` if `use_model` is enabled)
- `translator.py` - Simple translation wrapper using `googletrans` (optional)
- `requirements.txt` - Python packages (see note on torch)
- `README.md` - This file

## Quick setup (Windows, recommended)
1. Create a fresh virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install packages (except torch):
   ```bash
   pip install -r requirements.txt
   ```

3. Install PyTorch (CPU-only recommended on Windows). Example for many setups:
   ```bash
   pip install torch==2.2.0+cpu torchvision==0.17.0+cpu --index-url https://download.pytorch.org/whl/cpu
   ```
   If you prefer GPU/CUDA, follow the official guide: https://pytorch.org/get-started/locally/

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Notes & Troubleshooting
- If you get `ImportError: DLL load failed while importing _C`, it typically means PyTorch was installed incorrectly or the wheel doesn't match your Python version (e.g., Python 3.11). Installing the CPU wheel above or using Python 3.10 usually fixes it.
- The app falls back to a rule-based responder if a model can't be loaded.
- This project is for educational/demo purposes and **not** a substitute for medical advice.

## Customization ideas
- Replace `google/flan-t5-small` with a quantized local model for faster inference.
- Add a knowledge base (CSV/JSON) and simple retrieval for higher-quality answers.
- Add user authentication and logging for analytics (be careful with PHI).
