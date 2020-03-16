def first_partition(automata):
    p1 = []
    responses = []
    for q in automata.state_map.keys():
        responses.append((q,automata.get_response(q)))

    for q0,r0 in responses:
        temp = set() ##List of temporal states to add into a set in a partition
        if not is_state_in_partition(q0, p1):  
            temp.add(q0) 
            for q1,r1 in responses:
                if(q0 != q1 and r0 == r1):
                    temp.add(q1)
            p1.append(temp)
    return p1

def is_state_in_partition(q, p):
    for t in p:
        if q in t:
            return True
    return False

def kplus1partition(new, old, automata):
    if new == old :
        return new
    else:
        return kplus1partition(do_partition(new, old), new, automata)

def do_partition(new, old, automata):
    pass

def review_temp(temp, oldpartition, automata):
    partitions = []
    
    while (len(temp)!=0):
        control=True
        q = temp[0]
        temp.remove(q)



    return partitions


def review_states(q1, q2, automata, old):
    in_same_partition = []
    for stimuli in automata.S:
        transition_state_q1 = automata.transition_map[q1][1]
        transition_state_q2 = automata.transition_map[q2][1]
        in_same_partition.append(same_partition(old, q1, q2))

    for item in in_same_partition:
        if item!=True:
            return False

    return True
        
def same_partition(partitions, q1, q2):
    for partition in partitions:
        if q1 inpartition :
            if q2 in partition:
                return True
            else:
                return False



