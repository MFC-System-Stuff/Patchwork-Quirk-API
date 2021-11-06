from copy import copy

from quirks.utils import Quirk, Instructions
from quirks import Erasure, Voice

print(Erasure, "\n")
print(Voice, "\n")

Conditions = Erasure.conditions.imitate(1)
Secondary = Erasure.seffects.imitate(0, 1)
Deactivation = Erasure.deactivation.imitate(0)

VoiceM = copy(Voice)

VoiceM.name = "Voice (Mosaic)"
VoiceM.conditions.mosaic(0, 0, *Conditions)
VoiceM.seffects.mosaic(0, 1, *Secondary)
VoiceM.deactivation.mosaic(0, 0, *Deactivation)

print(VoiceM, "\n")

Microphone = Quirk(
  name="Microphone (Quilt)",
  conditions=Instructions(*Conditions),
  peffects=Instructions(*Voice.peffects.imitate(0)),
  seffects=Instructions(),
  deactivation=Instructions(Deactivation[0].isolate()[0]),
  vars=Voice.vars,
  limit=8
)

print(Microphone)
