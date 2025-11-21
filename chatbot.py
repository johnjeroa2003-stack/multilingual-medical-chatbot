import traceback

class MedicalChatbot:
    def __init__(self, use_model=False, max_tokens=150):
        self.use_model = use_model
        self.max_tokens = max_tokens
        self.model = None

        if use_model:
            try:
                from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
                model_name = "google/flan-t5-small"
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
                self.model = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)
            except Exception as e:
                print("Could not load HF model. Using fallback.", e)
                traceback.print_exc()
                self.model = None

    def get_response(self, prompt: str) -> str:
        prompt = prompt.strip()
        if not prompt:
            return "Please type a question."

        # Safety filter
        lower = prompt.lower()
        if any(w in lower for w in ["suicide", "kill myself", "self harm", "emergency",
                                    "chest pain", "severe bleeding", "loss of consciousness"]):
            return ("If this is an emergency, please contact local emergency services immediately. "
                    "I cannot assist with urgent or life-threatening issues.")

        # Model response (if enabled)
        if self.model:
            try:
                out = self.model(prompt, max_length=self.max_tokens, do_sample=False)
                return out[0]["generated_text"]
            except:
                pass

        # Fallback rule-based
        return self.rule_based_response(prompt)

    def rule_based_response(self, text: str) -> str:
        q = text.lower()

        # --- Medical definitions ---
        if "cardiology" in q:
            return "Cardiology is the branch of medicine that deals with the heart and blood vessels."

        if "neurology" in q:
            return "Neurology is the branch of medicine that studies the brain, nerves, and nervous system."

        if "diabetes" in q:
            return "Diabetes is a chronic condition where the body cannot regulate blood sugar properly."

        if "bp" in q or "blood pressure" in q:
            return "Blood pressure measures the force of blood against artery walls. Normal is around 120/80 mmHg."

        # --- Common medical symptoms ---
        if any(x in q for x in ["fever", "temperature", "hot", "chills"]):
            return "A fever is commonly caused by infections. Stay hydrated and rest. Seek care if it lasts >48 hours."

        if "headache" in q or "migraine" in q:
            return "Headaches often come from stress or dehydration. Drink water and rest. Seek help if severe."

        if "covid" in q or "coronavirus" in q:
            return "COVID-19 symptoms include fever, cough, and tiredness. Test if suspected and follow medical advice."

        # --- Non-medical general knowledge ---
        if "college" in q:
            return "A college is an educational institution where students pursue higher education after school."

        if "post graduation" in q or "postgraduate" in q:
            return "Post graduation refers to studies done after completing an undergraduate degree (e.g., MSc, MBA)."

        if "what is" in q:
            return f"{text.capitalize()} is something you are asking about. Based on context, it may require more details."

        # Default fallback
        return "Can you provide more details about your question so I can help better?"
