import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()


genai.configure(api_key = os.getenv('KEY'))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings=[
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings=safety_settings
)


def ai_compare(doc1, doc2):
    response = model.generate_content(f"Here we are comparing the difference between two documents to find the difference between both the documents. The data from first document is: '{doc1}' and the data from second document is '{doc2}'. Please find the difference and properly explain the differences in both of them.")
    print(response.text)
    return response.text