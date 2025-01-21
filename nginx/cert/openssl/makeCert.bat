REM key ����
openssl genrsa -out cert.key 2048
REM csr ����
openssl req -new -key cert.key -out cert.csr -config makeCert.conf
REM ������ �߱�
openssl x509 -req -days 36524 -extensions v3_user -in cert.csr -signkey cert.key -out cert.crt -extfile makeCert.conf
del /f /q cert.csr
pause