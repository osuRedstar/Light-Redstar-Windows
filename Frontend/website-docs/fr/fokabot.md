---
title: "Les Commandes de FokaBot"
reference_version: 383b905114b125d7bfd87a7dacdc8b56
---
Ce sont les commandes prises en charge par FokaBot, notre bot chat.

### Commandes générales
- `!roll` - Renvoie un nombre aléatoire de 0 à 100
- `!roll num` - Renvoie un nombre aléatoire de 0 au nombre que vous avez mis
- `!help` - Affiche le message d'aide
- `!pp [mode]` - Afficher vos pp actuels. Si `mode` n'est pas présent, FokaBot vous indiquera le montant de PP pour votre mode de jeu actuel. Si le mode est présent (cela peut-être `std/taiko/ctb/mania`), FokaBot vous indiquera le montant de PP pour ce mode de jeu. **Cette commande fonctionne seulements dans les MP**
- `!update` - Met à jour beatmapset que vous avez `/np` dans notre téléchargement de map alternative. Utilisez ceci si vous venez de télécharger une map à partir d'osu!direct et il apparaît comme obsolète ou si une map ne peut pas être téléchargé depuis osu!direct car il est trop nouveau.

- `!ppboard` - Modification du classement en jeu par pp
- `!scoreboard` - Modification du classement en jeu par score

