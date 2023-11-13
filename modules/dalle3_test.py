import openai
openai.api_key = "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"
response = openai.Image.create(
  prompt="working in kitchen",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
#image_url = response['data'][0]['url']