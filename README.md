# 🔬 USB Hacking – Aaronia BPSG 6 Signal Generator

![Aaronia BPSG 6](docs/img/generator_aaronia.png)

Ce projet vise à rétroconcevoir le protocole de communication USB utilisé par le générateur de signaux RF Aaronia BPSG 6. Le fabricant ne fournit aucune documentation API, et le logiciel officiel n'est disponible que pour les plateformes x86 avec une interface graphique, ce qui le rend inutilisable sur des systèmes sans écran comme le Raspberry Pi.  
Notre objectif est de créer un outil open-source en ligne de commande (Python) pour contrôler les fonctions de base du générateur (fréquence, puissance de sortie) via USB, le rendant ainsi accessible pour des applications embarquées ou à distance.

---

## 🚀 Objectifs

- Comprendre le protocole USB utilisé par le BPSG 6
- Capturer et analyser les paquets USB du logiciel propriétaire
- Développer une interface Python multiplateforme pour piloter le générateur
- Permettre l'utilisation sur des systèmes headless ou ARM (ex : Raspberry Pi)

## 🔧 Outils utilisés

- `Wireshark`
- `usbmon`
- `PyUSB`
- `lsusb`
- `dmesg`

---

> Ce projet est à but éducatif et n'est pas affilié à Aaronia AG.
