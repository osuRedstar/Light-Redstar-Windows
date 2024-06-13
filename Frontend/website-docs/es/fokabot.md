---
title: "Comandos de FokaBot"
reference_version: 383b905114b125d7bfd87a7dacdc8b56
---
Estos son los comandos soportados por FokaBot, nuestro bot de chat.

### Comandos generales
- `!roll` - Devuelve un número aleatorio de 0 a 100
- `!roll num` - Devuelve un número aleatorio de 0 a num
- `!help` - Muestra el mensaje de ayuda
- `!pp [modo]` - Muestra tu pp actual. Si el `modo` no está presente, FokaBot te dirá la cantidad de PP para tu modo de juego actual. Si el modo está presente (puede ser `std/taiko/ctb/mania`), FokaBot te dirá la cantidad de PP para ese modo de juego. **Este comando sólo funciona en mensajes privados**
- `!update` - Actualiza el set de mapas que has enviado con el comando `/np` en nuestro sitio espejo de mapas. Úselo si acaba de descargar un mapa de osu!direct y aparece como obsoleto o si no se puede descargar un mapa de osu!direct porque es demasiado nuevo.

- `!ppboard` - Cambiado Ingame Leaderboard por pp
- `!scoreboard` - Cambiado Ingame Leaderboard por score

