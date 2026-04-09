<div align="center">
  
# LinkedIn Computer Vision Automation
  
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GHCR](https://img.shields.io/badge/GHCR-Ready-2ea44f?logo=github)](https://github.com/maximeKets/linkedin-automation-bot/packages)
[![DockerHub](https://img.shields.io/badge/DockerHub-Ready-2496ed?logo=docker)](https://hub.docker.com/r/maximeks/linkedin-automation-bot)

**Un bot d'automatisation d'invitations LinkedIn reposant sur la reconnaissance visuelle (Computer Vision) et l'interaction orientée interface utilisateur (GUI Automation).**

</div>

## À propos du projet

Ce script automatise l'envoi d'invitations LinkedIn ciblées (notamment pour les profils Tech et Talent Acquisitions). Au lieu de se baser sur le code HTML du navigateur — qui change souvent et bloque les bots classiques — ce projet s'appuie sur la vision par ordinateur pour reproduire un véritable comportement humain (pauses aléatoires, mouvements réels de la souris, copier-coller dynamique).

## Fonctionnalités clés

-  **Localisation Visuelle** : Détection asynchrone des boutons via `opencv-python` et une tolérance (confidence) ajustable.
-  **Comportement Humain Simulé** : Mouvements naturels du curseur, scrolls et temps d'attente aléatoires.
-  **Approche Variée** : Copier-coller intelligent d'un pool de messages personnalisés (`pyperclip`).
-  **Environnement Moderne** : Construit et géré via le nouvel outil de packaging ultra-rapide `uv`.
- ️ **Failsafe (Arrêt d'Urgence)** : Interruption instantanée lors du déplacement de la souris en haut à gauche de l'écran.

## Installation & Configuration

### Prérequis
* Python 3.12+
* [uv](https://docs.astral.sh/uv/) installé sur votre machine.

### Déploiement

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/maximeKets/linkedin-automation-bot.git
   cd linkedin-automation-bot
   ```

2. Installez les dépendances via l'outil `uv` :
   ```bash
   uv sync
   ```

### Setups additionnels (Captures UI)

Le bot observe votre écran. Il dépend de captures PNG. Si le script ne repère pas de bouton, vous devrez recréer ces petites captures (depuis votre propre moniteur), recadrez-les précisément et mettez-les dans le folder "./image" :
* `connect_btn.png` : Bouton *Se connecter*.
* `add_note_btn.png` : Bouton *Ajouter une note*.
* `send_btn.png` : Bouton d'envoi modal.
* `next_page.png` : Bouton de pagination.

> **💡 Conseil de configuration**
> Gardez le niveau de zoom de votre navigateur à 100% lors de la création de la capture. Essayez de ne pas prendre de pixels de bordure extérieurs.

## Utilisation

1. Naviguez sur votre page de recherche LinkedIn.
2. Lancez le script en console :
   ```bash
   uv run main.py
   ```
3. Basculez sur votre navigateur en moins de **5 secondes**. Ne touchez plus à votre clavier ni votre souris. Le script va scanner l'écran, cliquer sur les boutons de connexion et coller la note automatiquement.

## Personnalisation

- Configurez le pool de messages directement dans la variable globale `MESSAGES` du fichier `main.py`.
- Ajustez le volume d'envois journalier en modifiant le paramètre dans l'exécution finale : `run_automation(nb_invits=100)`.

## 🐳 Déploiement via Docker

Ce projet est distribué sous forme d'image Docker multi-architecture (AMD64 / ARM64).

```bash
# 1. Récupérer la dernière image depuis GitHub Container Registry
docker pull ghcr.io/maximeKets/linkedin-automation-bot:latest

# 2. Lancer le conteneur (ajuste le port si nécessaire)
docker run -p 8000:8000 ghcr.io/maximeKets/linkedin-automation-bot:latest
```

---

<div align="center">
<i>Développé avec ❤️ pour optimiser la recherche d'opportunités entrantes.</i></br>
<i>Note: Ce projet est un Proof of Concept d'automatisation UI. Utilisez-le conformément aux conditions générales de LinkedIn.</i>
</div>
