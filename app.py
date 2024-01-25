import webview
import os
from py.api import Api

APP_MODE = os.environ.get('APP_MODE', 'development')

if APP_MODE == 'development':
    entry_point = 'http://localhost:5173'
else:
    entry_point = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist', 'index.html')

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Vue example', entry_point, js_api=api)
    webview.start(debug=True)