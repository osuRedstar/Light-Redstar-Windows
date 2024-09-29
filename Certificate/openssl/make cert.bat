echo cert Ű ����
openssl genrsa -aes256 -out cert.key 2048


echo cert Ű ��й�ȣ ����
openssl rsa -in cert.key -out cert.key


echo cert.conf ���� ����
echo conf/cert.conf


echo cert csr ����
openssl req -new -key cert.key -out cert.csr -config conf/cert.conf


echo cert ������ �߱�
openssl x509 -req -days 36524 -extensions v3_user -in cert.csr -CA rootca.crt -CAcreateserial -CAkey rootca.key -out cert.crt -extfile conf/cert.conf

pause