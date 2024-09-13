---
title: "Comandi FokaBot"
reference_version: 383b905114b125d7bfd87a7dacdc8b56
---
Questi sono i comandi supportati da FokaBot, il nostro chat bot.

### Comandi generici
- `!roll` - Ritorna un numero casuale da 0 a 100
- `!roll num` - Ritorna un numero casuale da 0 a num
- `!help` - Visualizza il messaggio d'aiuto
- `!pp [mode]` - Mostra i tuoi pp attuali. Se `mode` non è presente, FokaBot ti dirà l'ammontare dei PP per la tua modalità di gioco corrente. Se mode è presente (può essere `std/taiko/ctb/mania`), FokaBot ti dirà l'ammontare dei PP per quella modalità di gioco. **Questo comando funziona solo nei messaggi privati**
- `!update` - Aggiorna il beatmapset che hai inviato col comando `/np` nel nostro mirror di beatmap. Usalo se hai appena scaricato una beatmap dall'osu!direct e viene mostrata come non aggiornata o se una mappa non può essere scaricata dall'osu!direct poiché è troppo recente.

- `!ppboard` - Cambiato Ingame Leaderboard in pp
- `!scoreboard` - Cambiato Ingame Leaderboard in score

- `!nerinyan` - nerinyan beatmapset messaggio di download (+osu!direct)
- `!dl` - redstar beatmapset messaggio di download (+osu!direct)
- `!dl2` - uguale a `!nerinyan`
- `!catboy` - catboy beatmapset messaggio di download (+osu!direct)
- `!chimu` - chimu beatmapset messaggio di download (+osu!direct)
- `!bloodcat` - uguale a `!chimu`, bloodcat(chimu) beatmapset messaggio di download (+osu!direct)
- `!bc` - uguale a `!bloodcat`
- `!sayobot` - sayobot beatmapset messaggio di download (+osu!direct)
- `!beatconnect` - beatconnect beatmapset messaggio di download (+osu!direct)
- `!mirror` - mirror message, mirror beatmapset messaggio di download (+osu!direct)
- `!rankrq` - Questo è il comando di richiesta di rango. Prima di usarlo, è necessario usare il comando `/np` o `/!last` o `!with`. [Per maggiori dettagli, consultare il sito](/beatmaps/rank_request)
- `!songinfo` - Mostra informazioni dettagliate sul brano. è necessario utilizzare prima il comando `/np` o `/!last` o `!with`.
- `!songinfo <mods>` - `!songinfo` + Mostra PP per la beatmap richiesta in precedenza con le mod richieste. Le mod supportate sono `NF, EZ, HD, HR, DT, HT, NC, FL, SO`. Non usare spazi per più mod (es.: `!songinfo HDNC`).
- `!md5tobid <Beatmap_md5> ` - Restituisce il `beatmapID` del `md5` in ingresso.
- `!kickself` - prendersi a calci
- `!bpp` - Tra tutti i record, il record con la pp più alta viene restituito tramite il comando `!last'.
- `!replay <vn/rx/ap> <ReplayID>` - Restituisce il record di riproduzione del brano utilizzando il replayID.
- `!history <vn/rx/ap> <BeatmapID>` - Restituisce il record di tutte le riproduzioni del brano utilizzando il beatmapID.
- `!mapsuggest <jump/stream/+set(1000,999)>` - raccomandare mappe di stream o di jump. [di 1000](https://redstar.moe/u/1000)
- `!status` - Controllare lo stato del server. [Bancho](https://c.redstar.moe/api/v1/serverStatus), [lets](https://old.redstar.moe/letsapi/v1/status), [api](https://redstar.moe/api/v1/ping), [mediaserver](https://b.redstar.moe/status)
- `!b <BeatmapID>` - Restituisce il link di osu!direct (b/)
- `!d <BeatmapSetID>` - Restituisce il link di osu!direct (d/)
- `!lb <std(s)/taiko(t)/ctb(c)/mania(m)> <vn/rx/ap>` - Restituisce la classifica

### Comandi `!mp` (Torneo)
- `!mp <subcommand>` - principale
- `subcommands` = listref|addref|rmref|make|close|join|lock|unlock|size|move|host|clearhost
|start|invite|map|set|abort|kick|password|randompassword|mods|team|settings|scorev|help

### Comandi Faq
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

### Comand in stile Tillerino
Fokabot dispone di comandi simili a Tillerino. Questi comandi funzionano solo se li mandi a FokaBot tramite messaggio privato. Tieni a mente che il sistema dei PP è stato implementato solo per osu!standard e osu!mania. Il bot al momento non supporta i consigli per le beatmap, quella funzionalità sarà disponibile in futuro, se tutto va bene.

- `/np` - Mostra i PP per la canzone attualmente in ascolto  (solo se è una canzone per osu!standard)

- `!last` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato (Rileva automaticamente vn, rx, ap in base alla persona che ha eseguito il comando)
- `!last vn` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato (Vanilla)
- `!last rx` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato (Relax)
- `!last ap` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato (AutoPilot)

- `!last <beatmapID>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da beatmapID (Rileva automaticamente vn, rx, ap in base alla persona che ha eseguito il comando)
- `!last vn <beatmapID>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da beatmapID (Vanilla)
- `!last rx <beatmapID>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da beatmapID (Relax)
- `!last ap <beatmapID>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da beatmapID (Autopilot)

- `!last <username_safe>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da username (Rileva automaticamente vn, rx, ap in base alla persona che ha eseguito il comando)
- `!last vn <username_safe>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da username (Vanilla)
- `!last rx <username_safe>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da username (Relax)
- `!last ap <username_safe>` - Mostra delle informazioni (e i PP ottenuti, se fosse un punteggio di osu! standard) riguardanti l'ultimo punteggio inviato da username (Autopilot)

