# C/C++ Programming


## Variable Argument Macros in C/C++

```
#define some_macro(A,B,...) called_func(A,B,__VA_OPT__(,) __VA_ARGS__)
```

`__VA_ARGS__` expands to the arguments. `__VA_OPT__` expands to the passed
string only if one of more variable arguments are passed. This allows you to
only add syntactic elements in the case they're need to support a non-empty
arguments block.

## Function pointers (std::bind)

`std::bind` is the mechanism used to create a function pointer with bound arguments in c++. 

### Member function pointers

The mechanism is useful for creating a function pointer to a member function of an object with the object instance embedded within the pointer. In this case the first bound argument should be the object:

```
class SomeClass {
  int some_function(int a);
};

SomeClass some_instance;

auto f=std::bind(&SomeClass:some_function,&some_instance);

```

### Function pointers with unbound arguments


### Return type

While the c++ specification does not give an explicit return type for `std::bind`, it can be stored using a `std::function<...>` with the correct template types.

## Function pointers (std::function)

Syntax:

```
std::function<SomeReturnType(SomeArgType0,SomeArgType1,...)>
```
