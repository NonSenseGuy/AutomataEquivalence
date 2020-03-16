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
        return kplus1partition(do_partition(old, automata), new, automata)

def do_partition(old, automata):
    partition_new = []
    for partition in old:

        must_be = same_partition_states(partition, old, automata)
        temp = partition.difference(must_be)

        partitions = review_partition(temp, old, automata)

        partition_new.add(must_be)

        for item in partitions:
            partition_new.add(partitions)

    return partition_new

def review_partition(temp, old, automata):
    partitions = []
    partition = same_partition_states(temp, old, automata)   

    while (len(partition)!=0):
        partitions.add(partition)
        to_review = temp.difference(partiton)
        partition = same_partition_states(to_review, old, automata)

    return partitions 

def same_partition_states(states, old, automata):
    partition = set()
    state = states.pop()

    for item in states:
        control = review_states(state, item, automata, old)
        if control:
            partition.add(item)

    partition.add(state)

    return partition


def review_states(q1, q2, automata, old):
    in_same_partition = []
    for stimuli in len(automata.S):
        transition_state_q1 = automata.transition_map[q1][stimuli]
        transition_state_q2 = automata.transition_map[q2][stimuli]
        in_same_partition.append(same_partition(old, transition_state_q1, transition_state_q2))

    for item in in_same_partition:
        if item!=True:
            return False

    return True
        
def same_partition(partitions, q1, q2):
    for partition in partitions:
        if q1 in partition :
            if q2 in partition:
                return True
            else:
                return False



