---
title: "Manualna instalacja certyfikatu"
reference_version: 96a9ef2265cef92f7a7014f3303b74b9
---
Jeśli masz problemy z połączeniem się z Redstar używając stable (latest)/beta/cuttingedge albo przełącznik nie instaluje poprawnie certyfikatu, możesz zainstalować certyfikat manualnie.

### Instrukcje
- Najpierw, pobierz certyfikat [klikając tutaj](https://github.com/osuRedstar/Light-Redstar-Windows/raw/main/nginx/osu/cert/openssl/rootca.crt)
- Potem, otwórz **certificate.cer**
- Kliknij **Zainstaluj certyfikat...**
- Kliknij **Dalej**
- Wybierz **Umieść wszystkie certyfikaty w następującym magazynie** (druga opcja), i wtedy kliknij **Przeglądaj...**
- Wyskoczy wtedy nowe okno, wybierz **Zaufane główne urzędy certyfikacji** i kliknij **Ok**
- Kliknij **Dalej**
- Kliknij **Zakończ**

### Jak przetestować certyfikat
By sprawdzić czy certyfikat został zainstalowany poprawnie, upewnij się, że przełącznik jest **uruchomiony** i otwórz [tą stronę](https://c.ppy.sh).

- Jeśli widzisz **[rzeczy z osu!bancho](http://y.zxq.co/ubfzty.png)**, przełącznik jest wyłączony. **Włącz go i spróbuj ponownie.**
- Jeśli widzisz **[rzeczy z redstar](http://y.zxq.co/zphobw.png)**, poprawnie połączyłeś się z redstar pod https, **dobra robota!**
- Jeśli dostajesz **[jakieś błędy dotyczące certyfikatu](http://y.zxq.co/reaueu.png)**, certyfikat nie został zainstalowany poprawnie. **Zastosuj się do instrukcji poniżej.**

### Jeśli wszystko inne nie działa...
...Możesz spróbować usunąć wszystkie istniejące certyfikaty Redstar i zainstaluj ponownie certyfikat. Zastosuj się do tych wskazówek:

- Wciśnij **Win+R**
- Wpisz `mmc certmgr.msc` w polu "Otwórz" i wciśnij **enter** by otworzyć Menadżera Certyfikatów
- Wybierz **Zaufane główne urzędy certyfikacji** po lewej
- Wybierz **Certyfikaty** po prawej
- Powinieneś widzieć wpis **[Redstar](http://y.zxq.co/bbyxev.png)** i jeden albo dwa wpisy **\*.ppy.sh** na liście. Wybierz je, wciśnij **prawy przycisk myszy** i kliknij **Usuń**
- Wybierz wszystkie pozytywne opcje
- Otwórz przełącznik, kliknij **Install certificate**, wtedy **Yes**
- Spróbuj połączyć się z [ serwerem bancho redstar'a pod https](https://c.ppy.sh/) i _powinno_ działać