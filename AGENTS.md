# Instructions du projet « Roadtrip 5j »

## Périmètre

- Le dépôt Git est `my_first_repo`; les pages publiées sont dans `Nouveau dossier/`.
- Conserver le site comme un ensemble de pages HTML/CSS/JavaScript statiques, sans dépendance ni étape de build, sauf demande explicite.
- Le mini-jeu planifie les cinq jours du roadtrip : Beauval, Puy du Fou, Saint-Nazaire, Dinan + Mont-Saint-Michel, puis le retour à Paris.
- L’interface attendue est un jeu de choix textuels : ne pas ajouter de maquette graphique, d’illustrations ou d’effets décoratifs pour ce besoin.

## Sources et contenu du roadtrip

- Les sources sont `Nouveau dossier/beauval-grands-animaux.html`, `puy-du-fou-1-jour.html`, `saint-nazaire.html`, `dinan.html`, `mont-saint-michel.html` et le récapitulatif de `index.html`.
- Réutiliser les contenus réels avant d’en inventer : étapes, durées connues, zones, priorités et règles de décision.
- Le jour de retour Paris n’a pas de page dédiée : limiter ses choix à une balade simple ou un repas, comme l’indique `index.html`, tant que l’utilisateur ne fournit pas d’autres activités.
- Ne pas présenter les horaires, la météo ou les animations comme des informations garanties : conserver les liens officiels et indiquer qu’ils sont à vérifier le jour même.

## Mini-jeu de planification

- Afficher des activités textuelles clairement numérotées, avec titre, lieu, durée lorsque connue et niveau de priorité accessible.
- Faire avancer la sélection du jour 1 au jour 5 sans effacer les choix déjà validés; permettre de revenir corriger un jour avant le récapitulatif final.
- Garder un état unique, sérialisable et testable (jour actif, activités choisies, rythme éventuel); persister uniquement après accord explicite sur le besoin de reprise entre sessions.
- Le récapitulatif final doit montrer les choix de chaque jour, les activités non sélectionnées et les éventuelles contraintes ou conflits signalés.

## Qualité

- Préserver le français, le balisage sémantique, les libellés accessibles et une utilisation complète au clavier.
- Préférer des modifications petites et isolées; vérifier au navigateur les flux desktop et mobile, les retours en arrière et le récapitulatif avant livraison.
- Ne jamais écraser de modifications non liées ni d’assets existants.
