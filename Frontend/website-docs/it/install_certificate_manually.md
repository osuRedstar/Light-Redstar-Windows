---
title: "Installazione manuale del certificato"
reference_version: 4548a100846bda49251451f487abbdad
---
Se riscontri dei problemi nel connetterti a Redstar o lo switcher non installa correttamente il certificato, puoi installare il certificato manualmente.

### Istruzioni
- Per prima cosa, scarica il certificato [cliccando qui](https://github.com/osuRedstar/Light-Redstar-Windows/raw/main/nginx/osu/cert/openssl/rootca.crt)
- In seguito, apri **certificate.cer**
- Clicca **Installa certificato...**
- Clicca **Avanti**
- Seleziona **Posiziona tutti i certificati nel seguente archivio** (seconda opzione), poi clicca **Sfoglia...**
- Spunterà una nuova finestra, seleziona **Autorità di certificazione fonti attendibili** e clicca **Ok**
- Clicca **Avanti**
- Clicca **Fine**

### Come testare il certificato
Una volta installato il certificato, puoi testare se è stato installato correttamente seguendo questi passi:

- Apri il server switcher e clicca su **Inspect**.
- Aspetta un paio di secondi e tutte le diciture nella sezione "Server connection" section, sulla destra, dovrebbero diventare verdi e riportare "OK" ([così](https://i.ibb.co/68TL6zT/Settings-Form.png)). In tal caso, dovresti essere in grado di collegarti a Redstar.
- Se ottieni **CERT ERROR**, il certificato non è stato installato correttamente. **Segui le istruzioni in basso.**
- Se ottieni **"..."**, non sei connesso a Redstar. Chiudi la finestra, clicca su **Switch to Redstar** e riprova.

### Se qualcos'altro non va a buon fine...
...puoi provare a rimuovere tutti i certificati esistenti di Redstar ed installare il certificato nuovamente. Segui questi passaggi:

- Premi **Win+R**
- Digita `mmc certmgr.msc` nella finestra esegui e premi **invio** per aprire il Gestore Certificati
- Seleziona **Autorità di certificazione radice attendibili** sulla sinistra
- Seleziona **Certificati** sulla destra
- Dovresti vedere alcune voci di **[Redstar](http://y.zxq.co/bbyxev.png)** e alcune voci di **\*.ppy.sh** nella lista. Selezionale, **click destro** e clicca su **Rimuovi**
- Seleziona tutte le opzioni positive (Ok/Sì ecc)
- Riavvia lo switcher, clicca su **Inspect**, poi clicca su **Install certificate**, successivamente **Sì**
- Clicca su **Test redstar connection** e dovresti vedere "OK" per tutti i domini
**Se la finestra inspect è apposto ma non riesci ancora a collegarti a redstar dal client di gioco, prova ad avviare osu! come amministratore**.