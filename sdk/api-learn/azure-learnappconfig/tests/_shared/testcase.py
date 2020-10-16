import os

from devtools_testutils import AzureTestCase

class AppConfigTestCase(AzureTestCase):
    def __init__(self, *args, **kwargs):
        super(AppConfigTestCase, self).__init__(*args, **kwargs)
        self.env_color = os.environ.get('API-LEARN_SETTING_COLOR_VALUE', "Green")
        self.env_color_key = os.environ.get('API-LEARN_SETTING_COLOR_KEY', "FontColor")
        self.env_greeting = os.environ.get('API-LEARN_SETTING_TEXT_VALUE', "Hello World!")
        self.env_greeting_key = os.environ.get('API-LEARN_SETTING_TEXT_KEY', "Greeting")

    def get_connection_string(self, id, secret):
        return "DefaultEndpointsProtocol=https;Id=" + id + ";Secret=" + secret