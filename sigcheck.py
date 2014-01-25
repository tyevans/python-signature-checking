#!/usr/bin/python
import inspect

def typed(func):
    if not __debug__:
        return func

    argspec = inspect.getfullargspec(func)
    arg_types = []
    for key in argspec.args:
        arg_types.append(argspec.annotations.get(key, None))

    varargs_type = argspec.annotations.get(argspec.varargs, None)

    varkw_type = argspec.annotations.get(argspec.varkw, None)

    def inner(*args, **kwargs):
        for i, arg_type in enumerate(arg_types):
            if arg_type is not None and not isinstance(args[i], arg_type):
                raise TypeError("Call Did Not Match Signature", argspec.args[i], type(args[i]), args[i], arg_types[i])
        if varargs_type and len(args) > len(arg_types):
            for arg in args[i+1:]:
                if not isinstance(arg, varargs_type):
                    raise TypeError("vararg type", argspec.varargs, type(args[i]), args[i], arg_types[i])
        if varkw_type:
            for key, value in kwargs.items():
                if not isinstance(value, varkw_type):
                    raise TypeError("kwarg type", key, value, varkw_type)
        return func(*args, **kwargs)
    return inner
