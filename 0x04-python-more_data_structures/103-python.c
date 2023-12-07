#!/usr/include/python3.4/bytesobject.h
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] Bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  Size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));
    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

    str = PyBytes_AsString(p);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", str[i]);
        if (i + 1 < size && i + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}
