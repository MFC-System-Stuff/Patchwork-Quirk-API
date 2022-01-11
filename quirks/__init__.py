from .utils import Quirk, Instructions, Variables

class CStr(object):
    def __init__(self, sep="", lot=[], prefix=None, **kwargs):
        BASE_FORMATTING_RULES = {
          "QH":"Quirk Holder",
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
        return CStr("IF", (statement, condition), "THEN", **kwargs)

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
    C.FMT("Raise >QH<'s hair"),
    C.FMT("Make >QH<'s eyes glow red")
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
    C.FMT("Amplify >QH<'s voice to VOLUME")
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
    C.IF(C.AND(">QH< has Quirk", "Quirk is not >Q<", Q="One For All"), "boost quirk with stockpiled energy"),
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


GravityPull = Quirk( # Inko's quirk
  name="Gravity Pull",
  conditions=Instructions(
    C.FMT("Hands angled towards >T<", T="Object"),
    "Gesture for object to 'come here'"
  ),
  peffects=Instructions(
    C.FMT("Manipulate >T<'s gravity to float towards >QH<", T="Object")
  ),
  seffects=Instructions(
  ),
  deactivation=Instructions(
    C.FMT("Stop motioning to >T<", T="Object")
  ),
  vars=Variables(
  )
)
