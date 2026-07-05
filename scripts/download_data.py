"""Télécharge le dataset Animals-10 depuis Kaggle puis prépare le sous-ensemble
équilibré utilisé par les exercices 6 et 7.

Usage :
    python scripts/download_data.py

Étapes :
    1. télécharge Animals-10 via kagglehub (~26 000 images),
    2. copie les dossiers de classes dans ~/Downloads/archive/raw-img/,
    3. lance scripts/reduce_animals10.py pour produire data/animals10_1k/.

Alternative manuelle : télécharger l'archive depuis
https://www.kaggle.com/datasets/alessiocorrado99/animals10
la décompresser dans ~/Downloads/archive/ (dossier raw-img/), puis lancer
    python scripts/reduce_animals10.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEST_RAW = Path.home() / "Downloads" / "archive" / "raw-img"


def main() -> None:
    try:
        import kagglehub
    except ImportError:
        print("kagglehub absent. Installez-le (pip install kagglehub) ou "
              "téléchargez manuellement le dataset (voir docstring).")
        sys.exit(1)

    print("Téléchargement d'Animals-10 depuis Kaggle...")
    path = Path(kagglehub.dataset_download("alessiocorrado99/animals10"))
    src = path / "raw-img"
    if not src.exists():
        # certaines versions exposent directement les dossiers de classes
        src = path

    DEST_RAW.parent.mkdir(parents=True, exist_ok=True)
    if DEST_RAW.exists():
        print(f"{DEST_RAW} existe déjà, copie ignorée.")
    else:
        print(f"Copie de {src} vers {DEST_RAW}...")
        shutil.copytree(src, DEST_RAW)

    print("Réduction à 1000 images par classe...")
    subprocess.run([sys.executable, str(HERE / "reduce_animals10.py")], check=True)
    print("Terminé. Données prêtes dans project/data/animals10_1k/.")


if __name__ == "__main__":
    main()
