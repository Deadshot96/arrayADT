import ctypes as _ct
from copy import copy as _cp
from copy import deepcopy as _dp
from collections import OrderedDict as _od

class Array:  
    def __init__(self, size):
        assert isinstance(size, int), 'The size of array must be an integer'
        assert size > 0, 'The size must be greater than 0'

        self._size = size
        PyArrayType = _ct.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value


    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        S = '['
        for i in range(self._size):
            S += (str(self._elements[i]) + ', ')
        S = S[:-2]
        S += ']'
        return S

    def __repr__(self):
        S = '['
        for i in range(self._size):
            S += (str(self._elements[i]) + ', ')
        S = S[:-2]
        S += ']'
        return S

    def __contains__(self, target):
        return self.contains(target)

    def contains(self, target):
        for element in self._elements:
            if element == target:
                return True
        else:
            return False
        
    def count(self, target):
        counter = 0
        for i in range(self._size):
            if target == self._elements[i]:
                counter += 1
        return counter
        
    def copy(self):
        X = Array(len(self))
        for i, j in enumerate(self):
            X[i] = j
        return X
    
    def index(self, value):
        for i, j in enumerate(self):
            if j == value:
                return i
        else:
            return None
        
        
    def __add__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] + val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] + val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    
    def __sub__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] - val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] - val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        
        
    def __mul__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] * val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] * val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        

    def __truediv__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] / val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] / val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        
    
    def __floordiv__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] // val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] // val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
        
    def __mod__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] % val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] % val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __pow__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ** val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ** val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
    
    def __lshift__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] << val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] << val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __rshift__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >> val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >> val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __and__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] & val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] & val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __or__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] | val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] | val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')

    def __xor__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ^ val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ^ val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
    
    def __pos__(self):
        return self.copy()
    
    def __neg__(self):
        return -1 * self.copy()
    
    def __iadd__(self, val):
        self = self + val
    
    def __isub__(self, val):
        self = self - val
        
    def __imul__(self, val):
        self = self * val
        
    def __itruediv__(self, val):
        self = self / val
    
    def __ifloordiv__(self, val):
        self = self // val
        
    def __imod__(self, val):
        self = self % val
        
    def __ilshift__(self, val):
        self = self << val
        
    def __irshift__(self, val):
        self = self >> val
        
    def __ipow__(self, val):
        self = self ** val
        
    def __iand__(self, val):
        self = self & val
        
    def __ior__(self, val):
        self = self | val
        
    def __ixor__(self, val):
        self = self ^ val        
    
    def __abs__(self):
        total = Array(len(self))
        for index in range(len(self)):
            total[index] = abs(self[index])
            
        return total
    def __invert__(self):
        total = Array(len(self))
        for index, val in enumerate(self):
            total = ~val
            
        return total
    
    def __lt__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] < val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] < val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __gt__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] > val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] > val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __eq__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] == val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] == val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')

    def __le__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] <= val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] <= val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __ge__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >= val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >= val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __ne__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] != val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] != val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
        
        
    


