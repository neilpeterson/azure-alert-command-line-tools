# import openai

# openai.api_key = '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'

# prompt = 'Return date from three weeks ago'

# response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=5)

# print(response)

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omittedc
    api_key='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'
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)