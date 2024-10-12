import os

import google.generativeai as genai
from google.generativeai.types.safety_types import normalize_safety_settings, HarmBlockThreshold

def configureApiKey():
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        print("Error: GEMINI_API_KEY environment variable is not set.")
    else:
        genai.configure(api_key=api_key)

def trainingSet() -> str:
    with open("training_set.txt", "r") as f:
        return f.read()

def conditionTip(user_input : str) -> str:
    configureApiKey()
    model = genai.GenerativeModel("gemini-1.5-flash")
    examples = trainingSet()

    task = f"""Perform a task that replaces x with a particular string.
    Here are some examples:
    {examples}
    Here is the user input: {user_input},
    Generate output without any additional string"""

    # Set safety settings to BLOCK_NONE for all harm categories
    safety_settings = normalize_safety_settings(HarmBlockThreshold.BLOCK_NONE)

    response = model.generate_content(
        task,
        safety_settings=safety_settings,
        stream=False
    )

    return response.text

