
try:
    from kivymd.app import MDApp 
    from kivymd.uix.button import MDFlatButton
    from kivy.uix.screenmanager import ScreenManager as MDScreenManager
    from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, OptionProperty, NumericProperty, ListProperty
    from kivymd.uix.screen import MDScreen
    from kivy.uix.screenmanager import NoTransition
    from kivy.lang import Builder
    from kivy.core.text import LabelBase
    from modified_widgets import *
    from kivy.core.window import Window
    from kivymd.uix.snackbar import MDSnackbar
    from kivymd.uix.label import MDLabel
    from threading import Thread
    import speech_recognition as sr
    from kivy.uix.camera import Camera
    from kivymd.uix.button import MDFloatingActionButton
    from kivymd.uix.label import MDLabel
    from kivymd.uix.dialog import MDDialog
    #Window.size = (350,580)
    import os
    from kivy.clock import Clock, mainthread
    #from langchain import ConversationChain
    from googletrans import Translator
    from functions import *
    from kivy.uix.image import Image
    from kivymd_extensions.akivymd.uix.navigationrail import AKNavigationrail, AKNavigationrailCustomItem, AKNavigationrailItem
    import json
except:
    from traceback import format_exc
    from kivy.app import App
    from kivy.uix.textinput import TextInput
    class BackupApp(App):
        def build(self):
            print(format_exc())
            return TextInput(text=str(format_exc()))
    BackupApp().run()

class Wallpaper(Image):
    source='./resources/images/wallpaper.jpeg'
    opacity = 0.5

