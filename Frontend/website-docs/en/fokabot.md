---
title: "FokaBot Commands"
old_id: 4
---
These are the commands supported by FokaBot, our chat bot.

### General commands
- `!roll` - Returns a random number from 0 to 100
- `!roll num` - Returns a random number from 0 to num
- `!help` - Display help message
- `!pp [mode]` - Show your current pp. If `mode` is not present, FokaBot will tell you the amount of PP for your current game mode. If mode is present (it can be `std/taiko/ctb/mania`), FokaBot will tell you the amount of PP for that gamemode. **This command works only in PMs**
- `!update` - Update the beatmapset you've `/np`ed in our beatmap mirror. Use this if you've just downloaded a beatmap from osu!direct and it shows as outdated or if a beatmap can't be downloaded from osu!direct because it's too new.

- `!ppboard` - Changed Ingame Leaderboard by pp
- `!scoreboard` - Changed Ingame Leaderboard by score

- `!nerinyan` - nerinyan beatmapset download message (+osu!direct)
- `!dl` - redstar beatmapset download message (+osu!direct)
- `!dl2` - Same As `!nerinyan`
- `!catboy` - catboy beatmapset download message (+osu!direct)
- `!chimu` - chimu beatmapset download message (+osu!direct)
- `!bloodcat` - Same As `!chimu`, bloodcat(chimu) beatmapset download message (+osu!direct)
- `!bc` - Same As `!bloodcat`
- `!sayobot` - sayobot beatmapset download message (+osu!direct)
- `!beatconnect` - beatconnect beatmapset download message (+osu!direct)
- `!mirror` - mirror message, mirror beatmapset download message (+osu!direct)
- `!rankrq` - This is the Rank Request command. Before using, you must use the `/np` or `/!last` or `!with` command first. [Please check here for more details](/beatmaps/rank_request)
- `!songinfo` - Shows detailed information about the song. you must use the `/np` or `/!last` or `!with` command first.
- `!songinfo <mods>` - `!songinfo` + Show PP for the previous requested beatmap with requested mods. Supported mods are `NF, EZ, HD, HR, DT, HT, NC, FL, SO`. Don't use spaces for multiple mods (eg: `!songinfo HDNC`)
- `!md5tobid <Beatmap_md5> ` - Returns the `beatmapID` of the input `md5`.
- `!kickself` - kick yourself
- `!bpp` - Among all your records, the record with the highest pp is returned through the `!last `command.
- `!replay <vn/rx/ap> <ReplayID>` - Returns the play record of the song using the replayID.
- `!history <vn/rx/ap> <BeatmapID>` - Returns the all your plays record of the song using the beatmapID.
- `!mapsuggest <jump/stream/+set(1000,999)>` - recommend stream or jump maps. [by 1000](https://redstar.moe/u/1000)
- `!status` - Check server status. [Bancho](https://c.redstar.moe/api/v1/serverStatus), [lets](https://old.redstar.moe/letsapi/v1/status), [api](https://redstar.moe/api/v1/ping), [mediaserver](https://b.redstar.moe/status)

### `!mp` (Tournament) commands
- `!mp <subcommand>` - main
- `subcommands` = listref|addref|rmref|make|close|join|lock|unlock|size|move|host|clearhost
|start|invite|map|set|abort|kick|password|randompassword|mods|team|settings|scorev|help

### Faq commands
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

### Tillerino-like commands
Fokabot has some commands similar to Tillerino. Those commands work only if you send them to Fokabot through a PM. Remember that PP system has been implemented only on osu!standard and osu!mania. The bot doesn't support beatmaps recommendations at the moment, that functionality wil come later, hopefully.

- `/np` - Show PP for the current playing song  (only if is a osu! standard song)

- `!last` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score (Automatically detects vn, rx, ap based on the person who executed the command)
- `!last vn` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score (Vanilla)
- `!last rx` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score (Relax)
- `!last ap` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score (AutoPilot)

- `!last <beatmapID>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by beatmapID (Automatically detects vn, rx, ap based on the person who executed the command)
- `!last vn <beatmapID>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by beatmapID (Vanilla)
- `!last rx <beatmapID>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by beatmapID (Relax)
- `!last ap <beatmapID>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by beatmapID (Autopilot)

- `!last <username_safe>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by username (Automatically detects vn, rx, ap based on the person who executed the command)
- `!last vn <username_safe>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by username (Vanilla)
- `!last rx <username_safe>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by username (Relax)
- `!last ap <username_safe>` - Show info (and gained PP, if it was an osu! standard score) about the last submitted score by username (Autopilot)

- `!with <mods>` - Show PP for the previous requested beatmap with requested mods. Supported mods are `NF, EZ, HD, HR, DT, HT, NC, FL, SO.`. Don't use spaces for multiple mods (eg: `!with HDHR`)

- `!token.tillerino` - Check information of token.tillerino `[Beatmap_ID, mod (number), acc, by]`
- `!del token.tillerino` - Delete token.tillerino value (reset) `[0, 0, -1.0, by !del token.tillerino]`
- `!input token.tillerino <Beatmap_ID> <mod (number)>(options) <acc>(options) <by>(options)` - Insert token.tillerino value

### Beatmap Nominator commands
- `!map <ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>` - Change the rank status of the beatmap.

### Admin commands
- `!system restart` - Restart the server. Everyone will be disconnected and reconnected automatically
- `!system status` - Show server status
- `!system reload` - Reload bancho settings (the one that are editable from RAP)
- `!system maintenance on/off` - Turn on/off bancho maintenance mode
- `!moderated on/off` - Turn on/off moderated mode for the current channel
- `!silence <username> <count> <unit (s/m/h/d)> <reason>` - Silence a user
- `!removesilence <target>` - Remove target's silence 
- `!kick <username>` - Kick an user from the server
- `!ban <username>` - Ban and kick someone
- `!unban <username>` - Unban someone
- `!restrict <username>` - Restrict someone
- `!unrestrict <username>` - Unrestrict someone
- `!fokabot reconnect` - Reconnect Fokabot if he's not on online users list anymore
- `!alert <message>` - Send a notification to every user connected to bancho
- `!alertuser  <username> <message>` - Send a notification to a specific user

- `!vbri <True(1)/False(0)/check>` - This command determines whether to display the records of banned people on the Ingame leaderboard.
<!-- Ingame의 leaderboard에서 banned당한 사람들의 기록을 표시여부를 결정하는 명령어 입니다. -->
<!-- This command determines whether to display the records of banned people on the Ingame leaderboard. -->
- `!view_banneduser_record_ingame` - Same as `!vbri`
- `!view_banneduser` - Same as `!vbri`