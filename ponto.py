class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Ponto({}, {})'.format(self.x+1, self.y+1)


