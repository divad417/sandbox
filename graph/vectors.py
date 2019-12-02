class vec:
    '''Cartesian location vector. May be 2D or 3D.'''
    def __init__(self, *args):
        if not args or len(args) > 3:
            raise ValueError('Invalid input')

        # Creation by list or tuple
        if len(args) == 1:
            if not isinstance(args[0], (list, tuple)):
                raise ValueError('Invalid Input')
            if len(args[0]) == 2:
                self.x, self.y = args[0]
                self.z = 0.0
                self._len = 2
            if len(args[0]) == 3:
                self.x, self.y, self.z = args[0]
                self._len = 3
            return

        # Creation by multiple input arguments
        self.x = args[0]
        self.y = args[1]
        if len(args) == 2:
            self.z = 0.0
            self._len = 2
        elif len(args) == 3:
            self.z = args[2]
            self._len = 3

    
    def _check(self, other: 'vec'):
        if self._len != other._len:
            raise RuntimeError('Cannot perform operations on vectors of different length')

    def _trim(self, out: 'vec') -> 'vec':
        # Trim 3D vectors to 2D to simplify operator definitions.
        if self._len == 2:
            out._len = 2
        return out

    def __repr__(self) -> str:
        if self._len == 2:
            return '{}, {}'.format(self.x, self.y)
        elif self._len == 3:
            return '{}, {}, {}'.format(self.x, self.y, self.z)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __eq__(self, other: 'vec') -> bool:
        self._check(other)
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other: 'vec') -> 'vec':
        self._check(other)
        return self._trim(
            vec(self.x + other.x, self.y + other.y, self.z + other.z))

    def __neg__(self) -> 'vec':
        return self._trim(
            vec(-self.x, -self.y, -self.z))

    def __sub__(self, other: 'vec') -> 'vec':
        return self + -other

    def __getitem__(self, key: int):
        # For conversion to numpy array
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        if key == 2 and self._len == 3:
            return self.z
        else:
            raise IndexError

    def __len__(self) -> int:
        # For conversion to numpy array
        return self._len

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @property
    def max(self):
        return max([abs(self.x), abs(self.y), abs(self.z)])