- `!with <mods>` - Mostra i PP per la beatmap precedentemente richiesta con i modificatori richiesti. I modificatori supportati sono `NF, EZ, HD, HR, DT, HT, NC, FL, SO.`. Non usare gli spazi per più modificatori (ad esempio: `!with HDHR`)

- `!r` - Raccomanda una Beatmap Casuale (Calcola il PP medio applicando pesi ai primi 10 record di PP e dividendo la somma ponderata per 10. In assenza di modalità, usa il PP massimo raggiungibile come base e raccomanda mappe nello stato classificato o approvato all'interno di un intervallo ±50PP dal PP medio.)

- `!token.tillerino` - Controllare le informazioni di token.tillerino `[Beatmap_ID, mod (numero), acc, by]`
- `!del token.tillerino` - Cancellare il valore di token.tillerino (reset) `[0, 0, -1.0, by !del token.tillerino]`
- `!input token.tillerino <Beatmap_ID> <mod (number)>(options) <acc>(options) <by>(options)` - Inserire il valore di token.tillerino

### Comandi del nominatore di beatmap
- `!map <ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>` - Modifica lo stato di rango della beatmap.

### Comandi di amministrazione
- `!system restart` - Riavvia il server. Tutti verranno disconnessi e riconnessi automaticamente
- `!system status` - Mostra lo stato del server
- `!system reload` - Ricarica le impostazioni di bancho (quelle che sono modificabili dal RAP)
- `!system maintenance on/off` - Attiva/disattiva la modalità di manutenzione di bancho
- `!moderated on/off` - Attiva/disattiva la modalità moderata per il canale corrente
- `!silence <username> <count> <unit (s/m/h/d)> <reason>` - Silenzia un utente
- `!removesilence <target>` - Rimuove il silence dal target
- `!kick <username>` - Caccia un utente dal server
- `!ban <username>` - Bandisce e caccia qualcuno
- `!unban <username>` - Toglie il bando da qualcuno
- `!restrict <username>` - Mette in modalità ristretta qualcuno
- `!unrestrict <username>` - Toglie la modalità ristretta a qualcuno
- `!fokabot reconnect` - Riconnette Fokabot se non è più nella lista degli utenti online
- `!alert <message>` - Manda una notifica a ciascun utente connesso a bancho
- `!alertuser  <username> <message>` - Manda una notifica ad un utente specifico

- `!vbri <True(1)/False(0)/check>` - Questo comando determina se visualizzare i record delle persone bandite nella Ingame Leaderboard.
<!-- Ingame의 leaderboard에서 banned당한 사람들의 기록을 표시여부를 결정하는 명령어 입니다. -->
<!-- This command determines whether to display the records of banned people on the Ingame leaderboard. -->
- `!view_banneduser_record_ingame` - uguale a `!vbri`
- `!view_banneduser` - uguale a `!vbri`