# Erstelle python code, dass aus einer Datei mit 10 Vornamen liest und aus einer Datei mit 10 Nachnnamen liest. Aus diesen 10 Vornamen und 10 Nachnamen sollen 10 vollständige Namen ezeugt werden und in einer dritten Datei ausgegeben werden.

with open('vornamen.txt', 'r') as f:
    vornamen = [line.strip() for line in f]

with open('nachnamen.txt', 'r') as f:
    nachnamen = [line.strip() for line in f]

vollstaendige_namen = set()
for vorname in vornamen:
    for nachname in nachnamen:
        vollstaendige_namen.add(f'{vorname} {nachname}')

with open('vollstaendige_namen.txt', 'w') as f:
    for name in vollstaendige_namen:
        f.write(f'{name}\n')
