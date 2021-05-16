import numpy
from cffi import FFI

ffi = FFI()

ffi.cdef("""
void single_test(double *x , int n);
""")
C  = ffi.dlopen("./simple.so")

def single_test_a(x):
    C.single_test(ffi.cast("double *", x.ctypes.data), len(x))

x = numpy.linspace(1,10,10).astype('float64')
print("Before single" ,x)
single_test_a(x)
print("After single", x)