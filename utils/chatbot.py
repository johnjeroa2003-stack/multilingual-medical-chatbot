from transformers import pipeline

# Load FLAN-T5 model
chatbot_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small",
    framework="pt"
)


def generate_medical_response(user_input):

    user_input = user_input.lower()

    # Fever
    if "fever" in user_input:
        return """
Fever may occur due to viral or bacterial infections.

Precautions:
- Drink plenty of fluids
- Take proper rest
- Eat nutritious food

Consult a doctor if the fever persists for more than 2 days.
"""

    # Headache
    elif "headache" in user_input:
        return """
Headache may occur due to stress, dehydration, or lack of sleep.

Precautions:
- Drink enough water
- Take rest
- Avoid excessive screen time

Consult a doctor if the pain becomes severe.
"""

    # Diabetes
    elif "diabetes" in user_input:
        return """
Common symptoms of diabetes include:
- Increased thirst
- Frequent urination
- Fatigue

Maintain a healthy diet and exercise regularly.

Consult a doctor for diagnosis and treatment.
"""

    # Cold / Cough
    elif "cold" in user_input or "cough" in user_input:
        return """
Cold and cough are commonly caused by viral infections.

Precautions:
- Drink warm fluids
- Take adequate rest
- Avoid cold foods and drinks

Consult a doctor if symptoms worsen.
"""

    # Sneezing
    elif "sneezing" in user_input:
        return """
Sneezing may occur due to allergies, dust exposure, or a common cold.

Precautions:
- Avoid dust and allergens
- Drink sufficient water
- Maintain cleanliness

Consult a doctor if symptoms continue for several days.
"""

    # Stomach Pain
    elif "stomach" in user_input or "abdominal" in user_input:
        return """
Stomach pain may occur due to indigestion, gas, or infection.

Precautions:
- Drink water
- Avoid spicy foods
- Take proper rest

Consult a doctor if pain becomes severe.
"""

    # General AI Response
    else:

        prompt = f"""
You are a medical assistant.

Answer the medical question in simple words.

Include:
- Possible reasons
- Basic precautions
- When to see a doctor

Keep response short and clear.

Question: {user_input}

Answer:
"""

        response = chatbot_pipeline(
            prompt,
            max_length=120,
            do_sample=False
        )

        return response[0]['generated_text']
