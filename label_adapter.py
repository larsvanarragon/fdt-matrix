from matrix_user import MatrixUser
from callback_handler import CallbackHandler
import input_generation

# logging
import logging
logger = logging.getLogger(__name__)

TESTROOM_ID = "!AxPlfhgsOJxRiKuOWe:variability.testing.nl"

class LabelAdapter:

    def __init__(self, matrix_user: MatrixUser):
        self.matrix_user = matrix_user

    def register_callback_handler(self, callback_handler: CallbackHandler):
        self.callback_handler = callback_handler

    def handle_label(self, label: str):
        match label:
            case "SendMessage":
                to_send_message = input_generation.random_word(20, 2)
                self.callback_handler.callback(f"ASentMessage(\"{to_send_message}\")")
                response = self.matrix_user.send_message(TESTROOM_ID, to_send_message)
                if response.ok:
                    self.callback_handler.callback("Ok")
                else:
                    self.callback_handler.callback("NOk")