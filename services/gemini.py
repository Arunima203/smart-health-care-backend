from google import genai

client = genai.GenerativeModel()

genai.configure(api_key=os.getenv("AQ.Ab8RN6Ix8-udDdiNRo8WZ31mUDw9MfZniUyK7M04cy0UrP26Qg"))

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