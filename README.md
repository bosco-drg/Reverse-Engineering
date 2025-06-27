# 🔬 USB Hacking – Reverse Engineering du Générateur de Signaux Aaronia BPSG 6

<p align="center">
  <img src="docs/img/generator_aaronia.png" alt="Aaronia BPSG 6" width="400"/>
</p>

## 📖 Introduction

Ce projet vise à rétroconcevoir le protocole de communication USB du générateur de signaux RF **Aaronia BPSG 6**, un appareil professionnel couvrant la plage 23.5 MHz - 6 GHz. Le fabricant ne fournit aucune documentation API, et son logiciel propriétaire est limité aux plateformes x86 avec interface graphique, le rendant inutilisable sur des systèmes embarqués comme le Raspberry Pi.

Notre solution open-source permet un contrôle complet via USB en Python, notamment :
- Réglage précis de la fréquence (mode Integer-N et Fractional-N)
- Configuration de la puissance de sortie
- Pilotage sans interface graphique (SSH, scripts automatisés)

## 🛠️ Méthodologie de Reverse Engineering

### 1. Identification du Périphérique USB
- **Outils** : `lsusb`, `dmesg`, `usbmon`
- **Identifiants** :
  - Vendor ID: `0x04d8`
  - Product ID: `0xf3b5`
- **Type** : Appareil HID (Human Interface Device), permettant une compatibilité native sans drivers spécifiques.

### 2. Capture et Analyse des Trames USB
- **Outils** : Wireshark avec filtres ciblés (`usb.bus_id == 1 && usb.device.address == 10`)
- **Structure des Trames** :
  ```plaintext
  [En-tête 12 octets] | [Registres SPI (24 octets)] | [Commande Gain (5 octets)] | [Padding]
  ```
  - **En-tête** : Constante pour un modèle donné (ex: `19 03 04 05 06 07 08 ff 00 00 00 00`)
  - **Registres SPI** : Configuration de la PLL MAX2870 (6 registres de 4 octets en little-endian)
  - **Commande Gain** : Octets modifiés lors du réglage de puissance (encodage non documenté)

### 3. Décodage de la PLL MAX2870
La fréquence est générée par une boucle à verrouillage de phase (PLL) **MAX2870**, configurée via 6 registres :
- **Registre 0** : Mode (Integer/Fractional-N), valeurs N et F
- **Registre 1** : Paramètres du Charge Pump et modulus (M)
- **Registre 4** : Diviseur de sortie (DIVA) et puissance RF

Exemple de calcul pour 2 GHz :
```python
f_out = 2000e6  # 2 GHz
registers = generate_spi_registers(f_out, int_n=False)
# Output: ['80003200', '42E80019', 'C0400C93', '00000013', '630000E4', '00040000']
```

## 💻 Fonctionnalités Implémentées

### Pilotage de la Fréquence
- Prise en charge des modes **Integer-N** (stabilité) et **Fractional-N** (précision)
- Calcul automatique des paramètres PLL (N, F, DIVA) via `generate_spi_registers()`
- Plage couverte : 23.5 MHz - 6 GHz avec résolution <1 Hz

### Contrôle du Gain (Partiel)
- Encodage partiellement reverse-engineeré (valeurs empiriques)
- 4 niveaux de gain disponibles (0-3)

### Exemple d'Utilisation
```bash
# Générer un signal à 1.5 GHz avec gain maximal
python send_trame_usb.py 1500 3
```

## 📂 Structure du Projet
```
.
├── generate_spi.py          # Génération des registres PLL
├── send_trame_usb.py       # Construction des trames USB
├── usb.py                  # Communication HID avec l'appareil
├── docs/                   # Captures d'écran et schémas
└── README.md               # Ce document
```

## 🔍 Résultats et Perspectives
### ✅ Succès
- Contrôle complet de la fréquence via USB
- Compatibilité avec Linux/ARM (Raspberry Pi)
- Solution légère (<100 lignes de code Python)

### 🔴 Limitations
- Encodage du gain non entièrement décrypté
- Manque de calibration précise pour la puissance de sortie

### 🚀 Améliorations Futures
- Décodage complet du contrôle de gain par analyse statistique
- Interface Web/REST pour un contrôle distant
- Intégration avec GNU Radio pour des applications SDR

## 📝 Licence
Ce projet est à but éducatif et n'est pas affilié à Aaronia AG. Code publié sous licence MIT.

---

<p align="center">
  <em>Projet réalisé par Bosco de Rauglaudre & Yanis Bouzidi - BUT GEII 2024/2025</em>
</p>
