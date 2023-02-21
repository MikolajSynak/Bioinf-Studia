x = input('Wpisz wypowiedź:  ')
wordd = x.split(" ")
długosc = [len(word) for word in wordd]
srednia = sum(długosc) / len(długosc)
print(f'Srednia długosci słów: {srednia}')