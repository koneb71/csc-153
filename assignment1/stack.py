class ListStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)


    def isempty(self):
        return len(self._data) == 0

    def top(self):
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        return self._data.pop()

    def remove_empties(self):
        self._data = filter(len, filter(None, self._data))