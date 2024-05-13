from openai import OpenAI
class LLMClient:
	def __init__(self, url):#"http://192.168.1.94:1234/v1"
		self.OPENAIclient = OpenAI(base_url=url, api_key="lm-studio")

	#SystemMessage = "You are a helpfulAI"
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