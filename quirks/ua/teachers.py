from ..utils import Quirk, Variables, Instructions
from .. import CStr, C

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
    C.FMT("Looking at >T<"),
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