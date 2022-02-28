class TooManyPatches(Exception):
    pass

class Variables(object):
    def __init__(self, vars=[], values=[]):
        self._vars = vars
        self._indent_multiplier = 2
        self.vars = []
        for var, val in zip(vars, values):
            setattr(self, var, val)
            setattr(getattr(self, var), 'name', var)
            self.vars.append(var)

    def __str__(self):
        tmp = ""
        for var in self.vars:
            tmp += ("  "*self._indent_multiplier+"⟩ "+var+" = "+str(getattr(self, var))+" ⟨\n")
        return tmp


class Instructions(object):
    def __init__(self, *instructions):
        self.instructions = [*instructions]
        self.is_patched = False
        self.original_instrutions = instructions
        self.from_index = None
        self.to_index = None
        self._indent_multiplier = 2

    def imitate(self, *indexes):
        return [self.instructions[i] for i in indexes]

    def mosaic(self, from_index, to_index, *instructions):
        self.is_patched = True
        self.from_index = from_index
        self.to_index = to_index

        counter = 0
        if not len(self.instructions):
            for i in range(from_index, to_index+1):
                self.instructions.append("")
        for i in range(from_index, to_index+1):
            self.instructions[i] = instructions[counter]
            counter += 1

    def __str__(self) -> str:
        tmp = ""
        if self.is_patched:
            for i in self.instructions:
                index = self.instructions.index(i)
                if (self.from_index > index and self.to_index < index) or (self.from_index == self.to_index and self.from_index == index):
                    tmp += ("  "*self._indent_multiplier+"⟩ "+i+" ⟨ PATCHED\n")
                elif self.from_index == index:
                    tmp += ("  "*self._indent_multiplier+"⟩ "+i+" ⟨ PATCH START\n")
                elif self.to_index == index:
                    tmp += ("  "*self._indent_multiplier+"⟩ "+i+" ⟨ PATCH END\n")
                else:
                    tmp += ("  "*self._indent_multiplier+"⟩ "+i+" ⟨\n")
            return tmp
        for i in self.instructions:
            tmp += ("  "*self._indent_multiplier+"⟩ "+i+" ⟨\n")
        return tmp


Quirks = []

class Quirk(object):
    def __init__(self, name="Base Quirk", description=None, conditions=Instructions(), peffects=Instructions(), seffects=Instructions(), deactivation=Instructions(), vars=Variables(), limit=100):
        self.name = name
        self.description = description
        self.conditions = conditions
        self.peffects = peffects
        self.seffects = seffects
        self.deactivation = deactivation
        self.vars = vars
        self.instructions_count = len(conditions.instructions) + len(peffects.instructions) + len(seffects.instructions) + len(deactivation.instructions)
        if limit < self.instructions_count:
            raise TooManyPatches(f"You have attempted to add {self.instructions_count} patches, when you can only have a maximum of {limit}.")

        Quirks.append(self)

    def __str__(self) -> str:
        im = (self.vars._indent_multiplier, self.conditions._indent_multiplier, self.peffects._indent_multiplier, self.seffects._indent_multiplier, self.deactivation._indent_multiplier)

        self.vars._indent_multiplier = self.conditions._indent_multiplier = self.peffects._indent_multiplier = self.seffects._indent_multiplier = self.deactivation._indent_multiplier = 2
        tmp = self.name+" ->\n"
        if self.description:
            tmp += "  Description -> \"{str(self.description)}\""
        if len(self.vars.vars):
            tmp += "  Variables ->\n"+str(self.vars)+"\n"
        if len(self.conditions.instructions):
            tmp += "  Trigger Conditions ->\n"+str(self.conditions)+"\n"
        tmp += "  Primary Effects ->\n"+str(self.peffects)+"\n"
        if len(self.seffects.instructions):
            tmp += "  Secondary Effects ->\n"+str(self.seffects)+"\n"
        if len(self.deactivation.instructions):
            tmp += "  Deactivation ->\n"+str(self.deactivation)
        self.vars._indent_multiplier, self.conditions._indent_multiplier, self.peffects._indent_multiplier, self.seffects._indent_multiplier, self.deactivation._indent_multiplier = im[0], im[1], im[2], im[3], im[4]
        return tmp
