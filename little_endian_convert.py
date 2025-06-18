def desinverser_trames(lines):
    trames_originales = []

    for line in lines:
        # Nettoyer la ligne, séparer les octets
        octets = line.strip().split()
        if len(octets) != 4:
            print(f"Ligne ignorée (non conforme): {line}")
            continue
        
        # Inverser l'ordre des octets (Little Endian -> Big Endian)
        octets_inverses = octets[::-1]
        # Convertir en chaîne hexadécimale
        hex_value = ''.join(octets_inverses).upper()
        trames_originales.append(hex_value)

    return trames_originales

# Exemple d'entrée
entree = """
08 01 00 00
""".strip().split('\n')

# Appel de la fonction
resultat = desinverser_trames(entree)

# Affichage du résultat
print("Trames désinversées :")
for trame in resultat:
    print(trame)
