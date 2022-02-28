from .utils import Quirk, Instructions, Variables

class CStr(object):
    def __init__(self, sep="", lot=[], prefix=None, **kwargs):
        BASE_FORMATTING_RULES = {
          "QH":"Quirk Holder",
          "T": "Target",
        }
        BASE_FORMATTING_RULES.update(**kwargs)
        self.kwargs = BASE_FORMATTING_RULES
        self.sep = sep
        self.lot = lot
        self.prefix = prefix

    def isolate(self): # Returns the list of traits as a list
        return self.lot

    def __str__(self):
        tmp = ""
        mindex = len(self.lot) - 1
        for i in self.lot:
            tmp += str(i)
            if self.lot.index(i) != mindex:
                tmp += f' {self.sep} '
        if self.prefix:
            tmp = self.prefix + ' ' + tmp
        for key in self.kwargs:
            tmp = tmp.replace('>'+key+'<', self.kwargs[key])
        return tmp

    def __repr__(self):
        return f"CStr({self.sep.__repr__()}, {self.lot.__repr__()})"

    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)


class C(object):
    def FMT(*statements, **kwargs):
        return CStr(lot=statements, **kwargs)

    def OR(*statements, **kwargs):
        return CStr("OR", statements, **kwargs)

    def AND(*statements, **kwargs):
        return CStr("AND", statements, **kwargs)

    def IF(condition, statement, **kwargs):
        return CStr("THEN", (condition, statement), "IF", **kwargs)

    def SET(var, val):
        if isinstance(val, str):
            val = f'"{val}"'
        return f'SET {var} TO {val}'