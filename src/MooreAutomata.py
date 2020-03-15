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

    def add_response(self,state, response):
        try:
            if not response in self.R: 
                raise ValueError("La respuesta no esta contenida en el alfabeto de respuestas")
            self.state_r[state] = response 
        except ValueError:
            pass

    
    def remove_unreachable_vertices(self):
        visited_vertices = self.bfs()
        for v in visited_vertices:
            del self.state_r[v]
            del self.state_map[v]
    
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

            

    def get_response(self, q):
        return self.state_r[q]





