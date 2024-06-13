---
title: "Installing the certificate manually"
reference_version: 4548a100846bda49251451f487abbdad
---
If you're having troubles connecting to Redstar or the switcher doesn't install the certificate properly, you can try installing it manually.

### Instructions
- First, download the certificate [by clicking here](https://zxq.co/ripple/ripple-server-switcher/-/raw/master/RippleServerSwitcher/Resources/ripple.cer?inline=false)
- Then, open **certificate.cer**
- Click **Install certificate...**
- Click **Next**
- Select **Place all certificates in the following store** (second option), then click **Browse...**
- A new window will pop up, select **Trusted root certification authorities** and click **Ok**
- Click **Next**
- Click **Finish**

### How to test the certificate
Once you've installed the certificate, you can test whether it was successfully installed by following these steps:

- Open the server switcher and click on **Inspect**.
- Wait a few seconds and all the labels in the "Server connection" section, on the right, should become green and report "OK" (like [this](https://i.ibb.co/68TL6zT/Settings-Form.png)). If so, you should be able to connect to Redstar.
- If you get **CERT ERROR**, the certificate has not been installed successfully. **Follow the instructions below.**
- If you get **"..."**, you're not connected to Redstar. Close the inspect window, click on **Switch to Redstar** and try again.

### If everything else fails...
...you can try to remove all existing Redstar certificates and install the certificate again. Follow these steps:

- Press **Win+R**
- Type `mmc certmgr.msc` in the run box and press **enter** to open the Certificate Manager
- Select **Trusted root certification authorities** on the left
- Select **Certificates** on the right
- You should see some **[Redstar](http://y.zxq.co/bbyxev.png)** and some **\*.ppy.sh** entries in the list. Select them, **right click** and click on **Delete**  
- Select all the positive options (Ok/Yes etc)
- Restart the switcher, click on **Inspect**, then choose **Install certificate**, then **Yes**
- Click on **Test redstar connection** and you should see "OK" for every domains
**If the inspect dialog is fine but you still can't connect to redstar from the game client, try running osu! as administrator**.