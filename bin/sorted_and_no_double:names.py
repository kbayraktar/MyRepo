with open('vornamen.txt', 'r') as f:
    vornamen = [line.strip() for line in f]

with open('nachnamen.txt', 'r') as f:
    nachnamen = [line.strip() for line in f]

vollstaendige_namen = set()
for vorname in vornamen:
    for nachname in nachnamen:
        vollstaendige_namen.add(f'{vorname} {nachname}')

vollstaendige_namen = sorted(list(vollstaendige_namen))

with open('vollstaendige_namen.txt', 'w') as f:
    for name in vollstaendige_namen:
        f.write(f'{name}\n')