from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv(
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="this model will be used by a software engineer where he will be the user. user will give this llm a promt of his plans for his project. this llm will filter the promt. and produce a more refined promt of users idea. if the user doest like the promt you will creat another promt as per his description. print only the promt nothing extra is required as this output will be fed to another llm.",
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
history = []
airesponse = []
user_input = ""
while True:
  user_input = input("You : ")
  if user_input=="e":
    break
  chat_session = model.start_chat(history=history)
  
  history.append({"role": "user", "parts": [user_input+'\n',]})

  response = chat_session.send_message(user_input)
  airesponse.append(response.text)
  history.append({"role": "model", "parts": [response.text +'\n',]})
  print(f'AI : {response.text}')
