import json 
# from decouple import config 
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os


# load environment variables from .env file 
load_dotenv()

# get access to our credentials
# MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
# MISTRAL_MODEL = os.getenv("MISTRAL_MODEL")

def write_section(topic, header, sub_sections, text): 
    
    try:
        SYSTEM_MESSAGE = f"You are a well trained ghostwriter for writing impressive articles about {topic}. Your articles are informative, detailed and well organized and written in a way that is easy to understand by all ages."
        sub_section_text = ''
        
        for sub_section in sub_sections: 
            sub_section_text += f"{sub_section}\n\n"
            
        # Mistral Chat
        mistral_client = MistralClient(api_key = MISTRAL_API_KEY)
        messages = [
            
            ChatMessage(role='system', content=SYSTEM_MESSAGE), 
            ChatMessage(role='system', content=f"previous sections: \n{text}"), 
            ChatMessage(role= 'user', content= f"Write section {header} with sub sections: \n {sub_section_text}"
                                               f"Make sure to use the proper markdown formatting")
            
            ]

        chat_response = mistral_client.chat(
                                            model = MISTRAL_MODEL, 
                                            messages = messages
                                           )
        content = chat_response.choices[0].message.content
        return content
        

        
    except Exception as e:
        print(e)
        return "", ""
    
    
    
def generate_outline(topic, subject): 
    
    try:
        SYSTEM_MESSAGE = f"""You are well trained ghost writer for writing articles about {topic}.
                            Your articles are informative, detailed, well organized 
                            and written in a way that is easy to understand by all ages """
        prompt = f"write an outline for article about {subject}"
        
        mistral_client = MistralClient(api_key=MISTRAL_API_KEY)
        messages = [
            ChatMessage(role='system', content=SYSTEM_MESSAGE),
            ChatMessage(role='system', content= f"{prompt}"
                                             "Make sure to reply with a JSON object with the following format:"
                                             """{
                                                "title": "Example Title",
                                                "sections": [
                                                    {
                                                        "header": "Header Example",
                                                        "sub-sections": [
                                                            {
                                                                "header": "Example Header"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }"""), 
                   ]
        chat_response = mistral_client.chat(model = MISTRAL_MODEL, messages = messages)
        json_response = json.loads(chat_response.choices[0].message.content)
        return json_response
        
        
    except Exception as e:
        print(e)
        return "",""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
