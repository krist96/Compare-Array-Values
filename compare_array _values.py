class My(object):
    def __init__(self, tab, string):
        self.tab = tab
        self.string = string

    def task2(self):
        tab = self.tab #Tworzymy wewnetrzne zmienną tablicową
        n = self.string #Tworzymy wewnetrzne zmieną z wartością informacyjną o ostatnim elemencie
        tab.sort() #sortujemy wejściową tabelę

        ##Funkcja Sprawdzająca, i wypisująca brakujące elementy talicy
        def rek(i):   
            if(i <= n): #Sprawdzamy czy i jest równe 10
                if (tab.count(i) < 1):
                    print(i)
                rek(i+1)  #Rekurencyjnie wywołujemy funkcję z wartością podniesioną o jeden
        ##Wywołujemy powyższą funkcję
        rek(1)

my = My([2,3,7,4,9], 10)
my.task2()
