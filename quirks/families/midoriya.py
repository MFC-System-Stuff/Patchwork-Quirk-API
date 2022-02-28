from ..utils import Quirk, Variables, Instructions
from .. import CStr, C

# Quirk Variables go here
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


Attraction = Quirk( # Inko's quirk
  name="Attraction",
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