- `!nerinyan` - nerinyan beatmapset mensaje de descarga (+osu!direct)
- `!dl` - redstar beatmapset mensaje de descarga (+osu!direct)
- `!dl2` - Igual que `!nerinyan`
- `!catboy` - catboy beatmapset mensaje de descarga (+osu!direct)
- `!chimu` - chimu beatmapset mensaje de descarga (+osu!direct)
- `!bloodcat` - Igual que `!chimu`, bloodcat(chimu) beatmapset mensaje de descarga (+osu!direct)
- `!bc` - Igual que `!bloodcat`
- `!sayobot` - sayobot beatmapset mensaje de descarga (+osu!direct)
- `!beatconnect` - beatconnect beatmapset mensaje de descarga (+osu!direct)
- `!mirror` - mirror mensaje, mirror beatmapset mensaje de descarga (+osu!direct)
- `!rankrq` - Este es el comando Solicitud de Rank. Antes de usarlo, debes usar primero el comando `/np` o `/!last` o `!with`. [Más información aquí](/beatmaps/rank_request)
- `!songinfo` - Muestra información detallada sobre la canción. primero debe utilizar el comando `/np` o `/!last` o `!with`.
- `!songinfo <mods>` - `!songinfo` + Mostrar PP para el beatmap solicitado anteriormente con los mods solicitados. Los mods soportados son `NF, EZ, HD, HR, DT, HT, NC, FL, SO`. No use espacios para múltiples mods (ej: `!songinfo HDNC`).
- `!md5tobid <Beatmap_md5> ` - Devuelve el `beatmapID` del `md5` de entrada.
- `!kickself` - patéate a ti mismo
- `!bpp` - Entre todos sus registros, el registro con el pp más alto se devuelve a través del comando `!last`.
- `!replay <vn/rx/ap> <ReplayID>` - Devuelve el registro de reproducción de la canción utilizando el replayID.
- `!history <vn/rx/ap> <BeatmapID>` - Devuelve el registro de todas las reproducciones de la canción utilizando el beatmapID.
- `!mapsuggest <jump/stream/+set(1000,999)>` - recomiendan mapas de stream o jump. [por 1000](https://redstar.moe/u/1000)
- `!status` - Compruebe el estado del servidor. [Bancho](https://c.redstar.moe/api/v1/serverStatus), [lets](https://old.redstar.moe/letsapi/v1/status), [api](https://redstar.moe/api/v1/ping), [mediaserver](https://b.redstar.moe/status)

### Comandos de `!mp` (Torneo)
- `!mp <subcommand>` - principal
- `subcommands` = listref|addref|rmref|make|close|join|lock|unlock|size|move|host|clearhost
|start|invite|map|set|abort|kick|password|randompassword|mods|team|settings|scorev|help

### Comandos de preguntas frecuentes
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

### Comandos de tipo Tillerino
Fokabot tiene algunos comandos similares a Tillerino. Esos comandos sólo funcionan si se envían a Fokabot a través de un mensaje privado. Recuerde que el sistema PP se ha implementado sólo en osu!standard y osu!mania. El bot no soporta recomendaciones de mapas por el momento, esa funcionalidad vendrá después, ojalá.

- `/np` - Muestra la cantidad de PP para la canción que se está reproduciendo  (sólo si es una canción de osu! standard)

- `!last` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada (Detecta automáticamente vn, rx, ap en función de la persona que ejecutó el comando)
- `!last vn` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada (Vanilla)
- `!last rx` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada (Relax)
- `!last ap` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada (AutoPilot)

- `!last <beatmapID>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por beatmapID (Detecta automáticamente vn, rx, ap en función de la persona que ejecutó el comando)
- `!last vn <beatmapID>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por beatmapID (Vanilla)
- `!last rx <beatmapID>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por beatmapID (Relax)
- `!last ap <beatmapID>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por beatmapID (Autopilot)

- `!last <username_safe>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por username (Detecta automáticamente vn, rx, ap en función de la persona que ejecutó el comando)
- `!last vn <username_safe>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por username (Vanilla)
- `!last rx <username_safe>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por username (Relax)
- `!last ap <username_safe>` - Muestra información (y los PPs obtenidos, si fue una puntuación de osu! standard) respecto a la última puntuación enviada por username (Autopilot)

- `!with <mods>` - Muestra la cantidad de PP para el mapa anterior solicitado con los mods solicitados. Los mods soportados son `NF, EZ, HD, HR, DT, HT, NC, FL, SO.`. No utilice espacios para múltiples mods (por ejemplo: `!with HDHR`)

- `!token.tillerino` - Comprobar información de token.tillerino `[Beatmap_ID, mod (número), acc, by]`
- `!del token.tillerino` - Borrar valor token.tillerino (reinicio) `[0, 0, -1.0, by !del token.tillerino]`
- `!input token.tillerino <Beatmap_ID> <mod (número)>(opciones) <acc>(opciones) <by>(opciones)` - Insertar valor token.tillerino

### Comandos Beatmap Nominator
- `!map <ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>` - Cambiar el estado del rank del beatmap.

### Comandos administrativos
- `!system restart` - Reinicia el servidor. Todos serán desconectados y reconectados automáticamente
- `!system status` - Muestra el estado del servidor
- `!system reload` - Recarga los ajustes de Bancho (los que son editables desde RAP)
- `!system maintenance on/off` - Activa/desactiva el modo de mantenimiento de Bancho
- `!moderated on/off` - Activa/desactiva el modo moderado para el canal actual
- `!silence <nombre de usuario> <tiempo> <unidad (s/m/h/d)> <razón>` - Silencia un usuario
- `!removesilence <target>` - Elimina el silencio del target 
- `!kick <nombre de usuario>` - Botar a un usuario del servidor
- `!ban <nombre de usuario>` - Banear y botar a alguien
- `!unban <nombre de usuario>` - Eliminar el ban de alguien
- `!restrict <nombre de usuario>` - Poner a alguien en modo restringido
- `!unrestrict <nombre de usuario>` - Eliminar el modo restringido a alguien
- `!fokabot reconnect` - Reconecta Fokabot si ya no está en la lista de usuarios
- `!alert <mensaje>` - Envía una notificación a cada usuario conectado a Bancho
- `!alertuser  <nombre de usuario> <mensaje>` - Envía una notificación a un usuario específico

- `!vbri <True(1)/False(0)/check>` - Este comando determina si se muestran los registros de las personas baneadas en la tabla de clasificación ingame.
<!-- Ingame의 leaderboard에서 banned당한 사람들의 기록을 표시여부를 결정하는 명령어 입니다. -->
<!-- This command determines whether to display the records of banned people on the Ingame leaderboard. -->
- `!view_banneduser_record_ingame` - Igual que `!vbri`
- `!view_banneduser` - Igual que `!vbri`