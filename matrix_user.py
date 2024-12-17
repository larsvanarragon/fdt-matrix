import requests

# logging
import logging
logger = logging.getLogger(__name__)

# constants for Matrix API entrypoints
LOGIN_API_PATH = "/_matrix/client/v3/login"
SEND_MESSAGE_API_PATH = "/_matrix/client/v3/rooms/{0}/send/m.room.message"
JOIN_ROOM_API_PATH = "/_matrix/client/v3/join/{0}"
LEAVE_ROOM_API_PATH = "/_matrix/client/v3/rooms/{0}/leave"

class MatrixUser:

    def __init__(self, homeserver: str, username: str, password: str):
        self.homeserver = homeserver
        self.username = username
        self.password = password
        # variables used in actions of a Matrix User
        self.access_token = None
        
        logger.info(f"{username}: initialized user: '{username}', with pw '{password}' on homeserver '{homeserver}'")

    # private function enabling uniform creation of authentication headers
    # adds Bearer token to the header if it is not None
    def __get_authentication_headers(self):
        if self.access_token == None:
            return None
        logger.debug(f"{self.username}: generating headers")
        return {"authorization": f"Bearer {self.access_token}"}

    # TODO placeholder
    def login(self):
        url = f"{self.homeserver}{LOGIN_API_PATH}"
        data = {
            "type": "m.login.password",
            "user": self.username,
            "password": self.password,
        }
        response = requests.post(url=url, json=data)

        if response.ok:
            self.access_token = response.json()["access_token"]
            logger.info(f"{self.username}: logged in successfully and got '{self.access_token}' as token")
        else:
            logger.error(f"{self.username}: logging in failed with '{response.status_code}' because '{response.reason}'")
        return response
    
    # TODO placeholder
    def join_room(self, room_id):
        url = f"{self.homeserver}{JOIN_ROOM_API_PATH.format(room_id)}"
        response = requests.post(url=url, headers=self.__get_authentication_headers())

        if response.ok:
            logger.info(f"{self.username}: joined room '{room_id}'")
        else:
            logger.error(f"{self.username}: joining room '{room_id}'"
                         f" failed with '{response.status_code}' because '{response.reason}'")
        return response
    
    # TODO placeholder
    def leave_room(self, room_id):
        url = f"{self.homeserver}{LEAVE_ROOM_API_PATH.format(room_id)}"
        response = requests.post(url, headers=self.__get_authentication_headers())
        
        if response.ok:
            logger.info(f"{self.username}: left room '{room_id}'")
        else:
            logger.error(f"{self.username}: leaving room '{room_id}'"
                         f" failed with '{response.status_code}' because '{response.reason}'")
        return response

    # TODO placeholder
    def send_message(self, room_id, message):
        url = f"{self.homeserver}{SEND_MESSAGE_API_PATH.format(room_id)}"
        data = {
            "body": message,
            "msgtype": "m.text"
        }
        response = requests.post(url=url, params=None, json=data, headers=self.__get_authentication_headers())

        if response.ok:
            logger.info(f"{self.username}: send message '{message}' in '{room_id}'")
        else:
            logger.error(f"{self.username}: send message failed with '{response.status_code}' because '{response.reason}'" 
                         f" while sending '{message}' in '{room_id}'")
        return response