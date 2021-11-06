from .utils import Quirk, Instructions, Variables

class CStr(object):
    def __init__(self, sep, lot):
        self.sep = sep
        self.lot = lot

    def isolate(self): # Returns the list of traits as a list
        return self.lot

    def __str__(self):
        mindex = len(self.lot) - 1
        tmp = ""
        for c in self.lot:
            tmp += c
            if self.lot.index(c) != mindex:
                tmp += ' ' + self.sep + ' '
        return tmp

    def __repr__(self):
        return f"CStr({self.sep.__repr__()}, {self.lot.__repr__()})"

    def __add__(self, other):
        return str(self) + other
    def __radd__(self, other):
        return other + str(self)


class C(object):
    QUIRK_HOLDER = "Quirk Holder"

    def OR(*conditions):
        return CStr("OR", conditions)

    def AND(*conditions):
        return CStr("AND", conditions)

    def THEN(condition, statement):
        return CStr("THEN", (condition, statement))

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
    f"Raise {C.QUIRK_HOLDER}'s hair",
    f"Make {C.QUIRK_HOLDER}'s eyes glow red"
  ),
  deactivation=Instructions(
    C.OR("Intent to deactivate the quirk", "Blink")
  )
)


Voice = Quirk(
  name="Voice",
  conditions=Instructions(
    C.THEN("Take a deep breath", "shout loudly")
  ),
  peffects=Instructions(
    f"Amplify {C.QUIRK_HOLDER}'s voice to VOLUME"
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
  name="One For All",
  conditions=Instructions(
  ),
  peffects=Instructions(
  ),
  seffects=Instructions(
  ),
  deactivation=Instructions(
  ),
  vars=Variables(
  )
)

