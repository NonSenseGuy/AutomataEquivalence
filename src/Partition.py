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
