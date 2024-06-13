---
title: "How to connect to Redstar"
old_id: 1
---
- First, you have to [Register](http://redstar.moe/index.php?p=3) an account


### How to play on Redstar (Windows Shortcut)
- **Create a shortcut** of your osu!.exe:
    - **If you already have an osu! shortcut on your desktop**, create a copy of it and rename it to "Redstar"
    - **If you don't have one:**
        - Find osu! in your start menu and click "Open file location"
        - Right click osu! in the file explorer and select Open file location
        - Hold Alt and drag osu! on your desktop
        - Click "Create shortcut here"

- Right click on the newly created shortcut and choose "Properties"
- Add a space and `-devserver redstar.moe` at the very end of the **"Target"** field
- **Open the "Redstar" shortcut** and enter your credentials to log in to Redstar

- A video tutorial on how to do this 1 [is linked here](/static/switcher)
- A video tutorial on how to do this 2 [is linked here](https://www.youtube.com/watch?v=NkDMdyLgF0U)

### How to play on Redstar (Steam Shortcut)
- Add osu! as a non-Steam game on Steam
- Right click on osu! on Steam and select Properties
- Rename the game to "Redstar" and add a space and `-devserver redstar.moe` at the end of the "target" field

### How to play on Redstar (Linux)
- Open the script you use to launch osu
- Add `"$@"` after `osu!.exe` if it's not already present. So if it looks like this:

    ```sh
    wine osu\!.exe
    ```

    It will become

    ```sh
    wine osu\!.exe "$@"
    ```

- Then, add `-devserver redstar.moe` when you launch the script. So if you launch osu! with:

    ```sh
    ./osu.sh
    ```

    You can launch Redstar with

    ```sh
    ./osu.sh -devserver redstar.moe
    ```

If you only play on redstar, you can also replace `"$@"` with `-devserver redstar.moe` so you don't have to type the server address each time

### How to play on official osu! again
You can simply launch the appropriate shortcut to launch either osu! or redstar.

Please note that, for security reasons, the client will log you out each time you switch servers.

### Having troubles?
You can check out out [Legacy connection guide](https://redstar.moe/doc/legacy_connection_guide) to use the server switched and https certificate to connect, however this method will be discontinued soon.

Also remember to check out our [FAQ](https://redstar.moe/doc/5)