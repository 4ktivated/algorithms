import collections
def bfs(name):
    search_queue = collections.deque()
    search_queue += graf[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_valid(person):
                print('i find you'+ person)
                return True
            else:
                search_queue += graf[person]
                searched.append(person)
    return False

def person_valid(person):
    if person[0] == 'M':
        return True
    else:
        return False
    
#alg from book
graf = {'Marty': ['Sam', 'Bob', 'Alex'], 'Alex': ['Patrik'], 'Bob':['Maggy', 'Sam'], 'Sam':['Tom']}

