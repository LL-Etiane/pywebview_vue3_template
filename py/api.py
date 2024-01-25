import os 
import webview

class Api:
    def select_music_dailog(self):
        window = webview.windows[0]
        music = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False, file_types=('Music Files (*.mp3;*.wav)',))
        if not music:
            webview.evaluate_js('alert("No music selected.");')
            return None
        
        # play the music with default player
        print(music)
        os.system(music[0])
        True
    