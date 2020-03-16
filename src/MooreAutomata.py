from Automata import Automata

class MooreAutomata(Automata):
    """
    A class used to represent a Moore automata
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
        self.state_r = {}
        self.transition_map = {}
        Automata.__init__(self, Q, S, R, initial_state)
            
    """
    Add a transition to automata
    it gets the stimuli, the initial state and the final state where the stimuli goes
    it does not need the response because in Moore if you reach a state it has its own response
    so you don't have to specify 
    """
    def add_transition(self, stimuli, initial_q, final_q):
        try:
            if not initial_q in self.Q or not initial_q in self.state_map.keys():
                raise ValueError("Estado inicial erroneo") 
            if not final_q in self.Q or not final_q in self.state_map.keys():
                raise ValueError("Estado final erroneo")
            for s,q in self.transition_map[initial_q]:
                if(s == stimuli):
                    raise ValueError("Ya una transicion desde el estado inicial con el mismo estimulo")

            self.state_map[initial_q].add(final_q)
            self.transition_map[initial_q].append((stimuli, final_q))
        except ValueError:
            pass        
    
    """
    In Moore automatas you have the state response 
    R is an alphabet so you need to chose a response that you will 
    return if you reach a given state 
    """
    def add_response(self,state, response):
        try:
            if not response in self.R: 
                raise ValueError("La respuesta no esta contenida en el alfabeto de respuestas")
            self.state_r[state] = response 
        except ValueError:
            pass
    
    """
    This algorithm removes unreacheble states
    from a Moore Automata 
    """
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        l = []
        for v in self.transition_map:
            if v not in visited_vertices:
                l.append(v)
        self.remove_vertices_from_dict(l)

    """
    This method removes all the dependencies that can occur when you delete
    a state in the automata
    """
    def remove_vertices_from_dict(self, l):
        for v in l:
            del self.transition_map[v]
            del self.state_map[v]
            del self.state_r[v] 
    
    """
    This method replace all the dependencies that can occur when you
    change the name of a state in Moore Automata
    """
    def replace_states(self,old_state, new_state):
        self.replace_values(old_state, new_state)
        i = self.Q.index(old_state)
        self.Q[i] = new_state
        self.transition_map[new_state] = self.transition_map.pop(old_state)

    def replace_values(self, old_state, new_state):
        for t in self.transition_map[old_state]:
            if old_state in t:
                t[1] = new_state
        for state in self.transition_map:
            state_list = self.state_map[state]
            if old_state in state_list:
                state_list.remove(old_state)
                state_list.add(new_state)
                self.transition_map[state] = state_list
                    

        self.state_r[new_state] = self.state_r.pop(old_state)  

    """
    It gives you the response that you get when you reach a state 
    """
    def get_response(self, q):
        return self.state_r[q]





