vornamen = ['Emma', 'Ben', 'Mia', 'Noah', 'Hannah', 'Finn', 'Emilia', 'Elias', 'Anna', 'Leon']
nachnamen = ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Schulz', 'Hoffmann']

with open('vornamen.txt', 'w') as f:
    for vorname in vornamen:
        f.write(f'{vorname}\n')

with open('nachnamen.txt', 'w') as f:
    for nachname in nachnamen:
        f.write(f'{nachname}\n')

