class SeriNum:

    YIL = 22

    def __init__(self, barkod, isEmri, hafta, adet) -> None:
        self.barkod = barkod
        self.isEmri = isEmri
        self.hafta = hafta
        self.adet = adet

    def is_emri(self, isemri):
        return isemri[-5:]

    def printe(self):
        print("-"*50)
        s = f"{self.barkod}M{self.is_emri(self.isEmri)}{self.YIL}{self.hafta}{self.adet:>04}"
        print(s)
        print(len(s))
        print("-"*50)