Algorithm A, the original:
    tortoise = head
    rabbit = head
    length = 0
    if rabbit == null: return length
    rabbit, length = step(rabbit), length+1
    if rabbit == null: return length
    while rabbit != tortoise:
        rabbit, length = step(rabbit), length+1
        if rabbit==null: return length
        rabbit, length = step(rabbit), length+1
        if rabbit==null: return length
        tortoise = step(tortoise)
    return infinity

Algorithm B, the leaping version:
    tortoise = head
    rabbit = head
    length,gap = 0, 0
    if rabbit == null: return "Finite list of length "+string(length)
    rabbit, length, gap = step(rabbit), length+1, gap+1
    if rabbit == null: return "Finite list of length "+string(length)
    limit = 1
    while rabbit != tortoise:
        if gap==limit: tortoise, gap, limit = rabbit, 0, limit*2
        rabbit, length, gap = step(rabbit), length+1, gap+1
        if rabbit==null: return "Finite list of length "+string(length)
    return "List with loop of size "+string(gap)
