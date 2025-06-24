import sys
import traceback
import os

# Crash logging for Android (with robust path)
def log_exception(exc_type, exc_value, exc_traceback):
    crash_log_path = os.path.join(os.path.expanduser('~'), 'grabber4_crashlog.txt')
    with open(crash_log_path, "w") as f:
        traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
sys.excepthook = log_exception

# Main Kivy app
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.core.window import Window

class Grabber4App(App):
    def build(self):
        # Set window size for desktop testing (ignored on Android)
        Window.size = (400, 600)
        self.title = "Grabber 4.0"

        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Camera widget
        self.camera = Camera(resolution=(640, 480), play=True)
        layout.add_widget(self.camera)

        # Label for results
        self.result_label = Label(text="Press the button to grab text", size_hint_y=0.2)
        layout.add_widget(self.result_label)

        # Button to trigger action
        button = Button(text="Capture Text", size_hint_y=0.2)
        button.bind(on_press=self.capture_and_ocr)
        layout.add_widget(button)

        return layout

    def capture_and_ocr(self, instance):
        # Save the camera image (for demo, not used in OCR yet)
        capture_path = os.path.join(os.path.expanduser('~'), 'grabber4_capture.png')
        self.camera.export_to_png(capture_path)

        # Simulate OCR (replace this with real OCR logic later)
        # For real OCR, you'd use pytesseract or Google Vision here
        # For now, just show a message
        self.result_label.text = "Text capture started!\n(Replace this with your OCR logic.)"
        self.show_popup("Info", "Image captured! Replace this with your OCR logic to extract text from the image.")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                    content=Label(text=message),
                    size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    Grabber4App().run()
