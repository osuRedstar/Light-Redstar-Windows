# Redstar

## requirements.txt

- rootFolder/requirements.txt

## Youtube Link
[![Video Label](http://img.youtube.com/vi/KDJ9fqeqM30/0.jpg)](https://youtu.be/KDJ9fqeqM30)

## Domain List

- osu.{Your_Domain} (osu connect with -devserver option (-devserver {Your_Domain}))
- admin.{Your_Domain} (Admin Panel - Realistik Panel)
- assets.{Your_Domain}
- a.{Your_Domain} (Avatar Server)
- b.{Your_Domain} (osu!direct thumb img & preview Server) (using RedstarOSU's mediaserver or redirect b.ppy.sh)
- c.{Your_Domain} (Main Server - Bancho) | (c1~c6, ce).{Your_Domain} (option)
- cheesegull.{Your_Domain} (cheeesegull)
- old.{Your_Domain} (Lets Server - Score Server)
- new.{Your_Domain}

---

## Nginx

- nginx 폴더에 temp, logs 폴더가 없으므로 temp, logs 폴더를 생성해주세요.
    - There are no temp, logs folders in the nginx folder, so please create temp, logs folders.
- nginx.conf, nginx2.conf(추가기능)을 당신의 맞게 수정하세요
    - Modify nginx.conf, nginx2.conf (additional functions) to suit your needs.

---

## Redis

- redis.windows.conf 에서 비밀번호를 변경 가능 하며 (requirepass), redis.bat 으로 redis서버를 설정파일과 함께 실행합니다.
    - You can change the password in redis.windows.conf (requirepass), and run the redis server with the configuration file using redis.bat.

---

## Cheesegull

- cheesegull의 설정을 당신에 맞게 변경하면 됩니다.
    - Just change cheesegull's settings to suit you.
- cheesegull을 사용하고 싶지 않다면 lets, pep.py 폴더속에 config.ini 파일의 cheesegull 주소를 다른 서버의 주소로 변경하면 됩니다.
    - If you do not want to use cheesegull, you can change the cheesegull address in the config.ini file in the lets, pep.py folder to the address of another server.

---

## Realistik Panel

- config.json을 당신의 맞게 수정하세요
    - Modify config.json to suit your needs

---

## API, Frontend (+WSL)

- API, Frontend는 리눅스를 사용하기 때문에 Windows 환경이라면 WSL을 설치해야합니다.
    - The API and Frontend use Linux, so if you are in a Windows environment, you need to install WSL.
- WSL 버전은 1이어야 합니다. 호스트의 IP 주소를 사용하려면 WSL 버전이 1이어야 합니다.
    - WSL version must be 1. The WSL version must be 1 to use the host's IP address.

---

## Mediaserver

- b.{Your_Domain}은 RedstarOSU의 mediaserver로 요청이 전달됩니다. Mediaserver를 사용하고 싶지 않다면 nginx에서 b.ppy.sh로 리다이렉트 시켜야 합니다.
    - b.{your domain} will send the request to RedstarOSU's mediaserver. If you do not want to use mediaserver, you must redirect nginx to b.ppy.sh.


# Ripple

<h1 align="center">
  Self Hosted <a href=https://ripple.moe>RIPPLE</a> (Windows Edition)
</h1>
<h4 align="center">Self-Hosted Ripple Code ! Can be used with a bit modification. (For Personal Use)</h4>

<p align="center">
  <img src="https://img.shields.io/badge/Maintained%3F-No-red?style=for-the-badge">
  <img src="https://img.shields.io/github/license/Uniminin/Light-Ripple-Windows?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/Uniminin/Light-Ripple-Windows?color=violet&style=for-the-badge">
  <img src="https://img.shields.io/github/stars/Uniminin/Light-Ripple-Windows?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/Uniminin/Light-Ripple-Windows?color=teal&style=for-the-badge">
  <img src="https://github.com/Uniminin/Light-Ripple-Windows/blob/master/RIPPLE.PNG"/>
</p>

### Requirements:
* <a href=https://conemu.github.io>ConEmu</a> FOSS windows terminal emulator. (Recommended)
* <a href=https://www.python.org/downloads/release/python-368>Python 3.6+</a> (with pip, add python to path for windows)
* <a href=https://www.apachefriends.org/index.html>XAMPP</a>
* <a href=http://nginx.org/en/download.html>NGINX</a> (nginx 1.16.1)
* <a href=https://github.com/tporadowski/redis/releases>REDIS</a> (For Windows)
* <a href="https://go.microsoft.com/fwlink/?LinkId=691126">Visual C++ Build Tools 2015</a>
* <a href="https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab">Ubuntu 18.04 LTS (WSL)</a> WSL Enabled with A Ubuntu Terminal to run efl binaries i.e hanayo, api.

### Setting up
* Download or clone the upstream repository with `git clone https://github.com/Uniminin/Light-Ripple-Windows`.
* Create and Run MySQL Database Server.
* Connect to MySQL DB and import <a href=https://github.com/Uniminin/Light-Ripple-Windows/blob/master/SQL/RIPPLE.sql>RIPPLE</a> SQL query.
* Go to `pep.py`, `lets` & `avatar-server` Folder and install the necessary python packages with `python3 -m pip install -r requirements.txt`.
* Go to `lets` folder and change my directory to yours in `lets/pp/rippoppai.py` and `lets/pp/relaxoppai.py`. Create a `replays` folder in `lets/.data/replays` if there isn't any.
* Edit `config.ini` and change it. (Both in pep.py & lets folder)
* Go to `api` and edit `api.conf`.
* Go to `Frontend` and edit `hanayo.conf`.
* You can get OSU!API Key here: <a href=https://old.ppy.sh>OSU!API</a>.
* Go to `nginx-1.16.1` folder and edit the content of `conf/nginx.conf`, `osu/nginx.conf` and `osu/old-frontend.conf`. Replace my directory with your one.
* You can switch to localhost server and bancho either by <a href=https://github.com/Uniminin/Light-Ripple-Windows/blob/master/Switcher/LocalHost.exe>LocalHost.exe</a> Switcher or Manually by:
* Install <a href=https://github.com/Uniminin/Light-Ripple-Windows/blob/master/Certificate/cert.crt>Certificate</a>
* Edit Hosts File in `c:\Windows\System32\Drivers\etc\hosts`. And add <a href=https://raw.githubusercontent.com/Uniminin/Light-Ripple-Windows/master/Hosts/hosts.txt>this</a> lines to your hosts file.

### Host File & Certificate
```
#<domain that support in certificate> default is i-need-to.click

<127.0.0.1 or your Public IP> osu.ppy.sh
<127.0.0.1 or your Public IP> c.ppy.sh
<127.0.0.1 or your Public IP> c1.ppy.sh
<127.0.0.1 or your Public IP> c2.ppy.sh
<127.0.0.1 or your Public IP> c3.ppy.sh
<127.0.0.1 or your Public IP> c4.ppy.sh
<127.0.0.1 or your Public IP> c5.ppy.sh
<127.0.0.1 or your Public IP> c6.ppy.sh
<127.0.0.1 or your Public IP> c7.ppy.sh
<127.0.0.1 or your Public IP> ce.ppy.sh
<127.0.0.1 or your Public IP> a.ppy.sh
<127.0.0.1 or your Public IP> i.ppy.sh
<127.0.0.1 or your Public IP> <domain that support in certificate>
<127.0.0.1 or your Public IP> c.<domain that support in certificate>
<127.0.0.1 or your Public IP> i.<domain that support in certificate>
<127.0.0.1 or your Public IP> a.<domain that support in certificate>
<127.0.0.1 or your Public IP> old.<domain that support in certificate>
```

These domains are supported by osu!thailand certificate (You can make your by doing a new self-signed certificate)
- tatoe.pw
- i-need-to.click
- keidas.pw
- cookiezi.pw
- kawata.pw

### Manually Creating Passwording (DB)
Ripple uses Password -> MD5 -> BCrypt Hash (10 rounds) for the password to login so in `users` table in `password_md5` column in db.

1. For Example: If you want to make your password `ExamplePassword87`, first you need to hash it as MD5. So the hash will be `df4s5fe65f456344f4re549` (You can hash your password at http://www.md5.cz/).
2. After hashing it, you'll still need to make it as BCrypt Hash (10 Rounds), you can use https://bcrypt-generator.com/ as BCrypt encryptor.
3. Put the MD5 Hash to `String to encrypt` box, change rounds to 10 and then click `Hash!` button.
4. You'll get the hash like `asdjslkfjlkUy89y32098y*(*@#&(*3y928hih32toij[][;gfgd` (which is our MD5 hash. `ExamplePassword87`).
5. Put your BCrypt hash in `password_md5` in your user data (DB).

Note: The BCrypt hash will be always different because BCrypt hashes it 10 times!

### Starting the Server
* Start MySQL (MySQL Server must be started and running).
* Start Redis Server, `Redis/redis-server.exe`.
* Go to `lets` folder and run `python lets.py` (cmd.exe/x-terminal-emulator.exe).
* Go to `pep.py` folder and run `python pep.py` (cmd.exe/x-terminal-emulator.exe).
* Go to `avatar-server` folder and run `python avatar-server.py` (cmd.exe/x-terminal-emulator.exe).
* Go to `api` folder and run `./API` (bash.exe/WSL).
* Go to `Frontend` folder and run `./frontend` (bash.exe/WSL).
* Go to `nginx-1.16.1` folder and run `nginx` (cmd.exe/x-terminal-emulator.exe).

### Logging Into osu!
Before you login you have to create an account. You can create an account either by using the/from frontend which is `i-need-to.click`(default) site or manually from database.
* Use a local database software to log into local database. I recommend <a href=https://www.heidisql.com/download.php>HeidiSQL</a> or <a href=https://www.devart.com/dbforge/mysql/studio/download.html>dbForge Studio</a>.
* Log into local db. Then Click on RIPPLE db. Then head find `users`. And click on `Data` section above.
* In id `1000` fill-up your desired username, notes, and email. (It will have full owner/admin access).
* For Password follow that above section [#manually-creating-passwording-db](https://github.com/Uniminin/Light-Ripple-Windows#manually-creating-passwording-db).
* Then you can login with your username/email and password.

### Credits
* <a href=https://github.com/Kanaze-chan>Kanaze-Chan(Aoba)</a> for their <a href=https://github.com/Kanaze-chan/readme>readme</a>!
* <a href=https://github.com/Hazuki-san>Aoba Suzukaze</a> for their lots of help.

### License :scroll:
All code in this and its related repositories is licensed under the GNU AGPL 3 License. See the `LICENSE` file for more information.