class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        self._curNdx = 0
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])
    
    def shape(self):
        return self.numRows(), self.numCols()
    
    def size(self):
        return self.numRows() * self.numCols()

    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

    def __str__(self):
        S = str()
        for row in self._theRows:
            S += (str(row) + "\n")
        return S

    def __repr__(self):
        return str(self)
    

    def returnRow(self, row):
        assert row in range(0, self.numRows()), "Invalid Row"
        return self._theRows [ row ]
    
    def returnCol(self, col):
        assert col in range(0, self.numCols()), "Invalid Column"
        newArray = Array(self.numRows())
        for i in range(self.numRows()):
            row = self._theRows[i]
            newArray[i] = row [col]
        return newArray
    
    def __iter__(self):
        self._curNdx = 0
        return self
    
    def __next__(self):
        row = self._curNdx // self.numCols()
        col = self._curNdx % self.numCols()
        
        if self._curNdx < (self.numCols() * self.numRows()):
            self._curNdx += 1
            iterRow = self._theRows[row]
            return iterRow[col]
        else:
            raise StopIteration
        
    def copy(self):
        copyArray = Array2D(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                copyArray[i, j] = self[i, j]
        return copyArray
    
    def count(self, target):
        count = 0
        for i in range(self.numRows()):
            X = self._theRows[i]
            count += X.count(target)
        
        return count
    
    def index(self, value):
        for xNum, row in enumerate(self._theRows):
            for yNum, val in enumerate(row):
                if val == value:
                    return xNum, yNum
        
        return None, None
    
    def __len__(self):
        return self.numRows()
    
    def __add__(self, val):
        if isinstance(val, (int, float)):
            total = Array2D(self.numRows(), self.numCols())
            for i in range(self.numRows()):
                for j in range(self.numCols()):
                    total[i, j] = self[i, j] + val
            return total
        elif isinstance(val, Array2D) and self.shape() == val.shape():
            total = Array2D(self.numRows(), self.numCols())
            for i in range(self.numRows()):
                for j in range(self.numCols()):
                    total[i, j] = self[i, j] + val[i, j]
            return total
    


#if isinstance(val, (int, float)):
    #total = Array(len(self))
    #for index in range(len(self)):
        #total[i] = self[i] // val
    #return total
#elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
    #total = Array(len(self))
    #for index in range(len(self)):
        #total[i] = self[i] // val[i]
    #return total
#else:
    #raise TypeError('Operation between invalid types.')
            
            
        

class MultiArray:
        
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."

        self._dims = dimensions
        size = 1
        for dim in dimensions:
            assert dim > 0, "Dimensions must be > 0."
            size *= dim
        self._elements = Array(size)
        self._factors = Array(len(dimensions))
        self._factors.clear(1)
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim > 0 and dim < len(self._dims), "Dimension component out of range."
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)
    
    def shape(self):
        dims = _cp(self._dims)
        return dims

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."

        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    def _computeIndex(self, idx):
        offset = 0
        for i, j in enumerate(idx):
            if j < 0 and j > self._dims[i]:
                return None
            else:
                offset += self._factors[i] * j
        return offset

    def _computeFactors(self):
        for i in range(1, len(self._factors)):
            self._factors[len(self._factors) -i - 1] = self._factors[len(self._factors)-i] * self._dims[len(self._factors)-i]

class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

class _SparseArrayNode(object):
    
    def __init__(self, index = 0, value = 0):
        self.index = index
        self.value = value
        self.next = None


