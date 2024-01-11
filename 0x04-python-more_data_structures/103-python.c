#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *element;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *trying_str;
	unsigned char *bytes_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	trying_str = PyBytes_AsString(p);
	bytes_str = (unsigned char *)trying_str;
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", trying_str);

	printf("  first %zd bytes:", size > 10 ? 10 : size + 1);
	for (i = 0; i < 10 && i < size; i++)
	{
		printf(" %02x", bytes_str[i]);
	}
	if (size >= 10)
	{
		printf(" %02x", bytes_str[10]);
	}
	printf("\n");
}
