from MealyAutomata import MealyAutomata
from MooreAutomata import MooreAutomata
import Partition
from Equivalence import Equivalence

MEALY = 0
MOORE = 1



def main():
    automata1 = None
    automata2 = None
    print("INGRESE TIPO DE AUTOMATA, 0 SI ES MEALY - 1 SI ES MOORE")
    typ = int(input())
    for i in range(2):
        print("INGRESE LOS ELEMENTOS DEL ALFABETO Q SEPARADOS POR ESPACIO")
        states = input().split(' ')
        print('INGRESE EL ALFABETO DE ESTIMULOS')
        stimulus = input().split(' ')
        print('INGRESE EL ALFABETO DE RESPUESTAS')
        responses = input().split(' ')
        print('INGRESE EL ESTADO INICIAL')
        initial_state = input()
        if(typ == MEALY):
            a = MealyAutomata(states,stimulus,responses, initial_state)
            for q in a.Q:
                a.add_state(q)
            print("Ingrese el numero de transiciones a agregar")
            n = int(input())
            for i in range(n):
                print("INGRESE LA TRANSICION DE LA SIGUIENTE MANERA STIMULO, Q0, Q1, RESPUESTA. POR EJ: 0 A B 1")
                s,q0,q1,r = input().split(' ')
                a.add_transition(s,q0,q1,r)
        else:
            a = MooreAutomata(states,stimulus, responses,initial_state)
            for q in a.Q:
                a.add_state(q)
            print("INGRESE LAS RESPUESTAS PARA CADA ESTADO, DE LA SIGUIENTA MANERA [ESTADO,RESPUESTA], POR EJ: A 0 ")
            n = len(a.Q)
            for _ in range(n):
                q, r = input().split(' ')
                a.add_response(q, r)
            print("Ingrese el numero de transiciones a agregar")
            n = int(input())
            for i in range(n):
                print("INGRESE LA TRANSICION DE LA SIGUIENTE MANERA STIMULO, Q0, Q1, RESPUESTA. POR EJ: 0 A B 1")
                s,q0,q1,r = input().split(' ')
                a.add_transition(s,q0,q1,r)
        if i == 0:
            automata1 = a
            print("AHORA INGRESE LOS VALORES DEL SIGUIENTE AUTOMATA")
        else:
            automata2 = a
    
    e = Equivalence(automata1, automata2)
    if(e.are_equivalent()):
        print("SON EQUIVALENTES")
    else:
        print("NO SON EQUIVALENTES")
    

    

if __name__ == '__main__':
    main()