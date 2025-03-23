import sys

class Racer:
    def __init__(self, name1, name2, racer_id):
        # Shranimo ime, priimek in številko tekmovalca
        self.name1 = name1  
        self.name2 = name2  
        self.id = racer_id  

        # Časi na posameznih delih proge
        self.s1 = ""  # Split1 čas
        self.s2 = ""  # Split2 čas
        self.sf = ""  # Ciljni čas

        # Oblikujemo številko tekmovalca na 5 mest
        self.sid = f"{self.id:05d}"

        # Mesta po rezultatih
        self.rank1 = 0
        self.rank2 = 0
        self.rankf = 0

    def __lt__(self, other):
        # Razvrstitev po priimku, če je isti, pa po imenu
        if self.name2 == other.name2:
            return self.name1 < other.name1
        return self.name2 < other.name2

    def __repr__(self):
        # Predstavitev tekmovalca za debug
        return f"Racer({self.name1}, {self.name2}, {self.id}, {self.s1}, {self.s2}, {self.sf})"

    def __str__(self):
        # Oblikovan izpis podatkov o tekmovalcu
        return f"{(self.name2 + ', ' + self.name1):<20}{self.sid:>10}{self.s1:>10}{self.rank1:>10}{self.s2:>10}{self.rank2:>10}{self.sf:>10}{self.rankf:>10}"


def main():
    while True:
        # Preberemo število tekmovalcev
        line = sys.stdin.readline().strip()
        if not line:
            break

        num_racers = int(line)
        if num_racers == 0:
            break

        # Ustvarimo slovar in seznam za tekmovalce
        racers_dict = {}
        racers_list = []

        # Preberemo podatke o tekmovalcih
        for _ in range(num_racers):
            parts = sys.stdin.readline().strip().split()
            n1, n2, rid = parts[0], parts[1], int(parts[2])
            r = Racer(n1, n2, rid)
            racers_dict[rid] = r
            racers_list.append(r)

        # Preberemo čase tekmovalcev
        for _ in range(num_racers * 3):
            parts = sys.stdin.readline().strip().split()
            rid, rtype, rtime = int(parts[0]), parts[1], parts[2]
            if rtype == "S1":
                racers_dict[rid].s1 = rtime  # Čas prvega dela
            elif rtype == "S2":
                racers_dict[rid].s2 = rtime  # Čas drugega dela
            elif rtype == "F":
                racers_dict[rid].sf = rtime  # Čas cilja

        # Razvrstimo po Split1 času in določimo uvrstitve
        racers_list.sort(key=lambda r: r.s1)
        racers_list[0].rank1 = 1
        for i in range(1, num_racers):
            if racers_list[i].s1 == racers_list[i - 1].s1:
                racers_list[i].rank1 = racers_list[i - 1].rank1
            else:
                racers_list[i].rank1 = i + 1

        # Razvrstimo po Split2 času in določimo uvrstitve
        racers_list.sort(key=lambda r: r.s2)
        racers_list[0].rank2 = 1
        for i in range(1, num_racers):
            if racers_list[i].s2 == racers_list[i - 1].s2:
                racers_list[i].rank2 = racers_list[i - 1].rank2
            else:
                racers_list[i].rank2 = i + 1

        # Razvrstimo po ciljnem času in določimo uvrstitve
        racers_list.sort(key=lambda r: r.sf)
        racers_list[0].rankf = 1
        for i in range(1, num_racers):
            if racers_list[i].sf == racers_list[i - 1].sf:
                racers_list[i].rankf = racers_list[i - 1].rankf
            else:
                racers_list[i].rankf = i + 1

        # Razvrstimo tekmovalce po imenih
        racers_list.sort()

        # Izpišemo naslovno vrstico tabele
        print(f"{'NAME':<20}{'BIB':>10}{'SPLIT1':>10}{'RANK':>10}{'SPLIT2':>10}{'RANK':>10}{'FINISH':>10}{'RANK':>10}")
        
        # Izpišemo podatke o vseh tekmovalcih
        for r in racers_list:
            print(str(r))
        
        # Izpišemo prazno vrstico med testnimi primeri
        print()


if __name__ == "__main__":
    main()
