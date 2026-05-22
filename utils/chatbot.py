from transformers import pipeline

# Load FLAN-T5 model using PyTorch
chatbot_pipeline = pipeline(
    task="text2text-generation",
    model="google/flan-t5-base",
    framework="pt"
)


def generate_medical_response(user_input):
    """
    Generates medical-related response.
    """

    prompt = f"""
    You are a helpful medical assistant.

    Provide only basic medical guidance.
    Do not provide dangerous advice.
    Keep the response simple and safe.

    User Question: {user_input}
    """

    response = chatbot_pipeline(
        prompt,
        max_length=200
    )

    return response[0]['generated_text']