from Gemini_planning_promt_filtering import airesponse
from dotenv import load_dotenv
import os
import google.generativeai as genai


#getting the last airesponse
last = len(airesponse)
responseai = airesponse[last-1]

load_dotenv()
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
  system_instruction="the input of this model will be a filtered prompt of the ideas of a software engineers project.create a plan for the user including the major functionalities pf that project the parts of the project and the total plan of carrying out the project",
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
history = []
majorfunc = []
while True:

  chat_session = model.start_chat(history=history)
  history.append({"role": "user", "parts": [responseai+'\n',]})

  response = chat_session.send_message(responseai)
  majorfunc.append(response.text)
  plan = response.text
  history.append({"role": "model", "parts": [response.text +'\n',]})
  print(f'AI : {plan}')
  break
file = open("plan.csv" , "w")
file.write(plan)
file.close()