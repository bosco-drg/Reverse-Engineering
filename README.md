# 🔬 USB Hacking – Aaronia BPSG 6 Signal Generator

<!--portfolio
{
  "id": "superproject",
  "repo": "https://github.com/bosco-drg/Reverse-Engineering",
  "images": [
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/generator_aaronia.png",
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/generator_aaronia.png"
  ],
  "tags": ["tag_maintenance", "tag_maintenance", "tag_maintenance"],
  "title_fr": "Super Projet",
  "title_en": "Super Project",
  "short_desc_fr": "Un projet innovant pour le portfolio.",
  "short_desc_en": "An innovative project for the portfolio.",
  "desc_fr": "Ce projet démontre l'intégration de matériel et de logiciel pour une solution IoT complète.",
  "desc_en": "This project demonstrates the integration of hardware and software for a complete IoT solution.",
  "sections": [
    {
      "type": "text",
      "value": ["project_superproject_desc"]
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/generator_aaronia.png",
      "caption_i18n": "project_superproject_img_caption1"
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/generator_aaronia.png",
      "caption_i18n": "project_superproject_img_caption2"
    }
  ]
}
-->

<p align="center">
  <img src="docs/img/generator_aaronia.png" alt="Aaronia BPSG 6" />
</p>

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
