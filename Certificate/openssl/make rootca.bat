echo rootca 키 생성
openssl genrsa -aes256 -out rootca.key 2048


echo rootca 키 비밀번호 제거
openssl rsa -in rootca.key -out rootca.key


echo rootca.conf 파일 생성
echo conf/rootca.conf


echo rootca csr 생성
openssl req -new -key rootca.key -out rootca.csr -config conf/rootca.conf


echorootca 인증서 발급
openssl x509 -req -days 36524 -extensions v3_ca -set_serial 1 -in rootca.csr -signkey rootca.key -out rootca.crt -extfile conf/rootca.conf

pause