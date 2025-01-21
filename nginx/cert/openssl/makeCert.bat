REM key 생성
openssl genrsa -out cert.key 2048
REM csr 생성
openssl req -new -key cert.key -out cert.csr -config makeCert.conf
REM 인증서 발급
openssl x509 -req -days 36524 -extensions v3_user -in cert.csr -signkey cert.key -out cert.crt -extfile makeCert.conf
del /f /q cert.csr
pause