from transformers import pipeline

# HuggingFace model (fallback or primary)
generator = pipeline("text-generation", model="gpt2")

def generate_response(query, intent):
    if intent in ["savings", "investments", "taxes"]:
        prompt = f"Provide financial advice about {intent}: {query}"
    else:
        prompt = f"General financial guidance: {query}"

    response = generator(prompt, max_length=100)[0]['generated_text']
    return response


