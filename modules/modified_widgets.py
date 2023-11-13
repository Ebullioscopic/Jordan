try:
    from kivymd.uix.relativelayout import MDRelativeLayout
    from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, OptionProperty, NumericProperty, ListProperty
    from kivy.uix.popup import Popup
    from kivy.animation import Animation
    from kivy.uix.widget import Widget
    from kivymd.theming import ThemableBehavior
    from kivy.clock import Clock, mainthread
    from kivymd.uix.label import MDLabel
    from kivy.uix.camera import Camera
    from threading import Thread
    from functions import *
    from cv2 import imread
except:
    from traceback import format_exc
    from kivy.app import App
    from kivy.uix.textinput import TextInput
    class BackupApp(App):
        def build(self):
            print(format_exc())
            return TextInput(text=str(format_exc()))
    BackupApp().run()

class FaceCam(Camera):

    #play = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.play = True
    @mainthread
    def usedeepface(self):
        mythread = self.export_to_png("FaceValue.png")
        #self.export_to_png("FaceValue.png")
        mynewthread = FaceRecognition.get_emotion()
        self.export_to_png("FaceValue.png")
        FaceRecognition.get_emotion()
        #Clock.schedule_once(lambda x: mythread)
        #Clock.schedule_once(lambda x: mynewthread)

class AKSpinnerBase(ThemableBehavior, Widget):
    spinner_size = NumericProperty(48)
    speed = NumericProperty(0.4)
    active = BooleanProperty(False)
    color = ListProperty()

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins-Light"
    font_size = 17

class ChatTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    write_tab = BooleanProperty()
    on_text_validate = ObjectProperty()

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Poppins-Light"
    font_size = 17

class SpeechRequest(Popup):
    text = StringProperty("")
    state = BooleanProperty(0)


class AKSpinnerThreeDots(AKSpinnerBase):

    animation = StringProperty("linear")

    _circle_size1 = ListProperty([0, 0])
    _circle_size2 = ListProperty([0, 0])
    _circle_size3 = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _start_animate(self, size):
        self.anim1 = (
            Animation(
                _circle_size1=[size, size],
                opacity=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _circle_size1=[0, 0], duration=self.speed, t=self.animation
            )
            + Animation(duration=self.speed)
        )

        self.anim2 = (
            Animation(
                _circle_size2=[size, size],
                opacity=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _circle_size2=[0, 0], duration=self.speed, t=self.animation
            )
            + Animation(duration=self.speed)
        )

        self.anim3 = (
            Animation(
                _circle_size3=[size, size],
                opacity=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _circle_size3=[0, 0], duration=self.speed, t=self.animation
            )
            + Animation(duration=self.speed)
        )

        self.anim1.repeat = True
        self.anim2.repeat = True
        self.anim3.repeat = True

        self.anim1.start(self)
        Clock.schedule_once(lambda dt: self.anim2.start(self), self.speed)
        Clock.schedule_once(lambda dt: self.anim3.start(self), self.speed * 2)

    def _stop_animate(self):
        self.anim1.cancel_all(self)
        self.anim2.cancel_all(self)
        self.anim3.cancel_all(self)
        self.anim1_stop = Animation(
            _circle_size1=[0, 0], opacity=0, duration=0.1, t=self.animation
        )
        self.anim2_stop = Animation(
            _circle_size2=[0, 0], opacity=0, duration=0.1, t=self.animation
        )
        self.anim3_stop = Animation(
            _circle_size3=[0, 0], opacity=0, duration=0.1, t=self.animation
        )
        self.anim1_stop.start(self)
        self.anim2_stop.start(self)
        self.anim3_stop.start(self)

    def on_active(self, *args):
        size = self.size[1]
        if self.active:
            self._start_animate(size)
        else:
            self._stop_animate()

class AKSpinnerFoldingCube(AKSpinnerBase):
    angle = NumericProperty(45)
    animation = StringProperty("out_cubic")

    _cubeitem1 = ListProperty([0, 0])
    _cubeitem2 = ListProperty([0, 0])
    _cubeitem3 = ListProperty([0, 0])
    _cubeitem4 = ListProperty([0, 0])
    _cube1a = NumericProperty(0)
    _cube2a = NumericProperty(0)
    _cube3a = NumericProperty(0)
    _cube4a = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _start_animate(self, size):
        size /= 2
        self.cube_fold = (
            Animation(
                _cubeitem1=[size, size],
                _cube1a=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem2=[size, size],
                _cube2a=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem3=[size, size],
                _cube3a=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem4=[size, size],
                _cube4a=1,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem4=[0, size],
                _cube4a=0,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem3=[size, 0],
                _cube3a=0,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem2=[0, size],
                _cube2a=0,
                duration=self.speed,
                t=self.animation,
            )
            + Animation(
                _cubeitem1=[size, 0],
                _cube1a=0,
                duration=self.speed,
                t=self.animation,
            )
        )
        self.cube_fold.repeat = True
        self.cube_fold.start(self)

    def _update(self, size):
        self._cubeitem1 = [size / 2, 0]
        self._cubeitem2 = [0, size / 2]
        self._cubeitem3 = [size / 2, 0]
        self._cubeitem4 = [0, size / 2]

    def _stop_animate(self, size):
        size /= 2
        self.cube_fold.cancel_all(self)
        self.cube_stop = (
            Animation(
                _cubeitem4=[0, size], _cube4a=0, duration=0.1, t=self.animation
            )
            + Animation(
                _cubeitem3=[size, 0], _cube3a=0, duration=0.1, t=self.animation
            )
            + Animation(
                _cubeitem2=[0, size], _cube2a=0, duration=0.1, t=self.animation
            )
            + Animation(
                _cubeitem1=[size, 0], _cube1a=0, duration=0.1, t=self.animation
            )
        )
        self.cube_stop.start(self)

    def on_active(self, *args):
        size = self.size[0]
        self._update(size)
        if self.active:
            self._start_animate(size)
        else:
            self._stop_animate(size)

class MDPasswordTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    write_tab = BooleanProperty()
    on_text_validate = ObjectProperty()

class LoadingAnimation(Popup):
    def on_pre_open(self):
        self.ids.foldingcube.active = True

    def on_dismiss(self):
        self.ids.foldingcube.active = False
