echo cert 키 생성
openssl genrsa -aes256 -out cert.key 2048


echo cert 키 비밀번호 제거
openssl rsa -in cert.key -out cert.key


echo cert.conf 파일 생성
echo conf/cert.conf


echo cert csr 생성
openssl req -new -key cert.key -out cert.csr -config conf/cert.conf


echo cert 인증서 발급
openssl x509 -req -days 36524 -extensions v3_user -in cert.csr -CA rootca.crt -CAcreateserial -CAkey rootca.key -out cert.crt -extfile conf/cert.conf

pause