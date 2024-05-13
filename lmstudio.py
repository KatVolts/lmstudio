from openai import OpenAI
class LLMClient:
	def __init__(self, url):#"http://192.168.1.94:1234/v1"
		self.OPENAIclient = OpenAI(base_url=url, api_key="lm-studio")

	#SystemMessage = "You are a helpful AI"
	#Prompt = "meowmeow"
	#messageHistory = [
	#   {"role": "system", "content": SystemMessage},
	#   {"role": "user", "content": Prompt}
	#  ]
	def queryLLM(self, messageHistory, temp):
		
		completion = self.OPENAIclient.chat.completions.create(
		  model="local-model", # this field is currently unused
		  messages = messageHistory,		
		  temperature=temp  
		)
		return completion.choices[0]#.message.content

class LLMEClient:
	def __init__(self, url, model):#"http://192.168.1.94:1234/v1"
		self.OPENAIclient = OpenAI(base_url=url, api_key="lm-studio")
		self.model = model

	def get_embedding(self, text):#"nomic-ai/nomic-embed-text-v1.5-GGUF"):
	   text = text.replace("\n", " ")
	   return self.OPENAIclient.embeddings.create(input = [text], model=self.model)

#print(get_embedding("Once upon a time, there was a cat."))