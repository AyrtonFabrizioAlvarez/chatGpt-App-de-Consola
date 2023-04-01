import openai

openai.api_key = "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"

while True:
    prompt = input("Ingresa tu pregunta crack: ")

    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=4000)
    print("\n\n")

    print(completion.choices[0].text)