#!/usr/bin/env python3
"""
Genere les 10 meilleurs endroits a visiter sur l'itineraire :
Zoo de Beauval, Puy du Fou, Saint-Nazaire, Dinan et Mont-Saint-Michel.

Exemples :
  python top_10_itineraire.py
  python top_10_itineraire.py --format json
  python top_10_itineraire.py --format csv --output top_10_itineraire.csv
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Place:
    rank: int
    name: str
    destination: str
    category: str
    visit_time: str
    best_moment: str
    why: str
    practical_tip: str
    source: str


TOP_10: list[Place] = [
    Place(
        rank=1,
        name="Abbaye du Mont-Saint-Michel",
        destination="Mont-Saint-Michel",
        category="Patrimoine majeur",
        visit_time="1 h 30 a 2 h",
        best_moment="Avant 10 h ou apres 15 h",
        why="C'est le point le plus fort de l'itineraire : un monument millenaire au sommet du Mont, inscrit au patrimoine mondial de l'UNESCO.",
        practical_tip="Reserver le billet si possible et garder de bonnes chaussures : le parcours comporte beaucoup d'escaliers.",
        source="https://montsaintmichel.gouv.fr/visite-du-mont-et-de-sa-baie/abbaye-du-mont-saint-michel",
    ),
    Place(
        rank=2,
        name="Le Signe du Triomphe",
        destination="Puy du Fou",
        category="Grand spectacle",
        visit_time="Environ 30 min, hors attente",
        best_moment="Premier horaire disponible",
        why="Un des grands spectacles incontournables du Puy du Fou, avec arene romaine, course de chars, combats et effets spectaculaires.",
        practical_tip="Bloquer cet horaire en premier dans le programme du jour, puis organiser les autres spectacles autour.",
        source="https://w3.puydufou.com/faq-mon-compte/les-spectacles-incontournables-du-puy-du-fou-",
    ),
    Place(
        rank=3,
        name="La Plaine des Elephants",
        destination="ZooParc de Beauval",
        category="Grands animaux",
        visit_time="35 a 50 min",
        best_moment="Matin ou fin d'apres-midi",
        why="Une zone phare pour observer les elephants d'Afrique depuis plusieurs points de vue, y compris a proximite de la telecabine.",
        practical_tip="Prevoir assez de temps pour regarder les deplacements et interactions, pas seulement passer devant l'enclos.",
        source="https://www.zoobeauval.com/zooparc/territoires/la-plaine-des-elephants",
    ),
    Place(
        rank=4,
        name="Les remparts et la Grande Rue",
        destination="Mont-Saint-Michel",
        category="Village historique",
        visit_time="45 min a 1 h",
        best_moment="En arrivant tot ou au retour de l'abbaye",
        why="Les remparts offrent un chemin de ronde et de tres beaux points de vue, tandis que la Grande Rue concentre l'ambiance medievale du village.",
        practical_tip="Monter par les remparts quand la Grande Rue est trop chargee.",
        source="https://www.ot-montsaintmichel.com/je-decouvre/visiter-le-mont-saint-michel/je-visite-le-mont-saint-michel/le-village-et-les-remparts/",
    ),
    Place(
        rank=5,
        name="Les Vikings",
        destination="Puy du Fou",
        category="Grand spectacle",
        visit_time="26 min, hors attente",
        best_moment="Avant ou juste apres le dejeuner",
        why="Un spectacle tres lisible et spectaculaire, avec drakkars, cascades, flammes et grand decor de village.",
        practical_tip="Arriver avec de l'avance, surtout pendant les journees de forte affluence.",
        source="https://w3.puydufou.com/faq-mon-compte/les-spectacles-incontournables-du-puy-du-fou-",
    ),
    Place(
        rank=6,
        name="Escal'Atlantic",
        destination="Saint-Nazaire",
        category="Visite immersive",
        visit_time="1 h 30 a 2 h",
        best_moment="Quand la meteo est moyenne ou en milieu de journee",
        why="Une visite immersive autour de l'histoire des paquebots transatlantiques, tres representative de Saint-Nazaire.",
        practical_tip="A placer avant le sous-marin Espadon pour rester dans le meme univers portuaire.",
        source="https://www.saint-nazaire-tourisme.com/les-visites/les-visites-decouvertes-saint-nazaire/",
    ),
    Place(
        rank=7,
        name="Remparts, port et centre historique de Dinan",
        destination="Dinan",
        category="Vieille ville",
        visit_time="2 h a 3 h",
        best_moment="Matin ou fin de journee",
        why="Dinan est l'une des plus belles pauses urbaines du trajet, avec remparts, vues sur le port et ruelles medievales.",
        practical_tip="Descendre vers le port puis remonter tranquillement, ou faire l'inverse selon votre energie.",
        source="https://www.dinan-capfrehel.com/nos-incontournables/",
    ),
    Place(
        rank=8,
        name="Le Bal des Oiseaux Fantomes",
        destination="Puy du Fou",
        category="Grand spectacle",
        visit_time="Environ 30 min, hors attente",
        best_moment="Selon meteo et programme du jour",
        why="Un des grands spectacles les plus marquants du parc, centre sur le vol des rapaces et l'effet de proximite avec le public.",
        practical_tip="Eviter de le sacrifier si vous n'avez qu'une journee au Puy du Fou.",
        source="https://w3.puydufou.com/faq-mon-compte/les-spectacles-incontournables-du-puy-du-fou-",
    ),
    Place(
        rank=9,
        name="Le Sous-Marin Espadon",
        destination="Saint-Nazaire",
        category="Patrimoine maritime",
        visit_time="45 min a 1 h",
        best_moment="Apres Escal'Atlantic",
        why="Une visite forte et concrete pour comprendre le lien de Saint-Nazaire avec la mer, les navires et la base sous-marine.",
        practical_tip="Verifier les horaires et reserver si vous voyagez pendant une periode chargee.",
        source="https://www.saint-nazaire-tourisme.com/mon-sejour/a-faire/les-activites-incontournables/",
    ),
    Place(
        rank=10,
        name="Les Hauteurs de Chine et la Serre des Gorilles",
        destination="ZooParc de Beauval",
        category="Animaux emblematiques",
        visit_time="1 h a 1 h 30",
        best_moment="Apres-midi avec pause a l'ombre ou en interieur",
        why="Ces deux zones completent bien la Plaine des Elephants avec pandas geants, pantheres des neiges, gorilles et grands primates.",
        practical_tip="Les garder comme bloc flexible si votre journee a Beauval prend du retard.",
        source="https://www.zoobeauval.com/zooparc/territoires",
    ),
]


def as_markdown(places: Iterable[Place]) -> str:
    lines = [
        "# Top 10 des endroits a visiter sur l'itineraire",
        "",
        "Itineraire couvert : ZooParc de Beauval, Puy du Fou, Saint-Nazaire, Dinan et Mont-Saint-Michel.",
        "",
    ]

    for place in places:
        lines.extend(
            [
                f"## {place.rank}. {place.name}",
                "",
                f"- Destination : {place.destination}",
                f"- Type : {place.category}",
                f"- Temps conseille : {place.visit_time}",
                f"- Meilleur moment : {place.best_moment}",
                f"- Pourquoi y aller : {place.why}",
                f"- Conseil pratique : {place.practical_tip}",
                f"- Source : {place.source}",
                "",
            ]
        )

    return "\n".join(lines)


def as_json(places: Iterable[Place]) -> str:
    return json.dumps([asdict(place) for place in places], ensure_ascii=False, indent=2)


def as_csv(places: Iterable[Place]) -> str:
    rows = [asdict(place) for place in places]
    fieldnames = list(rows[0].keys())
    from io import StringIO

    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genere le top 10 des endroits a visiter sur l'itineraire de voyage."
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "csv"),
        default="markdown",
        help="Format de sortie.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Fichier de sortie. Sans cette option, le resultat est affiche dans le terminal.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.format == "json":
        content = as_json(TOP_10)
    elif args.format == "csv":
        content = as_csv(TOP_10)
    else:
        content = as_markdown(TOP_10)

    if args.output:
        args.output.write_text(content, encoding="utf-8", newline="")
        print(f"Fichier cree : {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()
