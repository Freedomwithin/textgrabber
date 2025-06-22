import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window

import pytesseract
from PIL import Image
import datetime
import re
import os

print("✅ App is starting up...")  # Debug print on start

class TextGrabberLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Raw OCR text area
        self.raw_text_area = TextInput(text='', readonly=True, size_hint_y=0.45)
        self.add_widget(Label(text="📄 Raw OCR Text:", size_hint_y=0.05))
        self.add_widget(self.raw_text_area)

        # Parsed text area
        self.parsed_text_area = TextInput(text='', readonly=True, size_hint_y=0.45)
        self.add_widget(Label(text="🔎 Parsed Fields:", size_hint_y=0.05))
        self.add_widget(self.parsed_text_area)

        button_box = BoxLayout(size_hint_y=0.1)

        grab_btn = Button(text='📸 Grab Text')
        grab_btn.bind(on_press=self.grab_text)
        button_box.add_widget(grab_btn)

        save_raw_btn = Button(text='💾 Save Raw Text')
        save_raw_btn.bind(on_press=self.save_raw_text)
        button_box.add_widget(save_raw_btn)

        save_parsed_btn = Button(text='💾 Save Parsed Data')
        save_parsed_btn.bind(on_press=self.save_parsed_text)
        button_box.add_widget(save_parsed_btn)

        self.add_widget(button_box)

        # Receipt-style regex patterns
        self.terms = {
            "Store:": r"(Store[:\-]?\s*)([A-Za-z0-9 &]+)",
            "Date:": r"(Date[:\-]?\s*)(\d{2}/\d{2}/\d{4})",
            "Subtotal:": r"(Subtotal[:\-]?\s*)(EUR\s*\d+\.\d{2})",
            "Tax:": r"(Tax[:\-]?\s*)(EUR\s*\d+\.\d{2})",
            "Total:": r"(Total[:\-]?\s*)(EUR\s*\d+\.\d{2})",
            "Payment Method:": r"(Payment(?: Method)?[:\-]?\s*)([A-Za-z ]+)"
        }

    def grab_text(self, instance):
        try:
            image_path = "/home/jonathonkoerner/Pictures/screenshot.png"
            print(f"🔍 Trying to open image at: {image_path}")

            if not os.path.exists(image_path):
                self.show_popup("Error", f"Image not found:\n{image_path}")
                print("❌ Image not found.")
                return

            img = Image.open(image_path)
            raw_text = pytesseract.image_to_string(img)
            print("✅ OCR text extracted.")

            self.raw_text_area.text = raw_text if raw_text.strip() else "No text detected."

            parsed_results = self.extract_fields(raw_text)
            parsed_text_lines = []
            for key, val in parsed_results.items():
                parsed_text_lines.append(f"{key} {val if val else 'Not found'}")
            self.parsed_text_area.text = "\n".join(parsed_text_lines)
            print("✅ Parsed fields updated.")

        except Exception as e:
            self.show_popup("Error", f"Failed to process image:\n{e}")
            print(f"❌ Error during grab_text: {e}")

    def extract_fields(self, text):
        results = {}
        for term, pattern in self.terms.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                results[term] = match.group(2).strip()
            else:
                results[term] = None
        return results

    def save_raw_text(self, instance):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"textgrab_raw_{timestamp}.txt"
            with open(filename, "w") as f:
                f.write(self.raw_text_area.text)
            self.show_popup("Success", f"Raw text saved to {filename}")
            print(f"💾 Raw text saved to {filename}")
        except Exception as e:
            self.show_popup("Error", f"Failed to save raw text:\n{e}")
            print(f"❌ Error saving raw text: {e}")

    def save_parsed_text(self, instance):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"textgrab_parsed_{timestamp}.txt"
            with open(filename, "w") as f:
                f.write(self.parsed_text_area.text)
            self.show_popup("Success", f"Parsed data saved to {filename}")
            print(f"💾 Parsed data saved to {filename}")
        except Exception as e:
            self.show_popup("Error", f"Failed to save parsed data:\n{e}")
            print(f"❌ Error saving parsed data: {e}")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class TextGrabberApp(App):
    def build(self):
        print("✅ Building layout...")
        self.title = "Text Grabber Pro 3.0"
        Window.size = (700, 600)
        return TextGrabberLayout()

if __name__ == '__main__':
    TextGrabberApp().run()
