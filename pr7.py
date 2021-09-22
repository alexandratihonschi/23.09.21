v=[5438, 8765, 4637, 9847, 6352, 6479, 7463]
z=['Luni', 'Marti', 'Miercuri','Joi', 'Vineri', 'Sambata', 'Duminica']
print(sum(v), 'venitul saptamanal')
print(sum(v)/7, 'venitul zilnic mediu')
max=v.index(max(v))
print(z[max])
min=v.index(min(v))
print(z[min])