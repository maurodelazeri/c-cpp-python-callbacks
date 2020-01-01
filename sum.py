import ctypes
_sum = ctypes.CDLL('./libsum.so')
_sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def our_function(numbers):
    global _sum
    size = len(numbers)
    array_type = ctypes.c_int * size
    res = _sum.our_function(ctypes.c_int(size), array_type(*numbers))
    return int(res)

def myHello():
    global _sum
    return _sum.myHello()

def greater_than(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

callback_func = callback_type(greater_than)

def stamFunc():
    global _sum
    _sum.myFunc(callback_func)
