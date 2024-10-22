from abc import ABC, abstractmethod

class BaseApp(ABC):
    @abstractmethod 
    def app_tick(self):
        # Method that will be populated in child classes with the functionality 
        # called on every tick
        ...
    

    @abstractmethod
    def draw_window(self):
        # Method that will be populated in child classes with the functionality 
        # of rendering the UI
        ...