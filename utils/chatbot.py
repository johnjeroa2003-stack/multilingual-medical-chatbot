from transformers import pipeline

# Load model
chatbot_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small",
    framework="pt"
)


def generate_medical_response(user_input):

    user_input = user_input.lower()

    # Fever response
    if "fever" in user_input:
        return """
Fever may occur because of viral infection, flu, or body infection.

Precautions:
- Drink plenty of water
- Take proper rest
- Eat healthy food

Consult a doctor if fever continues for more than 2 days.
"""

    # Headache response
    elif "headache" in user_input:
        return """
Headache can happen because of stress, dehydration, or lack of sleep.

Precautions:
- Drink water
- Take rest
- Avoid too much screen time

Consult a doctor if headache becomes severe.
"""

    # Diabetes response
    elif "diabetes" in user_input:
        return """
Common symptoms of diabetes include:
- Increased thirst
- Frequent urination
- Tiredness

Maintain healthy food habits and regular exercise.

Consult a doctor for proper diagnosis.
"""

    # Cold and cough response
    elif "cold" in user_input or "cough" in user_input:
        return """
Cold and cough are usually caused by viral infections.

Precautions:
- Drink warm water
- Take proper rest
- Avoid cold foods

Consult a doctor if symptoms become severe.
"""

    # General AI response
    else:

        prompt = f"""
        You are a medical assistant chatbot.

        Give short and simple medical advice.

        Question: {user_input}

        Answer:
        """

        response = chatbot_pipeline(
            prompt,
            max_length=150,
            do_sample=False
        )

        return response[0]['generated_text']