import pickle

with open("cities.bin", "rb") as dosya:
  cities =  pickle.load(dosya)
  print(cities)

