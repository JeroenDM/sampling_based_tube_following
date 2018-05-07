# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_graph', [dirname(__file__)])
        except ImportError:
            import _graph
            return _graph
        if fp is not None:
            try:
                _mod = imp.load_module('_graph', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _graph = swig_import_helper()
    del swig_import_helper
else:
    import _graph
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class dijkstraSortFunction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dijkstraSortFunction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dijkstraSortFunction, name)
    __repr__ = _swig_repr

    def __call__(self, n1, n2):
        return _graph.dijkstraSortFunction___call__(self, n1, n2)

    def __init__(self):
        this = _graph.new_dijkstraSortFunction()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _graph.delete_dijkstraSortFunction
    __del__ = lambda self: None
dijkstraSortFunction_swigregister = _graph.dijkstraSortFunction_swigregister
dijkstraSortFunction_swigregister(dijkstraSortFunction)
cvar = _graph.cvar
INF = cvar.INF

class Graph(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Graph, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Graph, name)
    __repr__ = _swig_repr

    def add_data_column(self, mat):
        return _graph.Graph_add_data_column(self, mat)

    def print_graph_data(self):
        return _graph.Graph_print_graph_data(self)

    def init(self):
        return _graph.Graph_init(self)

    def reset(self):
        return _graph.Graph_reset(self)

    def run_dijkstra(self):
        return _graph.Graph_run_dijkstra(self)

    def run_bfs(self):
        return _graph.Graph_run_bfs(self)

    def get_path(self, vec):
        return _graph.Graph_get_path(self, vec)

    def get_path_cost(self):
        return _graph.Graph_get_path_cost(self)

    def print_path(self):
        return _graph.Graph_print_path(self)

    def print_graph(self):
        return _graph.Graph_print_graph(self)

    def set_graph_data(self, data):
        return _graph.Graph_set_graph_data(self, data)

    def __init__(self):
        this = _graph.new_Graph()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _graph.delete_Graph
    __del__ = lambda self: None
Graph_swigregister = _graph.Graph_swigregister
Graph_swigregister(Graph)

# This file is compatible with both classic and new-style classes.

