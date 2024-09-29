echo rootca Ű ����
openssl genrsa -aes256 -out rootca.key 2048


echo rootca Ű ��й�ȣ ����
openssl rsa -in rootca.key -out rootca.key


echo rootca.conf ���� ����
echo conf/rootca.conf


echo rootca csr ����
openssl req -new -key rootca.key -out rootca.csr -config conf/rootca.conf


echorootca ������ �߱�
openssl x509 -req -days 36524 -extensions v3_ca -set_serial 1 -in rootca.csr -signkey rootca.key -out rootca.crt -extfile conf/rootca.conf

pause