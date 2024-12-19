from abc import ABC, abstractmethod

class CallbackHandler(ABC):

    @abstractmethod
    def callback(label: str):
        raise NotImplementedError