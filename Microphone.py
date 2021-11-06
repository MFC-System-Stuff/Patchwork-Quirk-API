from quirks.utils import Quirk, Instructions
from quirks import Erasure, Voice

print(Erasure, "\n")
print(Voice, "\n")

Conditions = Erasure.conditions.imitate(1)
Secondary = Erasure.seffects.imitate(0, 1)
Deactivation = Erasure.deactivation.imitate(0)

Voice.name = "Voice (Mosaic)"
Voice.conditions.mosaic(0, 0, *Conditions)
Voice.seffects.mosaic(0, 1, *Secondary)
Voice.deactivation.mosaic(0, 0, *Deactivation)

print(Voice, "\n")

Microphone = Quirk(
  name="Microphone (Quilt)",
  conditions=Instructions(*Conditions),
  peffects=Instructions(*Voice.peffects.imitate(0)),
  seffects=Instructions(),
  deactivation=Instructions(Deactivation[0].isolate()[0]),
  limit=8
)

print(Microphone)
