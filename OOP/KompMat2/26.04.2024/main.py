from MilitaryObject import GeneralStaff, MilitaryBase
from Spy import Spy


class JamesBond(Spy):
    def __init__(self, name):
        super().__init__(name)

    def visit_general_staff(self, staff : GeneralStaff):
        print(self.name, staff.name)

    def visit_military_base(self, base: MilitaryBase):
        print(self.name, base.name)

class SecretAgent(Spy):
    def __init__(self, name):
        super().__init__(name)
    def visit_general_staff(self, staff:GeneralStaff):
        print(f"{self.name} дізнався що в {staff.name} {staff.secretPaper} сукретних паперів ")

    def visit_military_base(self,base:MilitaryBase):
        print(f"{self.name} дізнався що в {base.name} {base.officers} офіцерів , {base.jeeps} джипів, {base.tanks} танків, {base.soldiers} солдатів")

class Saboteur(Spy):
    def __init__(self, name):
        super().__init__(name)
    def visit_general_staff(self, staff:GeneralStaff):
        print(f"{self.name} знищив {staff.name} {staff.secretPaper} сукретних паперів і {staff.generals} ")
        staff.secretPaper = 0
        staff.generals = 0
    def visit_military_base(self,base:MilitaryBase):
        print(f"{self.name} знищив {base.name} {base.officers} офіцерів , {base.jeeps} джипів, {base.tanks} танків, {base.soldiers} солдатів")
        base.officers = 0
        base.soldiers = 0
        base.officers = 0
        base.tanks = 0




if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100, "Kremlin")
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20, "BNR")
    print(militaryBase)

    james = JamesBond("James Bond")
    generalStaff.accept(james)
    militaryBase.accept(james)

    Vasil = SecretAgent("Vasil")
    generalStaff.accept(Vasil)
    militaryBase.accept(Vasil)

    Kamikadze = Saboteur("Kamikadze")
    generalStaff.accept(Kamikadze)
    militaryBase.accept(Kamikadze)

    print(generalStaff, militaryBase)

