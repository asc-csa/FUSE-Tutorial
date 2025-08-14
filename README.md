<p align="center">
    <a href="https://www.asc-csa.gc.ca/eng/satellites/fuse.asp">
        <img alt="Image du FUSE | Image of FUSE" src="https://science.nasa.gov/wp-content/uploads/2023/06/192794main-fuse-20071018-hi.jpg?w=1536&format=webp" height="300">
    </a>
    <br> Crédit d'image | Image credit: <a href="https://science.nasa.gov/wp-content/uploads/2023/06/192794main-fuse-20071018-hi.jpg?w=1536&format=webp">NASA</a>
</p>

<p align="center">
    <a href="#stars">
        <img alt="Étoiles sur GitHub | GitHub Repo stars" src="https://img.shields.io/github/stars/asc-csa/FUSE-Tutorial">
    </a>
    <a href="#watchers">
        <img alt="Spectateurs sur Github | GitHub watchers" src="https://img.shields.io/github/watchers/asc-csa/FUSE-Tutorial">
    </a>
    <a href="https://github.com/asc-csa/FUSE-Tutorial/commits/main">
        <img alt="Dernier commit sur GitHub | GitHub last commit" src="https://img.shields.io/github/last-commit/asc-csa/FUSE-Tutorial">
    </a>
    <a href="https://github.com/asc-csa/FUSE-Tutorial/graphs/contributors">
        <img alt="Contributeurs sur GitHub | GitHub contributors" src="https://img.shields.io/github/contributors/asc-csa/FUSE-Tutorial">
    </a>
    <a href="https://twitter.com/intent/follow?screen_name=csa_asc">
        <img alt="Suivre sur Twitter | Twitter Follow" src="https://img.shields.io/twitter/follow/csa_asc?style=social">
    </a>
</p>

---

<h3 align="center">
  <a href="#titre-du-projet">Français</a> |
  <a href="#project-title">English (follows)</a>
</h3>

---

<a id="titre-du-projet"></a>
# FUSE - Un tutoriel

> **Description brève :**
> Ce tutoriel a été créé pour aider les utilisateurs à exploiter les données spectroscopiques ouvertes de l'archive FUSE. Les utilisateurs pourront créer des spectrogrammes, nettoyer les anomalies des données, et les analyser en fonction des différentes caractéristiques.

