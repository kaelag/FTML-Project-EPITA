"""Réduit Animals-10 à N images par classe via échantillonnage stratifié.

Source : ~/Downloads/archive/raw-img/
Sortie : project/data/animals10_1k/<classe>/
"""

from __future__ import annotations

import random
import shutil
from pathlib import Path

SRC = Path.home() / "Downloads" / "archive" / "raw-img"
DST = Path(__file__).resolve().parents[1] / "data" / "animals10_1k"
N_PER_CLASS = 1000
SEED = 42

IT_TO_FR = {
    "cane": "chien",
    "cavallo": "cheval",
    "elefante": "elephant",
    "farfalla": "papillon",
    "gallina": "poule",
    "gatto": "chat",
    "mucca": "vache",
    "pecora": "mouton",
    "ragno": "araignee",
    "scoiattolo": "ecureuil",
}


def main() -> None:
    rng = random.Random(SEED)
    if not SRC.exists():
        raise FileNotFoundError(f"Source absente : {SRC}")

    DST.mkdir(parents=True, exist_ok=True)

    summary: list[tuple[str, int, int]] = []
    for it_name, fr_name in IT_TO_FR.items():
        src_dir = SRC / it_name
        dst_dir = DST / fr_name
        dst_dir.mkdir(parents=True, exist_ok=True)

        for old in dst_dir.iterdir():
            if old.is_file():
                old.unlink()

        images = sorted(p for p in src_dir.iterdir() if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"})
        n_available = len(images)
        n_sample = min(N_PER_CLASS, n_available)
        sample = rng.sample(images, n_sample)

        for i, img in enumerate(sample):
            new_name = f"{fr_name}_{i:04d}{img.suffix.lower()}"
            shutil.copy2(img, dst_dir / new_name)

        summary.append((fr_name, n_sample, n_available))
        print(f"{fr_name:10s} : {n_sample:4d} copiees (sur {n_available} disponibles)")

    total = sum(s[1] for s in summary)
    print(f"\nTotal : {total} images dans {DST}")


if __name__ == "__main__":
    main()
