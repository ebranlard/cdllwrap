from __future__ import print_function
import sys
from ctypes import *
import unittest
import os

from cdllwrap import *


def test_lib(libfile,headerfile):

    print('Called with: ',libfile,headerfile)
    if not os.path.exists(libfile):
        raise Exception('File not found:',libfile)
    if not os.path.exists(headerfile):
        raise Exception('File not found:',headerfile)

    libfile='./'+libfile # TODO
    #lib = cdll.LoadLibrary('./'+libfile) # TODO
    ##A=lib.testlib_getdb(
    #print(lib)
    #print(type(A))

    print('Loading  : ', libfile)
    lib=WrapLib(libfile)

    # Simple call
    lib.call('testlib_print_version')

    # Getting an int
    myint = lib.call('testlib_getint')
    print('>>GetInt  :',myint)

    # Getting a double
    mydb  = lib.call_db('testlib_getdb')
    print('>>GetDB   :',mydb)
    
    # Getting a string, option 1:
    version=create_string_buffer(30)
    lib.call('testlib_get_version',version)
    print('>> Version:',version.value)

    # Getting a string, option 2:
    version=create_string_buffer(b' '*30)
    lib.call('testlib_get_version',version)
    print('>> Version:',version.value)

    # Passing a string
    inputfile=create_string_buffer(b'Inputfile.inp')
    res=lib.call('testlib_init',inputfile)
    print('>>InitCall:',res==1)

    # Passing doubles, getting a double
    add = lib.call_db('testlib_add', byref(to_c(12.0)),byref(to_c(100.0))) 
    print('>>Result  :',add)

    # Passing arrays in and out
    n=4
    x    = np.zeros(n) ;
    y    = np.zeros(n) ;
    z    = np.zeros(n) ;
    x=x+12
    y=y+100
    x_c    = to_c(x) ;
    y_c    = to_c(y) ;
    z_c    = to_c(z) ;
    lib.call('testlib_addvec',byref(x_c),byref(y_c),byref(z_c),to_c_intp(n))
    x    = c_to_py(x_c,x) ;
    y    = c_to_py(y_c,y) ;
    z    = c_to_py(z_c,z) ;
    print('>>AddVec  :',z)


if __name__ == "__main__":
    header=''
    if len(sys.argv)>1:
        libfile=sys.argv[1]
    if len(sys.argv)>2:
        headerfile=sys.argv[2]

    test_lib(libfile,headerfile)

#     else:
#         print('Provide one argument')
#     import sys
