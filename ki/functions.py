import config as c

import os
from dotenv import load_dotenv
import time
import openai

def initOpenAI(p):

    openai.api_key = os.environ['OPENAI_API_KEY']
    model_engine = "text-davinci-003"
    prompt = p
    completion = openai.Completion.create (
        engine=model_engine, 
        prompt=prompt, 
        max_tokens=1024,
        n=1,
        stop=None, temperature=0.5,
    )
    response = completion.choices[0].text
    response = response.lstrip()
    return response 