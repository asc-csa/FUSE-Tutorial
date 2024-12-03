# FUSE-Tutorial

<p align="center">
    <a href="https://www.asc-csa.gc.ca/eng/satellites/fuse.asp">
        <img alt="Image du FUSE | Image of FUSE" src="https://science.nasa.gov/wp-content/uploads/2023/06/192794main-fuse-20071018-hi.jpg?w=1536&format=webp" height="500">
        </a>
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

Image Credit: [NASA](https://science.nasa.gov/wp-content/uploads/2023/06/192794main-fuse-20071018-hi.jpg?w=1536&format=webp)

(English below)

Ce tutoriel a été créé pour aider les utilisateurs à exploiter les données spectroscopiques ouvertes de l'archive FUSE. Les utilisateurs pourront créer des spectrogrammes, nettoyer les anomalies des données, et les analyser en fonction des différentes caractéristiques. Pour plus d'informations sur les données et la mission : \
ASC - https://www.asc-csa.gc.ca/fra/satellites/fuse.asp \
De l'équipe FUSE - https://archive.stsci.edu/fuse/  

- 1_FUSE Tutorial.ipynb - Il s'agit du principal tutoriel au format Jupyter Notebook, qui permet d'obtenir des résultats immédiats. Il enseigne comment analyser les spectrogrammes et tracer la concentration sur une carte du ciel.
- 2_Display FUSE Images Script.py - Il s'agit d'un script Python qui affiche des images prises par le télescope FUSE et les enregistre sous la forme d'un ensemble d'images PNG. Ces images ont peu de valeur scientifique mais peuvent être intéressantes, c'est pourquoi elles sont séparées du tutoriel principal.

## Contexte
L'explorateur spectroscopique dans l'ultraviolet lointain (FUSE) est le fruit d'une collaboration entre l'Agence spatiale canadienne (ASC), la NASA, le Centre national d'études spatiales (CNES) et l'Université John Hopkins. L'Université du Colorado à Boulder et l'Université de Californie à Berkeley ont également collaboré au projet. FUSE a été lancé le 24 juin 1999 et a fonctionné jusqu'au 18 octobre 2007. FUSE a été utilisé pour observer près de 3000 objets astronomiques différents, avec un total de 64 millions de secondes d'observation réussie.  

Pour en savoir plus sur la mission générale, consultez le site suivant: https://archive.stsci.edu/fuse/overview.html  

L'objectif de cette mission était de mener diverses expériences scientifiques avec une précision jamais atteinte auparavant dans la bande de l'ultraviolet (UV). L'atmosphère terrestre (en particulier la thermosphère) absorbe les rayons UV, ce qui rend les observations au sol quasiment impossibles. Cela incite les scientifiques à développer des télescopes qui peuvent être envoyés dans l'espace et absorber les rayons UV pour étudier une variété de sujets couvrant une gamme de caractéristiques observées dans les objets célestes jusqu'aux atlas des objets célestes.  

Pour en savoir plus sur les principaux objectifs scientifiques et leurs résumés, consultez le site suivant : https://archive.stsci.edu/fuse/scisumm/  

## Démarrage rapide

1.	Configurez un environnement virtuel ou un environnement conda avec la version suivante de python (si vous utilisez conda, remplacez la commande pip install ci-dessous par conda) 
```
python = 3.9.18
```
2. Installer les dépendances depuis le fichier requirments.txt
```
pip install -r requirements.txt
```

#### Remerciements
Basé sur des observations faites avec le NASA-CNES-CSA Explorateur Spectroscopique de l'Ultraviolet Lointain. FUSE est opéré pour le NASA par l'Université Johns Hopkins sous le contrat NASA NAS5-32985.


---
(Le français précède) 

This tutorial has been created to help users make use of the open spectroscopy data from the FUSE archive. Users will be able to create spectrograms, clean data from anomalies, and analyze for different characteristics. For more information about the data and the mission: \
CSA -  https://www.asc-csa.gc.ca/eng/satellites/fuse.asp \
From the FUSE Team - https://archive.stsci.edu/fuse/

- 1_FUSE Tutorial.ipynb - This is the main tutorial in a Jupyter Notebook format which allows for immediate outputs. It teaches how to analyze spectrograms and plot the concentration on a skymap.
- 2_Display FUSE Images Script.py - This is a Python script that displays images taken by the FUSE telescope and saves them as a set of PNG images. These have little scientific value but may be of interest which is why it is kept separate from the main tutorial.

## About 
The Far Ultraviolet Spectroscopic Explorer (FUSE) was a collaboration between the Canadian Space Agency (CSA), NASA, the Centre national d'etudes spatiales (CNES), and John Hopkins University. The University of Colorado in Boulder and the University of California in Berkeley were also collaborators on the project. It launched on June 24, 1999 and was operational until October 18th, 2007. FUSE has been used to observe nearly 3000 different astronomical objects with a total of 64 million seconds of successful observing time.  

You can read more about the general mission here: https://archive.stsci.edu/fuse/overview.html  

The aim of this mission was to conduct various scientific experiments with precision never seen before in the ultraviolet (UV) band. The Earth's atmosphere (specifically the thermosphere) absorbs UV rays making ground observations near-impossible. This incentivizes scientists to develop telescopes that can be sent to space and absorb UV rays to study a variety of subjects covering a range of characteristics observed in celestial objects to atlases of celestial objects.  

You can read more about the high-profile science goals and summaries here: https://archive.stsci.edu/fuse/scisumm/  

## Quick Start

1.	Setup a virtual environment or conda environment with the following version of python (if using conda replace the below pip install with conda) 
```
python = 3.9.18
```
2.  Install requirements from the requirments.txt file 
```
pip install -r requirements.txt
```

#### Acknowledgements
Based on observations made with the NASA-CNES-CSA Far Ultraviolet Spectroscopic Explorer. FUSE is operated for NASA by the Johns Hopkins University under NASA contract NAS5-32985.

