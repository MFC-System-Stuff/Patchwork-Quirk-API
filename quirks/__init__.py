from .utils import Quirk, Instructions, Variables

class CStr(object):
    def __init__(self, sep="", lot=[], prefix=None, **kwargs):
        self.kwargs = kwargs
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


'''
class VStr(object):
    def __init__(self, text, **kwargs):
        self.kwargs = kwargs
        self.text = text

    def __str__(self):
        tmp = self.text
        for key in self.kwargs:
            tmp = tmp.replace('>'+key+'<', self.kwargs[key])
        return tmp

    def __repr__(self):
        return f"VStr({self.text.__repr__()}, **{self.kwargs})"

    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)
'''


class C(object):
    QUIRK_HOLDER = "Quirk Holder"

    def OR(*statements, **kwargs):
        return CStr("OR", statements, **kwargs)

    def AND(*statements, **kwargs):
        return CStr("AND", statements, **kwargs)

    def IF(condition, statement, **kwargs):
        return CStr("THEN", (statement, condition), "IF", **kwargs)

    def SET(var, val):
        if isinstance(val, str):
            val = f'"{val}"'
        return f'SET {var} TO {val}'


# Quirk Variables go here
class Volume(object):
    def __init__(self, vol=100): # 100% is normal, 1% is whispering as quiet as possible, 1000% is the loudest possible
        self.vol = vol

    def __str__(self):
        return str(self.vol)+"%"

    def volume(self, vol=100):
        self.vol = vol


class Stockpile:
    def __init__(self, holder_num):
        self.base = 1
        self.holder_num = holder_num
        self.stock = 1
        for _ in range(1, holder_num):
            self.stock *= 2

    def __str__(self):
        return str(self.stock)


# Quirk Definitions go here
Erasure = Quirk(
  name="Erasure",
  conditions=Instructions(
    "Unbroken eye contact with Target",
    "Intent to activate the quirk"
  ),
  peffects=Instructions(
    "Find quirk genes",
    "Prevent access to quirk genes"
  ),
  seffects=Instructions(
    CStr("Raise >QH<'s hair", QH=C.QUIRK_HOLDER),
    CStr("Make >QH<'s eyes glow red", QH=C.QUIRK_HOLDER)
  ),
  deactivation=Instructions(
    C.OR("Intent to deactivate the quirk", "Blink")
  )
)


Voice = Quirk(
  name="Voice",
  conditions=Instructions(
    C.AND("Deep breath taken", "yell")
  ),
  peffects=Instructions(
    CStr("Amplify >QH<'s voice to VOLUME", QH=C.QUIRK_HOLDER)
  ),
  deactivation=Instructions(
    "Stop shouting"
  ),
  vars=Variables(
    ("Volume",),
    (Volume(),)
  )
)


OneForAll = Quirk(
  name="One For All (9th iteration)",
  conditions=Instructions(
    C.OR("'Clench your buttcheeks and yell SMASH'", "Concentration")
  ),
  peffects=Instructions(
    C.IF(C.AND(">QH< has Quirk", "Quirk is not >Q<", QH=C.QUIRK_HOLDER, Q="One For All"), "boost quirk with stockpiled energy"),
    "Enhance body with stockpiled energy"
  ),
  seffects=Instructions(
    "Red lightning over body",
    "Sparks over body"
  ),
  deactivation=Instructions(
    "Relax"
  ),
  vars=Variables(
    ("Stockpile",),
    (Stockpile(9),)
  )
)


GravityPull = Quirk(
  name="Gravity Pull",
  conditions=Instructions(
    "{QH} must angle hands towards object"
  ),
  peffects=Instructions(
    ""
  ),
  seffects=Instructions(
    ""
  ),
  deactivation=Instructions(
    ""
  ),
  vars=Variables(
  )
)
