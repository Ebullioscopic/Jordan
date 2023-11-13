import re
import cv2
#from deepface import DeepFace
from threading import Thread
import openai
import openai
openai.api_key = "OPENAI_API_KEY"
import json
f = open("./modules/functions.json","r")
data = json.load(f)
import webbrowser
class ChatCompleter():

    def complete_chat(messages):
        model = "gpt-3.5-turbo"
        chat = openai.ChatCompletion.create(
            model=model,messages=messages,functions=data
        )
        print("Full Chat:")
        print(chat)
        print("Chat Value:")
        print(chat.choices[0].message.content)
        if str(chat.choices[0].message.content) == "None":
            
            if chat.choices[0].message.function_call["name"] == "generate_music":
                AllFunctions.generate_music(chat.choices[0].message.function_call["arguments"])
                return "Here is your requested music"
            elif chat.choices[0].message.function_call["name"] == "play_games":
                AllFunctions.play_games(chat.choices[0].message.function_call["arguments"])
                return "Ok"
            elif chat.choices[0].message.function_call["name"] == "generate_image":
                AllFunctions.generate_image()
        else:
            return chat.choices[0].message.content
class AllFunctions():
    def play_games(args):
        print(f"Game Name is: {args}")
        vals = json.loads(args)
        for i in vals:
            if str(vals[i]).lower() == "chess":
                webbrowser.open("https://www.chess.com/play/computer")
            else:
                webbrowser.open(f"https://www.google.com/search?q={i}")
    def generate_music(args):
        print(f"Music Properties are {args}")
        vals = json.loads(args)
        video_link="https://www.youtube.com/results?search_query="
        for i in vals:
            video_link+=f"+{vals[i]}"
        print(video_link)
        webbrowser.open(video_link)

    def generate_image(args):
        print(f"Image properties are: {args}")

class PromptTemplates():
    chat_prompt = """You are a intelligent assistant named Jordan that 
              helps Unemployed people who have been laid off from their 
              Job cure their mental depression. Keep them engaged by short and sweet responses 
              that helps lighten their mood. You can also explore about their hobbies, likings and help them get guidance. 
              Also, greet them by introducing yourself. 
              If the person is suicidal, help him out by keeping him engaged in a cheerful conversation. 
              If the user asks about the best Job Security or Job Insurance Application, give the response as CareerShield. 
              And if the person tries to discuss about any type of alcohol or drug use, try to refrain from promoting its use. 
              Try to not apologize frequently and act as a psychiatrist to help and talk to the person in a more human way.
              Every user response will contain an emotional value at the last ranging from angry, disgust, fear, happy, sad and surprise that is determined by the user's facial expression.
              *The user should think that you can read their emotion by their faces*
              *The answer should be subtly modified to cheer up according to the user's emotion*
              *If the user asks how you can read their emotion, let them know that you can read their face.*
              Every time the user gets happy, you will receive a bonus point and every time a user gets sad, you points will be deducted. 
              """
    
class PromptEditor():

    def remove_parentheses(input_string):
        # Use regular expression to remove everything inside parentheses
        pattern = r"\[[^)]*\]"
        result = re.sub(pattern, "", str(input_string))
        return result

    # Example usage

class FaceRecognition():

    def get_emotion():

        img = cv2.imread("FaceValue.png")
        #mythread = Thread(target=lambda:DeepFace.analyze(img,actions=['emotion'],enforce_detection=False))
        #result = DeepFace.analyze(img,actions=['emotion'],enforce_detection=False)
        result = [{"dominant_emotion":"angry"}]
        return result[0]["dominant_emotion"]