import openai
openai.api_key = "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"
from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="Hi there!")