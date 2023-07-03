with open('vornamen.txt', 'r') as f:
    vornamen = [line.strip() for line in f]

with open('nachnamen.txt', 'r') as f:
    nachnamen = [line.strip() for line in f]

vollstaendige_namen = []
for vorname, nachname in zip(vornamen, nachnamen):
    vollstaendige_namen.append(f'{vorname} {nachname}')

vollstaendige_namen = sorted(vollstaendige_namen)

with open('vollstaendige_namen.txt', 'w') as f:
    for name in vollstaendige_namen[:10]:
        f.write(f'{name}\n')
