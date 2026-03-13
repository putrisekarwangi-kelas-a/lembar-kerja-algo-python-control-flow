import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

import math

print(math.sqrt(99))
print(math.pi)

import random

angka = random.randint(3, 60)
print("Angka acak:", angka)

from datetime import datetime

sekarang = datetime.now()
print("Waktu sekarang:", sekarang)

import random

nilai =  random.randint(30, 100)
print("Nilai:", nilai)

if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")