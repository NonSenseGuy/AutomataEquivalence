from abc import ABC, abstractmethod

class AutomataInterface:

    @abstractmethod
    def add_transition(self):
        pass
    
    @abstractmethod
    def add_state(self):
        pass
    
    @abstractmethod
    def add_response(self):
        pass

    @abstractmethod
    def remove_unreachable_vertices(self):
        pass

    @abstractmethod
    def bfs(self):
        pass