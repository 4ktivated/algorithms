import collections
def bfs(name):
    search_queue = collections.deque(graf[name])
    searched = []
    while search_queue:
        for _ in range(len(search_queue)):
            person = search_queue.popleft()
            if person not in searched:
                if person_valid(person):
                    print('i find you '+ person)
                    return True
                else:
                    search_queue.append(graf[person])
                    searched.append(person)
    return False

def person_valid(person):
    return person.startswith('M')

graf = {'you': ['Sam', 'Bob', 'Alex'], 'Alex': ['Patrik'], 'Bob':['Maggy', 'Sam'], 'Sam':[]}

print(bfs('you'))
#now it works and looks like realy BFS :)