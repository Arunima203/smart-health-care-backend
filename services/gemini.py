from google import genai

client = genai.Client(api_key="AQ.Ab8RN6J6xceaVPhf_1i-OWrWufkRXMLrnXVkNwYuQgCoWSZbLQ")
print("Gemini client created successfully")
def get_health_advice(symptoms,language):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are an expert AI doctor.

Reply ONLY in {language} language.

Patient symptoms:
{symptoms}

Give:

1. Possible Disease
2. First Aid
3. Medicine Suggestion
4. Emergency Level
"""
)
    
    return response.text