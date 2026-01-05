from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivy.clock import Clock
from kivy.utils import platform
from kivy.core.window import Window
import yt_dlp
import threading
import os

# Request permissions on Android
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

class Spotify2Mobile(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        
        screen = Screen()
        scroll = MDScrollView()
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Title
        self.label_title = MDLabel(
            text="Spotify/YouTube Downloader", 
            halign="center", 
            font_style="H5",
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.label_title)

        # Input Field
        self.input_url = MDTextField(
            hint_text="Paste Link or Song Name",
            helper_text="Supports Spotify Tracks, YouTube Links, or Search Terms",
            helper_text_mode="on_focus",
            mode="rectangle",
            size_hint_y=None,
            height=60
        )
        layout.add_widget(self.input_url)

        # Format Selection (Simple Toggle)
        self.status_label = MDLabel(
            text="Ready", 
            halign="center", 
            theme_text_color="Secondary",
            size_hint_y=None, 
            height=40
        )
        layout.add_widget(self.status_label)

        # Download Button
        self.btn_download = MDRaisedButton(
            text="DOWNLOAD MP3",
            pos_hint={"center_x": 0.5},
            size_hint_y=None,
            height=50,
            on_release=self.start_thread
        )
        layout.add_widget(self.btn_download)

        scroll.add_widget(layout)
        screen.add_widget(scroll)
        return screen

    def start_thread(self, instance):
        query = self.input_url.text
        if not query:
            self.status_label.text = "Please enter a link or name!"
            return
        
        # Disable button during download
        self.btn_download.disabled = True
        self.status_label.text = "Initializing..."
        
        # Run download in background so UI doesn't freeze
        threading.Thread(target=self.run_download, args=(query,)).start()

def run_download(self, query):
        try:
            if platform == 'android':
                storage_path = "/storage/emulated/0/Download"
            else:
                storage_path = os.path.join(os.path.expanduser("~"), "Downloads")
            
            # UPDATED: No FFmpeg required. Downloads M4A (Audio Only)
            ydl_opts = {
                'format': 'bestaudio[ext=m4a]/bestaudio', # Forces M4A
                'outtmpl': f'{storage_path}/%(title)s.%(ext)s',
                'quiet': True,
                'no_warnings': True,
                # Removed 'postprocessors' block that required ffmpeg
            }

            if not query.startswith('http'):
                query = f"ytsearch1:{query}" 

            Clock.schedule_once(lambda x: self.update_status(f"Downloading: {query[:20]}..."), 0)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([query])

            Clock.schedule_once(lambda x: self.update_status("✅ Download Complete!"), 0)
            
        except Exception as e:
            Clock.schedule_once(lambda x: self.update_status(f"❌ Error: {str(e)}"), 0)
        
        finally:
            Clock.schedule_once(self.enable_button, 0)

    def update_status(self, text):
        self.status_label.text = text

    def enable_button(self, dt):
        self.btn_download.disabled = False

if __name__ == '__main__':
    Spotify2Mobile().run()