---
title: "Komendy FokaBota"
reference_version: 383b905114b125d7bfd87a7dacdc8b56
---
To są komendy które obsługuje Fokabot, nasz chat bot.

### Generalne komendy
- `!roll` - Podaje losowy numer od 0 do 100
- `!roll num` - Podaje losowy numer od 0 do num
- `!help` - Wyświetla wiadomość pomocniczą
- `!pp [mode]` - Pokazuje twoje obecne pp. Jeśli w miejsce `mode` nic nie jest napisane, Fokabot powie ci ile masz pp dla trybu który aktualnie grasz. Jeśli wpisałeś coś w mode (możesz tam wpisać `std/taiko/ctb/mania`), Fokabot powie ci ile masz pp dla tego trybu. **Ta komenda działa tylko w prywatnych wiadomościach**
- `!update` - Aktualizuj beatmapset który wysłałeś przez `/np`. Użyj tego jeśli właśnie pobrałeś mape z osu!direct a gra uznaje ją za niezaaktualizowaną lub jeśli beatmapa nie może zostać pobrana przez osu!direct bo jest zbyt nowa.

- `!ppboard` - Zmieniono tabelę liderów w grze według pp
- `!scoreboard` - Zmieniono tabelę liderów w grze według score

- `!nerinyan` - nerinyan beatmapset download message (+osu!direct)
- `!dl` - redstar beatmapset download message (+osu!direct)
- `!dl2` - Taki sam jak `!nerinyan`
- `!catboy` - catboy beatmapset download message (+osu!direct)
- `!chimu` - chimu beatmapset download message (+osu!direct)
- `!bloodcat` - Taki sam jak `!chimu`, bloodcat(chimu) beatmapset download message (+osu!direct)
- `!bc` - Taki sam jak `!bloodcat`
- `!sayobot` - sayobot beatmapset download message (+osu!direct)
- `!beatconnect` - beatconnect beatmapset download message (+osu!direct)
- `!mirror` - mirror message, mirror beatmapset download message (+osu!direct)
- `!rankrq` - Jest to komenda Rank Request. Przed jej użyciem należy najpierw użyć komendy `/np` lub `/!last` lub `!with`. [Więcej informacji można znaleźć tutaj](/beatmaps/rank_request)
- `!songinfo` - Wyświetla szczegółowe informacje o utworze. musisz najpierw użyć komendy `/np` lub `/!last` lub `!with`.
- `!songinfo <mods>` - `!songinfo` + Pokazuje PP dla poprzednio wybranej beatmapy z wybranymi modami. Obsługiwane mody to `NF, EZ, HD, HR, DT, HT, NC, FL, SO`. Nie używaj spacji dla wielu modów (np.: `!songinfo HDNC`).
- `!md5tobid <Beatmap_md5> ` - Zwraca `beatmapID` wejściowego `md5`.
- `!kickself` - kopnij się
- `!bpp` - Spośród wszystkich rekordów, rekord z najwyższym pp jest zwracany przez komendę `!last`.
- `!replay <vn/rx/ap> <ReplayID>` - Zwraca rekord odtwarzania utworu przy użyciu identyfikatora replayID.
- `!history <vn/rx/ap> <BeatmapID>` - Zwraca wszystkie odtworzenia utworu przy użyciu identyfikatora beatmapID.
- `!mapsuggest <jump/stream/+set(1000,999)>` - zalecane mapy stream lub jump. [przez 1000](https://redstar.moe/u/1000)
- `!status` - Sprawdź status serwera. [Bancho](https://c.redstar.moe/api/v1/serverStatus), [lets](https://old.redstar.moe/letsapi/v1/status), [api](https://redstar.moe/api/v1/ping), [mediaserver](https://b.redstar.moe/status)
- `!b <BeatmapID>` - Zwraca link osu!direct (b/)
- `!d <BeatmapSetID>` - Zwraca link osu!direct (d/)
- `!lb <std(s)/taiko(t)/ctb(c)/mania(m)> <vn/rx/ap>` - Zwraca ranking

### Komendy `!mp` (Turniej)
- `!mp <subcommand>` - główny
- `subcommands` = listref|addref|rmref|make|close|join|lock|unlock|size|move|host|clearhost
|start|invite|map|set|abort|kick|password|randompassword|mods|team|settings|scorev|help

### Komendy faq
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

### Komendy podobne do Tillerino
Fokabot ma trochę komend podobnych do Tillerino. Te komendy działają tylko jeśli wyślesz je Fokabotowi przez prywatną wiadomość. Pamiętaj że system PP został wprowadzony tylko w osu!standard osu!mania. Bot nie obsługuje rekomendacji map w tym momencie, Ta funkcja zostanie wprowadzona później. Miejmy nadzieje.

- `/np` - Pokaż PP za obecnie graną piosenke  (tylko jeśli to jest piosenka osu!standard)

- `!last` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku (Automatycznie wykrywa vn, rx, ap na podstawie osoby, która wykonała polecenie.)
- `!last vn` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku (Vanilla)
- `!last rx` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku (Relax)
- `!last ap` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku (AutoPilot)

- `!last <beatmapID>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez beatmapID (Automatycznie wykrywa vn, rx, ap na podstawie osoby, która wykonała polecenie.)
- `!last vn <beatmapID>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez beatmapID (Vanilla)
- `!last rx <beatmapID>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez beatmapID (Relax)
- `!last ap <beatmapID>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez beatmapID (Autopilot)

- `!last <username_safe>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez username (Automatycznie wykrywa vn, rx, ap na podstawie osoby, która wykonała polecenie.)
- `!last vn <username_safe>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez username (Vanilla)
- `!last rx <username_safe>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez username (Relax)
- `!last ap <username_safe>` - Pokaż informacje (i zdobyte PP, jeśli to jest piosenka osu!standard) o ostatnim wysłanym wyniku przez username (Autopilot)


- `!with <mods>` - Pokaż PP za ostatnio wysłaną mape z określonymi modami. Wspierane są `NF, EZ, HD, HR, DT, HT, NC, FL, SO.`. Nie używaj spacji dla wielu modów (np: `!with HDHR`)

- `!r` - Poleca Losową Beatmapę (Oblicza średni PP, stosując wagi do 10 najlepszych rekordów PP i dzieląc sumę ważoną przez 10. W przypadku braku trybu, używa maksymalnego osiągalnego PP jako podstawy i poleca mapy w stanie ranked lub approved w zakresie ±50PP od średniego PP.)

- `!token.tillerino` - Sprawdź informacje token.tillerino `[Beatmap_ID, mod (liczba), acc, by]`.
- `!del token.tillerino` - Usuń wartość token.tillerino (reset) `[0, 0, -1.0, by !del token.tillerino]`
- `!input token.tillerino <Beatmap_ID> <mod (number)>(options) <acc>(options) <by>(options)` - Wstaw wartość token.tillerino

### Komendy Beatmap Nominator
- `!map <ranked/approved/loved/qualified/unranked> <set/map> <BeatmapID>` - Zmiana statusu rangi beatmapy.

### Komendy administracji
- `!system restart` - Zrestartuj serwer. Wszyscy zostaną rozłączeni i dołączeni automatycznie
- `!system status` - Pokaż status serwera
- `!system reload` - Przeładuj ustawienia bancho (tylko te edytowalne przez RAP)
- `!system maintenance on/off` - Włącz/wyłącz tryb konwersacji bancho
- `!moderated on/off` - Włącz/wyłącz tryb moderowania dla aktualnego kanału
- `!silence <nazwa użytkownika> <czas> <jednostka (s/m/h/d)> <powód>` - Wycisz użytkownika
- `!removesilence <cel>` - Wyłącz wyciszenie celu 
- `!kick <nazwa użytkownika>` - Wyrzuć użytkownika z serwera
- `!ban <nazwa użytkownika>` - Zbanuj i wyrzuć kogoś
- `!unban <nazwa użytkownika>` - Odbanuj kogoś
- `!restrict <nazwa użytkownika>` - Restrictuj kogoś
- `!unrestrict <nazwa użytkownika>` - Odrestrictuj kogoś
- `!fokabot reconnect` - Połącz ponownie Fokabota jeśli nie jest na liście użytkowników online
- `!alert <wiadomość>` - Wyślij powiadomienie do każdego użytkownika na bancho
- `!alertuser  <nazwa użytkownika> <wiadomość>` - Wyślij powiadomienie do danego użytkownika

- `!vbri <True(1)/False(0)/check>` - To polecenie określa, czy rekordy zbanowanych osób mają być wyświetlane na tablicy wyników w grze.
<!-- Ingame의 leaderboard에서 banned당한 사람들의 기록을 표시여부를 결정하는 명령어 입니다. -->
<!-- This command determines whether to display the records of banned people on the Ingame leaderboard. -->
- `!view_banneduser_record_ingame` - Taki sam jak `!vbri`
- `!view_banneduser` - Taki sam jak `!vbri`