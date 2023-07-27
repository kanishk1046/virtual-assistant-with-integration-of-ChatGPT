import os
import openai
from config import apikey


openai.api_key = apikey


try:
  response = openai.Completion.create(
      model="text-davinci-003",
      prompt="write an email to my boss for resignation\n",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
  print(response)
except Exception as e:
  print("An error occurred:", e)

