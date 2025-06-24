# 🔬 USB Hacking – Aaronia BPSG 6 Signal Generator

# Projet Ultra Complet

Bienvenue sur le projet ultra complet, conçu pour tester toutes les fonctionnalités de l'import automatique de portfolio.

<!--portfolio
{
  "id": "ultracomplet",
  "repo": "https://github.com/bosco-drg/ultra-complet",
  "date": "2024-07-01",
  "images": [
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
    "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png"
  ],
  "tags": [
    "python", "iot", "hardware", "web", "ai", "robotics", "opensource", "cloud", "devops", "security"
  ],
  "title_fr": "Projet Ultra Complet",
  "title_en": "Ultra Complete Project",
  "short_desc_fr": "Un projet de test exhaustif pour explorer toutes les possibilités du script d'import.",
  "short_desc_en": "An exhaustive test project to explore all import script possibilities.",
  "desc_fr": "Ce projet ultra complet démontre l'intégration de toutes les fonctionnalités prévues pour le portfolio automatisé. Il inclut des images, des sections variées, des liens, des listes, du code, des tableaux, et des captions multilingues. Il permet de valider la robustesse du script sur de grands volumes de données et de textes.",
  "desc_en": "This ultra complete project demonstrates the integration of all features planned for the automated portfolio. It includes images, various sections, links, lists, code, tables, and multilingual captions. It validates the script's robustness on large volumes of data and text.",
  "sections": [
    {
      "type": "text",
      "value": [
        "project_ultracomplet_desc",
        "project_ultracomplet_long_text"
      ]
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
      "caption_i18n": "project_ultracomplet_img_caption1"
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
      "caption_i18n": "project_ultracomplet_img_caption2"
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
      "caption_i18n": "project_ultracomplet_img_caption3"
    },
    {
      "type": "image",
      "src": "https://raw.githubusercontent.com/bosco-drg/Reverse-Engineering/main/docs/img/generator_aaronia.png",
      "caption_i18n": "project_ultracomplet_img_caption4"
    },
    {
      "type": "hr"
    },
    {
      "type": "text",
      "value": [
        "project_ultracomplet_features_intro",
        "project_ultracomplet_features_list"
      ]
    },
    {
      "type": "list",
      "items": [
        "project_ultracomplet_list_item1",
        "project_ultracomplet_list_item2",
        "project_ultracomplet_list_item3"
      ]
    },
    {
      "type": "code",
      "language": "python",
      "value": [
        "project_ultracomplet_code"
      ]
    },
    {
      "type": "table",
      "headers": [
        "project_ultracomplet_table_header1",
        "project_ultracomplet_table_header2"
      ],
      "rows": [
        [
          "project_ultracomplet_table_row1col1",
          "project_ultracomplet_table_row1col2"
        ],
        [
          "project_ultracomplet_table_row2col1",
          "project_ultracomplet_table_row2col2"
        ],
        [
          "project_ultracomplet_table_row3col1",
          "project_ultracomplet_table_row3col2"
        ],
        [
          "project_ultracomplet_table_row4col1",
          "project_ultracomplet_table_row4col2"
        ]
      ]
    },
    {
      "type": "link",
      "href": "https://github.com/bosco-drg/ultra-complet",
      "caption_i18n": "project_ultracomplet_link_caption",
      "target": "_blank"
    },
    {
      "type": "hr"
    },
    {
      "type": "text",
      "value": [
        "project_ultracomplet_long_text2"
      ]
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