Pour plus d'informations sur les données et la mission : \
ASC - [Ici](https://www.asc-csa.gc.ca/fra/satellites/fuse.asp) \
De l'équipe FUSE - [Ici](https://archive.stsci.edu/fuse/)

- [FUSE Tutorial-FR.ipynb](https://github.com/asc-csa/FUSE-Tutorial/blob/main/code/FUSE%20Tutorial-FR.ipynb) – Il s'agit du principal tutoriel au format Jupyter Notebook, qui permet d'obtenir des résultats immédiats. Il enseigne comment analyser les spectrogrammes et tracer la concentration sur une carte du ciel.  
- [Display FUSE Images Script.py](https://github.com/asc-csa/FUSE-Tutorial/blob/main/code/Display%20FUSE%20Images%20Script.py) – Il s'agit d'un script Python qui affiche des images prises par le télescope FUSE et les enregistre sous la forme d'un ensemble d'images PNG. Ces images ont peu de valeur scientifique mais peuvent être intéressantes, c'est pourquoi elles sont séparées du tutoriel principal.

## À propos

**FUSE - Un tutoriel** est un tutoriel qui aide les utilisateurs à exploiter les données spectroscopiques ouvertes de l'archive FUSE. Il couvre :

- Création et analyse de spectrogrammes à partir de données FUSE
- Nettoyage et traitement des anomalies dans les données spectrales  
- Analyse spectroscopique pour différentes caractéristiques astronomiques
- Visualisation de données sur des cartes du ciel et spectrogrammes

L'explorateur spectroscopique dans l'ultraviolet lointain (FUSE) est le fruit d'une collaboration entre l'Agence spatiale canadienne (ASC), la NASA, le Centre national d'études spatiales (CNES) et l'Université John Hopkins. FUSE a été lancé le 24 juin 1999 et a fonctionné jusqu'au 18 octobre 2007, observant près de 3000 objets astronomiques différents avec un total de 64 millions de secondes d'observation réussie.

L'objectif de cette mission était de mener diverses expériences scientifiques avec une précision jamais atteinte auparavant dans la bande de l'ultraviolet (UV), permettant d'étudier une variété de sujets astronomiques impossibles à observer depuis le sol.

Pour en savoir plus sur la mission [ici](https://archive.stsci.edu/fuse/overview.html).

*Ce tutoriel est fourni à des fins pédagogiques et expérimentales.*

## Prérequis

- Python 3.9.18 ou plus récent
- Jupyter Notebook ou Jupyter Lab
- Bibliothèques Python : astropy, numpy, matplotlib, healpy
- Connexion Internet (pour l'accès aux archives FUSE)
- Espace de stockage pour les fichiers de données spectroscopiques

## Démarrage rapide

1. 📦 **Cloner le dépôt**
   ```bash
   git clone https://github.com/asc-csa/FUSE-Tutorial.git
   cd FUSE-Tutorial
   ```
2. 🐍 **Créer un environnement**
   ```bash
   # Avec virtualenv
   python -m venv env
   source env/bin/activate

   # Ou avec conda
   conda create -n fuse_env python=3.9.18
   conda activate fuse_env
   ```
3. 📥 **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
4. 🚀 **Lancer le tutoriel**
   ```bash
   jupyter notebook "FUSE Tutorial-FR.ipynb"
   ```

> **Remarque :** Deux fichiers sont disponibles - le tutoriel principal pour l'analyse spectroscopique et un script séparé pour l'affichage d'images.

## Astuces & Conseils

- **Données UV :** FUSE était le télescope le plus sensible jamais conçu pour l'ultraviolet lointain
- **Archives :** Les données FUSE sont archivées et accessibles via le Space Telescope Science Institute
- **Spectroscopie :** Utilisez les outils astropy pour manipuler efficacement les données FITS
- **Cartes du ciel :** Healpy est requis pour la visualisation des données sur des cartes sphériques

#### Remerciements
Basé sur des observations faites avec le NASA-CNES-CSA Explorateur Spectroscopique de l'Ultraviolet Lointain. FUSE est opéré pour le NASA par l'Université Johns Hopkins sous le contrat NASA NAS5-32985.

## Licence

Ce projet est sous une licence MIT modifiée – voir le fichier [LICENSE](https://github.com/asc-csa/FUSE-Tutorial/blob/main/LICENSE.txt) pour plus de détails.

---

<h3 align="center">
  <a href="#project-title">English </a> |
  <a href="#titre-du-projet">Français (précède)</a>
</h3>

---

<a id="project-title"></a>
# FUSE - A Tutorial

> **Brief description:**  
> This tutorial has been created to help users make use of the open spectroscopy data from the FUSE archive. Users will be able to create spectrograms, clean data from anomalies, and analyze for different characteristics.

For more information about the data and the mission: \
CSA -  [Here](https://www.asc-csa.gc.ca/eng/satellites/fuse.asp) \
From the FUSE Team - [Here](https://archive.stsci.edu/fuse/)

- [FUSE Tutorial-EN.ipynb](https://github.com/asc-csa/FUSE-Tutorial/blob/main/code/FUSE%20Tutorial-EN.ipynb) – This is the main tutorial in a Jupyter Notebook format which allows for immediate outputs. It teaches how to analyze spectrograms and plot the concentration on a skymap.  
- [Display FUSE Images Script.py](https://github.com/asc-csa/FUSE-Tutorial/blob/main/code/Display%20FUSE%20Images%20Script.py) – This is a Python script that displays images taken by the FUSE telescope and saves them as a set of PNG images. These have little scientific value but may be of interest which is why it is kept separate from the main tutorial.

## About

**FUSE - A Tutorial** is a tutorial that helps users make use of the open spectroscopy data from the FUSE archive. It covers:

- Creating and analyzing spectrograms from FUSE data
- Cleaning and processing anomalies in spectral data
- Spectroscopic analysis for different astronomical characteristics
- Visualizing data on sky maps and spectrograms

The Far Ultraviolet Spectroscopic Explorer (FUSE) was a collaboration between the Canadian Space Agency (CSA), NASA, the Centre national d'etudes spatiales (CNES), and John Hopkins University. It launched on June 24, 1999 and was operational until October 18th, 2007, observing nearly 3000 different astronomical objects with a total of 64 million seconds of successful observing time.

The aim of this mission was to conduct various scientific experiments with precision never seen before in the ultraviolet (UV) band, enabling the study of a variety of astronomical subjects impossible to observe from the ground.

You can read more about the mission [here](https://archive.stsci.edu/fuse/overview.html).

*This tutorial is provided for educational and experimental purposes.*

## Prerequisites

- Python 3.9.18 or newer
- Jupyter Notebook or Jupyter Lab
- Python libraries: astropy, numpy, matplotlib, healpy
- Internet connection (for FUSE archive access)
- Storage space for spectroscopic data files

## Quick Start

1. 📦 **Clone the repo**
   ```bash
   git clone https://github.com/asc-csa/FUSE-Tutorial.git
   cd FUSE-Tutorial
   ```
2. 🐍 **Create environment**
   ```bash
   # Using virtualenv
   python -m venv env
   source env/bin/activate

   # Or using conda
   conda create -n fuse_env python=3.9.18
   conda activate fuse_env
   ```
3. 📥 **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. 🚀 **Run the tutorial**
   ```bash
   jupyter notebook "FUSE Tutorial-EN.ipynb"
   ```

> **Note:** Two files are available - the main tutorial for spectroscopic analysis and a separate script for image display.

## Tips & Tricks

- **UV Data:** FUSE was the most sensitive telescope ever designed for far-ultraviolet observations
- **Archives:** FUSE data is archived and accessible via the Space Telescope Science Institute
- **Spectroscopy:** Use astropy tools to efficiently manipulate FITS data
- **Sky Maps:** Healpy is required for visualizing data on spherical maps

#### Acknowledgements
Based on observations made with the NASA-CNES-CSA Far Ultraviolet Spectroscopic Explorer. FUSE is operated for NASA by the Johns Hopkins University under NASA contract NAS5-32985.

## License

This project is licensed under a modified MIT license - see the [LICENSE](https://github.com/asc-csa/FUSE-Tutorial/blob/main/LICENSE.txt) file for details.
