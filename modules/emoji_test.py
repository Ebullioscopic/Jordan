from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
import os
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
except:
    pass
class TestApp(MDApp):
    
    def build(self):
        return MDLabel(text="🌃💬🌶️💜📌", font_name="NotoColorEmoji-Regular")

TestApp().run()