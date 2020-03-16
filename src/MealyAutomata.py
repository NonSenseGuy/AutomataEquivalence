from Automata import Automata

class MealyAutomata(Automata):
    """
    A class used to represent a deterministic finite state machine

    ...

    Attributes
    ----------
    Q : list(str)
    State set
    S : list(str)
    Stimuli set
    R : list(str):
    Response set
    initial_state : str
    Automata initial state

    """

    def __init__(self, Q, S, R, initial_state):
        self.transition_map = {}   
        Automata.__init__(self, Q, S, R, initial_state)

    """
    In Mealy automata if you need to add a transition you need to specify
    the response that you will receive
    """
    def add_transition(self, stimuli, initial_q, final_q, r):
        try:
            if not r in self.R:
                 raise ValueError("La respuesta no esta en el alfabeto de respuestas")
            if not initial_q in self.Q or not initial_q in self.state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in self.Q or not final_q in self.state_map.keys():
                raise ValueError("Estado final erroneo")
            if not stimuli in self.S or stimuli in self.transition_map[initial_q]:
                raise ValueError("Estimulo erroneo")

            self.transition_map[initial_q].append((stimuli,final_q, r)) 
            self.state_map[initial_q].add(final_q)
            self.sort_transition_map()
        except ValueError as e:
            print(str(e))       

    """
    It removes unreachable vertices from the initial state
    in a Mealy Automata
    """    
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        l = []
        for v in self.transition_map:
            if v not in visited_vertices:
                l.append(v)
        self.remove_vertices_from_dict(l)

    """
    It removes all the dependencies taht you will get if you delete a 
    state in a Mealy Automata
    """
    def remove_vertices_from_dict(self, l):
        for v in l:
            del self.transition_map[v]
            del self.state_map[v]
    
    """
    It replaces all the dependencies that you will get if you change
    the name of a state in a Mealy Automata 
    """
    def replace_states(self,old_state, new_state):
        for t in self.transition_map[old_state]:
            if old_state in t:
                t[1] = new_state
                pass
        
    """
    It alings the dictionaries with the stimulus
    Making it looks like the tables that we use to represent automatas
    """
    def sort_transition_map(self):
        for q in self.transition_map:
            l = self.transition_map[q]
            l.sort(key=lambda x: x[0])
            self.transition_map[q] = l
        return self.transition_map

    """
    It gives you the response that you get when you reach a state 
    """
    def get_response(self, q):
        self.sort_transition_map()
        responses = []
        for s,q1,r in self.transition_map[q]:
            responses.append(r)
        return responses
