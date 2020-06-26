import numpy as np
class PriorityQueue(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        "Co program ma wypisać jeżeli napiszemy len(PriorityQueue)"
        return len(self.items) - 1

    def __str__(self):
        "Co program ma wypisać jeżeli damy print(PriorityQueue)"
        return ' '.join([str((item[1],item[0])) for item in self.items[1:]])
    
    def insert(self, k):
        "Dodanie nowego elementu do PriorityQueue"
        self.items.append(k)
        self.heapify_up(len(self))

    def heapify_up(self, i):
        "Po dodaniu nowego elementu chcemy go ustawić na jego dobrej pozycji, więc wykonujemy odwrócone heapify dla niego"
        while i // 2 > 0:
            if self.items[i][0] < self.items[i//2][0]:
                self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
            i = i // 2


    def empty(self):
        return len(self) == 0

    def pop(self):
        "Wywal pierwszy element z heapa i go zwróć"
        if len(self) == 0: 
            return ''
        min_value = self.items[1]
        self.items[1] = self.items[len(self)] # na nowy pierwszy element ustawiamy ostatni, który był jednym z największych
        self.items.pop()
        if len(self) > 0:
            self.heapify_down(1)
        return min_value

    def heapify_down(self, i):
        " Po ustawieniu na początek ostatniego elementu mamy zaburzoną strukturę, dlatego wykonujemy podstawowe heapify"
        minimal_child = i
        if i * 2 <= len(self):
            minimal_child = min([(self.items[2*i+j],2*i+j) for j in range(2) if 2*i+j <= len(self)])[1]
        if self.items[i] > self.items[minimal_child]:
            self.items[i], self.items[minimal_child] = self.items[minimal_child], self.items[i]
            self.heapify_down(minimal_child)

    def top(self):
        return self.items[1][1] if len(self) > 0 else ''

    def priority(self, x, p):
        for i in range(1, len(self)+1):
            if self.items[i][1] == x and self.items[i][0] > p:
                self.items[i] = (p,x)
                self.heapify_up(i)




if __name__ == "__main__":



    pq = PriorityQueue()
    M = int(input("Podaj M: "))
    print("Podaj M poleceń:")
    for i in range(M):
        command = input().split(' ')
        command[0] = command[0].replace('\r','')
        if command[0] == 'print':
            print(pq)
        if command[0] == 'insert':
            command[1] = command[1].replace('\r','')
            command[2] = command[2].replace('\r','')
            pq.insert((int(command[2]), int(command[1])))
        if command[0] == 'top':
            print(pq.top())
        if command[0] == 'pop':
            print(pq.pop()[1])
        if command[0] == 'priority':
            command[1] = command[1].replace('\r','')
            command[2] = command[2].replace('\r','')
            pq.priority(int(command[1]), int(command[2]))
        if command[0] == 'empty':
            if pq.empty():
                print(1)
            else:
                print(0)

            
