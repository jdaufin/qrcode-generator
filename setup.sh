#!/bin/bash

set -e

# Nom du dossier d'environnement virtuel
VENV_DIR=".venv_qrcode"

# Création de l'environnement
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 Création de l'environnement virtuel..."
  python3 -m venv "$VENV_DIR"
fi

# Activation
source "$VENV_DIR/bin/activate"

# Installation des dépendances
echo "📥 Installation des dépendances Python..."
pip install --upgrade pip
pip install -r requirements.txt