#screen manager class
class Manager(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()
    
    def change_screen(self,name):
        self.current = name


#login screen class
class LoginScreen(MDScreen):
    
    username = StringProperty("")
    password = StringProperty("")

    def validate(username, password):
        pass

#sign up screen class
class RegisterScreen(MDScreen):
    name = StringProperty("")
    username = StringProperty("")
    password = StringProperty("")

#main screen class
class MainScreen(MDScreen):
    pass

#loading the widgets
Builder.load_file("modified_widgets.kv")
Builder.load_file("main.kv")


#app class
class SocksApp(MDApp):

    dest_language = "en"
    src_language = "en"
    last_answer = ""
    chatview_id = None
    ai_query = ""
    emotion = ""
    camera = None
    wallpaper = Wallpaper()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager = Manager(transition=NoTransition())
        self.loading_animation = LoadingAnimation()
        self.messages = [ {"role": "system", "content": PromptTemplates.chat_prompt} ]
        f = open("./modules/functions.json","r")
        self.functions = json.load(f)
        self.wallpaper = Wallpaper()
        self.speech_request = SpeechRequest()
        self.dialog = MDDialog(
            title="Didn't quite catch it",
            text="Wanna Try again?",
            buttons=[
                MDFlatButton(
                    text="NO",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=lambda x: self.dialog.dismiss(),
                ),
                MDFlatButton(
                    text="YES",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_press=lambda x: self.listen(self.chatview_id),
                ),
            ],
        )
    @mainthread
    def open_speech_request(self):
        self.speech_request.open()

    @mainthread
    def dowork(self):
        Clock.schedule_once(lambda x: Thread(target=lambda: self.close_speech_request()).start())
        Clock.schedule_once(lambda x: Thread(target=lambda: self.start_loading_animation()).start())

    @mainthread
    def start_loading_animation(self):
        Clock.schedule_once(lambda dt: self.loading_animation.open())
        #Clock.schedule_once(lambda dt: self.stop_loading_animation(), 1.5)


    @mainthread
    def close_speech_request(self):
        self.speech_request.dismiss()

    def process_data(self):
        self.start_intro_loading_animation()

    def start_intro_loading_animation(self):
        Clock.schedule_once(lambda dt: self.loading_animation.open())
        Clock.schedule_once(lambda dt: self.stop_intro_loading_animation(), 1)

    def stop_intro_loading_animation(self):
        Clock.schedule_once(lambda dt: self.loading_animation.dismiss())
        Clock.schedule_once(lambda dt: self.show_snackbar())

    def change_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def set_camera_id(self, widget):
        if not self.camera:
            self.camera = widget
        print(f"Set Camera ID:{self.camera}")
    def set_response_id(self, parent_id):
        if not self.chatview_id:
            self.chatview_id = parent_id
        print("Set Reponse ID: "+str(self.chatview_id))

    @mainthread
    def stop_loading_animation(self):
        Clock.schedule_once(lambda dt: self.loading_animation.dismiss())
        Clock.schedule_once(lambda dt: Thread(target=self.speak()).start(), 0.2)
        
    def speak(self):
        pass

    def takeCommand(self):
     
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)
    
        try:
            Thread(target=lambda: self.dowork()).start()
            print("Recognizing...")   
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            Clock.schedule_once(lambda x: self.stop_loading_animation())
            Clock.schedule_once(lambda x: self.dialog.open())
            return None
        
        print(query)
        self.ai_query = query
        Thread(target=lambda: self.get_response_without_objects()).start()
        print("Dismissed")


    def listen(self,val):
        #Clock.schedule_once(lambda x: self.speech_request.open())
        self.open_speech_request()
        print("GUI func executed")
        if self.dialog:
            self.dialog.dismiss()
        #thread0.start()
        thread1 = Thread(target=lambda: self.takeCommand())
        Clock.schedule_once(lambda x: thread1.start())
        print("Thread1")
        #thread1.start()
        print("Thread1 started")

    @mainthread
    def get_response_without_objects(self,child_id=None):
        self.emotion = str(self.camera.usedeepface()).upper()
        print(f"The emotional value is {self.emotion}")
        global size, halign, value
        value = self.ai_query
        if len(value) < 6:
            size = .22
            halign = "center"
        elif len(value) < 11:
            size = .32
            halign = "center"
        elif len(value) < 16:
            size = .45
            halign = "center"
        elif len(value) < 21:
            size = .58
            halign = "center"
        elif len(value) < 26:
            size = .71
            halign = "center"
        else:
            size = .77
            halign = "left"
        self.chatview_id.add_widget(
            Command(text=value, size_hint_x=size, halign=halign))
        print(self.ai_query)
        if self.ai_query:
            if self.src_language == "en":
                self.messages.append(
                    {"role": "user", "content": self.ai_query+f"[*'EMOTION':'{self.emotion}'*]"},
                )
                # chat = openai.ChatCompletion.create(
                #     model="gpt-3.5-turbo", messages=self.messages, functions=self.functions
                # )
                chat = ChatCompleter.complete_chat(messages=self.messages)
            else:
                self.messages.append(
                    {"role": "user", "content": self.translated_text(text=self.ai_query,src_lang=self.src_language,dest_lang="en")+f"[*'EMOTION':'{self.emotion}'*]"},
                )
                # chat = openai.ChatCompletion.create(
                #     model="gpt-3.5-turbo", messages=self.messages, functions=self.functions
                # )
                chat = ChatCompleter.complete_chat(messages=self.messages)
        reply = chat
        print("This is the full reply:")
        print(chat)
        if self.dest_language == "en":
            self.chatview_id.add_widget(
                Response(text=PromptEditor.remove_parentheses(reply), size_hint_x=.75))

        else:
            translated_reply=self.translated_text(reply,src_lang="en")
            self.chatview_id.add_widget(
                Response(text=PromptEditor.remove_parentheses(translated_reply), size_hint_x=.75))
        self.messages.append({"role": "assistant", "content": reply})
        if self.loading_animation:
            self.last_answer = reply
            self.stop_loading_animation()

    def translated_text(self,text,dest_lang=dest_language,src_lang=src_language):
        if dest_lang != src_lang:
            transtext = Translator().translate(text, dest=dest_lang, src=src_lang).text
            print("[INPUT TEXT]"+text)
            print("[FROM]"+src_lang)
            print("[TO]"+dest_lang)
            print("[TRANSLATED TEXT] "+transtext)
            return transtext
        else:
            return text

    def show_snackbar(self):
        MDSnackbar(
            MDLabel(
                text="Hello Hariharan!"
            )
        ).open()

    def change_screen(self,screen):
        self.manager.change_screen(screen)

    def change_to_main_screen(self,mobile,passw):
        self.change_screen("main")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Teal"
        return self.manager
    

try:
    def get_file_paths(directory_path):
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_name, file_extension = os.path.splitext(file)
                file_paths.append((file_path, file_name, file_extension))
        return file_paths
    font_dir= r"C:\Socks\resources\fonts"
    files_info = get_file_paths(font_dir)
    for file_path, file_name, file_extension in files_info:
        LabelBase.register(
            name=file_name,fn_regular=file_path
        )

    SocksApp().run()
except:
    from traceback import format_exc
    from kivy.app import App
    from kivy.uix.textinput import TextInput
    class BackupApp(App):
        def build(self):
            print(format_exc())
            return TextInput(text=str(format_exc()))
    BackupApp().run()  