- `!nerinyan` - nerinyan beatmapset download message (+osu!direct)
- `!dl` - redstar beatmapset download message (+osu!direct)
- `!dl2` - Pareil que `!nerinyan`
- `!catboy` - catboy beatmapset download message (+osu!direct)
- `!chimu` - chimu beatmapset download message (+osu!direct)
- `!bloodcat` - Pareil que `!chimu`, bloodcat(chimu) beatmapset download message (+osu!direct)
- `!bc` - Pareil que `!bloodcat`
- `!sayobot` - sayobot beatmapset download message (+osu!direct)
- `!beatconnect` - beatconnect beatmapset download message (+osu!direct)
- `!mirror` - mirror message, mirror beatmapset download message (+osu!direct)
- `!rankrq` - Il s'agit de la commande Rank Request. Avant de l'utiliser, vous devez d'abord utiliser la commande `/np` ou `/!last` ou `!with`. [Pour plus de détails, voir ici](/beatmaps/rank_request)
- `!songinfo` - Affiche des informations détaillées sur la chanson. Vous devez d'abord utiliser la commande `/np` ou `/!last` ou `!with`.
- `!songinfo <mods>` - `!songinfo` + Affiche le PP de la précédente beatmap demandée avec les mods demandés. Les mods supportés sont `NF, EZ, HD, HR, DT, HT, NC, FL, SO`. N'utilisez pas d'espace pour les mods multiples (ex : `!songinfo HDNC`)
- `!md5tobid <Beatmap_md5> ` - Retourne le `beatmapID` de l'entrée `md5`.
- `!kickself` - se donner un coup de pied
- `!bpp` - Parmi tous vos enregistrements, l'enregistrement ayant le pp le plus élevé est renvoyé par la commande `!last `.
- `!replay <vn/rx/ap> <ReplayID>` - Renvoie l'enregistrement de la chanson à l'aide de l'identifiant replayID.
- `!history <vn/rx/ap> <BeatmapID>` - Renvoie l'enregistrement de toutes les lectures de la chanson à l'aide de l'identifiant beatmapID.
- `!mapsuggest <jump/stream/+set(1000,999)>` - recommend stream or jump maps. [by 1000](https://redstar.moe/u/1000)
- `!status` - Vérifier l'état du serveur. [Bancho](https://c.redstar.moe/api/v1/serverStatus), [lets](https://old.redstar.moe/letsapi/v1/status), [api](https://redstar.moe/api/v1/ping), [mediaserver](https://b.redstar.moe/status)
- `!b <BeatmapID>` - Retourne le lien osu!direct (b/)
- `!d <BeatmapSetID>` - Retourne le lien osu!direct (d/)
- `!lb <std(s)/taiko(t)/ctb(c)/mania(m)> <vn/rx/ap>` - Retourne le classement

### Commandes `!mp` (Tournoi)
- `!mp <subcommand>` - principal
- `subcommands` = listref|addref|rmref|make|close|join|lock|unlock|size|move|host|clearhost
|start|invite|map|set|abort|kick|password|randompassword|mods|team|settings|scorev|help

### Commandes Faq
- `!faq rules`
- `!faq swearing`
- `!faq spam`
- `!faq offend`
- `!faq english`
- `!faq github`
- `!faq discord`
- `!faq blog`
- `!faq changelog`
- `!faq status`

### Commandes de type Tillerino
Fokabot a des commandes semblables à celles de Tillerino. Ces commandes ne fonctionnent que si vous les envoyez à Fokabot via un MP. Rappelez-vous que le système de PP a été implémenté que sur osu! Standard and osu! Mania. Le robot ne prend pas en charge les recommandations de maps en ce moment, cette fonctionnalité viendra plus tard, Espérons-le.

- `/np` - Affiche les PP pour la chanson en cours  (Seulement si c'est une musique osu!standard)  

- `!last` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis (Détecte automatiquement le vn, le rx, l'ap en fonction de la personne qui a exécuté la commande)
- `!last vn` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis (Vanilla)
- `!last rx` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis (Relax)
- `!last ap` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis (AutoPilot)

- `!last <beatmapID>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par beatmapID (Détecte automatiquement le vn, le rx, l'ap en fonction de la personne qui a exécuté la commande)
- `!last vn <beatmapID>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par beatmapID (Vanilla)
- `!last rx <beatmapID>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par beatmapID (Relax)
- `!last ap <beatmapID>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par beatmapID (Autopilot)

- `!last <username_safe>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par username (Détecte automatiquement le vn, le rx, l'ap en fonction de la personne qui a exécuté la commande)
- `!last vn <username_safe>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par username (Vanilla)
- `!last rx <username_safe>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par username (Relax)
- `!last ap <username_safe>` - Affiche les (et le nombre de PP gagné(s),Si c'était un score dans le mode standard) informations sur le dernier score soumis par username (Autopilot)

- `!with <mods>` - Affiche les PP pour la beatmap précédente demandée avec les mods demandés. Les modes supporter sont `NF, EZ, HD, HR, DT, HT, NC, FL, SO.`. N'utilisez pas d'espaces pour des mods multiples (ex : `!with HDHR`)

- `!r` - Recommander un Beatmap aléatoire (Calcule le PP moyen en appliquant des poids aux 10 meilleurs enregistrements de PP et en divisant la somme pondérée par 10. En cas d'absence de mode, utilise le PP maximal réalisable comme base et recommande des cartes en état classé ou approuvé dans une plage ±50PP autour du PP moyen.)

- `!token.tillerino` - Vérifier les informations de token.tillerino `[Beatmap_ID, mod (number), acc, by]`
- `!del token.tillerino` - Supprimer la valeur de token.tillerino (réinitialisation) `[0, 0, -1.0, by !del token.tillerino]`
- `!input token.tillerino <Beatmap_ID> <mod (number)>(options) <acc>(options) <by>(options)` - Insérer la valeur de token.tillerino

### Commandes du nominateur de Beatmap
- `!map <ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>` - Changer le statut du rang de la beatmap.

### Commandes d'administration
- `!system restart` - Redémarre le serveur. Tout le monde sera déconnecté et reconecté automatiquement
- `!system status` - Affiche l'état du serveur
- `!system reload` - Recharge les paramètres de Bancho (Celui qui est éditable depuis RAP)
- `!system maintenance on/off` - Active / désactive le mode de maintenance de bancho
- `!moderated on/off` - Active / désactive le mode modéré pour le canal actuel
- `!silence <pseudo> <temps> <unité (s/m/h/j)> <raison>` - Réduit au silence l'utilisateur
- `!removesilence <cible>` - Supprime le silence de la cible
- `!kick <pseudo>` - Kick l'utilisateur du serveur
- `!ban <pseudo>` - Ban l'utilisateur
- `!unban <pseudo>` - Unban l'utilisateur
- `!restrict <pseudo>` - Restricte l'accès à l'utilisateur au serveur
- `!unrestrict <pseudo>` - Donne le droit d'accès à l'utilisateur au serveur
- `!fokabot reconnect` - Reconnecte Fokabot s'il n'est plus sur la liste des utilisateurs en ligne
- `!alert <message>` - Envoye une notification à chaque utilisateur connecté à bancho
- `!alertuser  <pseudo> <message>` - Envoye une notification à une utilisation spécifique

- `!vbri <True(1)/False(0)/check>` - Cette commande détermine s'il convient d'afficher les enregistrements des personnes bannies dans le tableau de classement du jeu.
<!-- Ingame의 leaderboard에서 banned당한 사람들의 기록을 표시여부를 결정하는 명령어 입니다. -->
<!-- This command determines whether to display the records of banned people on the Ingame leaderboard. -->
- `!view_banneduser_record_ingame` - Pareil que `!vbri`
- `!view_banneduser` - Pareil que `!vbri`