class SparseArray(object):
    
    def __init__(self, size):
        assert isinstance(size, int), 'The size of array must be an integer.'
        assert size > 0, 'The size must be greater than 0.'
        
        self._lenght = size
        self._size = 0
        self._elements = None
        self._clear = 0
        self._ndx = None
        self._nodeFlag = False
        self._iterndx = 0
    
    def printNodes(self):
        if self._elements is None:
            print("Null Array.")
            return False
        
        curNode = self._elements
        nodeDir = dict()
        
        while curNode is not None:
            nodeDir[curNode.index] = curNode.value
            curNode = curNode.next
        
        print(nodeDir)
        return True
    
    
    def __len__(self):
        return self._lenght
    
    def __setitem__(self, index, value):
        assert index in range(0, len(self)), "Array subscript out of range."
        
        if value == self._clear:
            if self._isNodePresent(index, True):
                return False
            return False
                
        curNode = self._elements
        preNode = None
        
        while curNode is not None and curNode.index < index:
            preNode = curNode
            curNode = curNode.next
            
        if curNode is not None:
            if curNode.index == index:
                curNode.value = value
                return False
            elif preNode is None:
                newNode = _SparseArrayNode(index, value)
                newNode.next = curNode
                self._elements = newNode
            else:
                newNode = _SparseArrayNode(index, value)
                preNode.next = newNode
                newNode.next = curNode
        else:
            newNode = _SparseArrayNode(index, value)
            if preNode is not None:
                preNode.next = newNode
            else:
                self._elements = newNode
                
        self._size += 1
        return True
    
    def _isNodePresent(self, index, toDelete = False):
        curNode = self._elements
        preNode = None
        while curNode is not None and curNode.index != index:
            preNode = curNode
            curNode = curNode.next
           
        if curNode is not None:
            if toDelete:
                if preNode is None:
                    self._elements = curNode.next
                    del curNode
                else:
                    preNode.next = curNode.next
                    del curNode
                
                return True
            else:
                return True
            
        return False

    def __getitem__(self, index):        
        assert index in range(0, len(self)), "Array subscript out of range."
        curNode = self._elements
        
        while curNode is not None and curNode.index < index:
            curNode = curNode.next
            
        if curNode is not None:
            if curNode.index == index:
                return curNode.value
        return self._clear
    
    def __iter__(self):
        self._ndx = self._elements
        self._iterndx = 0
        return self
    
    def iterNode(self):
        return _nodeSparseArrayIterator(self._elements)
    
    
    def __next__(self):
        if self._iterndx < len(self):                    
            if self._ndx is not None and self._ndx.index == self._iterndx:
                value = self._ndx.value
                self._ndx = self._ndx.next
            else:
                value = self._clear
            
            self._iterndx += 1
            return value
        else:
            raise StopIteration      
        
    def clear(self, value):
        curNode = self._elements
        while curNode is not None:
            node = curNode
            curNode = curNode.next
            del node
        self._elements = None
        self._clear = value
        
    def __contains__(self, target):
        if self._size == 0 and self._clear != target:
            return False
        if self._size < len(self) and self._clear == target:
            return True
        for i in self:
            if i == target:
                return True
        else:
            return False
        
    def count(self, target):
        count = 0
        if not target in self:
            return count
        else:
            for i in self:
                if i == target:
                    count += 1
        
        if target == self._clear:
            count += (len(self) - self._size)
            
        return count
    
    
    
    def __str__(self):
        S = '['
        curNode = self._elements
        index = 0
        
        for i in range(len(self)):
            if curNode is not None and i == curNode.index:
                S += (str(curNode.value) + ', ')
                curNode = curNode.next
            else:
                S += (str(self._clear) + ', ')
                
        S = S[:-2]
        S += ']'
        return S
    
    def __repr__(self):
        return str(self)
    
    def copy(self):
        X = SparseArray(len(self))
        X.clear(self._clear)
        
        curNode = self._elements
        while curNode is not None:
            X [curNode.index] = curNode.value
        
        return X
    
    
class _nodeSparseArrayIterator(object):
    
    def __init__(self, theElements = None):
        self._theElements = theElements
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._theElements is not None:
            node = self._theElements
            self._theElements = self._theElements.next
            return node
        else:
            raise StopIteration

class SparseArrayDir(object):
    
    def __init__(self, size):
        self._length = size
        self._size = 0
        self._elements = _od()
        self._clear = 0
        self._ndx = 0
        
    def __len__(self):
        return self._length
    
    def size(self):
        return self._size
    
    def __setitem__(self, index, value):
        assert isinstance(index, int) and index in range(0, len(self)), "Invalid index for an array subscript."
        if value != self._clear:
            self._elements[index] = value
            self._size += 1
        else:
            if index in self._elements:
                self._elements.pop(index)
                self._size -= 1
                
                
    def __getitem__(self, index):
        assert isinstance(index, int) and index in range(0, len(self)), "Invalid index for an array subscript."
        if index in self._elements:
            return self._elements[index]
        else:
            return self._clear
        
    def __contains__(self, target):
        return target in self._elements.values()
    
    def clear(self, value):
        self.clear = value
        self._elements.clear()
        
    def count(self, target):
        L = list(self._elements.values())
        count = L.count(target)
        
        if target == self._clear:
            return (count + len(self) - self.size())
        else:
            return count
    
    def __str__(self):
        S = '['
        
        for i in range(len(self)):
            S += (str(self.__getitem__(i)) + ', ')
                
        S = S[:-2]
        S += ']'
        return S
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._ndx < len(self):
            self._ndx += 1
            return self.__getitem__(self._ndx)
        else:
            raise StopIteration
    
    def iterNode(self):
        return nodeIteratorSparseDir(self._elements)
    
    
class nodeIteratorSparseDir(object):
    
    def __init__(self, SparseDict = _od()):
        self._SparseDict = SparseDict
        self._list = self._SparseDict.keys()
        self._ndx = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self._SparseDict[self._ndx]
        index = self._ndx
        self._ndx += 1
        return index, value

if __name__ == '__main__':
    X = SparseArray(50)
