import hashlib
from py3rijndael import Pkcs7Padding
from py3rijndael import RijndaelCbc
from base64 import b64decode, b64encode

def decryptRinjdael(aeskey: str, iv: str, data: str, areBase64: bool=False) -> str:
    """
	Where the magic happens

	aeskey -- AES key (string) \n
	iv -- iv thing (string) \n
	data -- data to decrypt (string) \n
	areBase64 -- if True, iv and data are passed in base64 \n
	"""
    aes = RijndaelCbc(
        key=aeskey.encode(),
        iv=b64decode(iv) if areBase64 else iv,
        padding=Pkcs7Padding(32),
        block_size=32,
    )
    return aes.decrypt(b64decode(data)).decode("utf-8") if areBase64 else aes.decrypt(data).decode("utf-8")

def encryptRinjdael(aeskey: str, iv: str, data: str, areBase64: bool=False) -> str:
    """
	AES CBC 모드로 데이터를 암호화하는 함수

	aeskey -- AES 키 (string) \n
	iv -- 초기화 벡터 (string) \n
	data -- 암호화할 평문 데이터 (string) \n
	areBase64 -- True인 경우, iv는 base64로 디코딩하고 최종 암호문은 base64로 인코딩하여 반환 \n
	"""
    aes = RijndaelCbc(
        key=aeskey.encode(),
        iv=b64decode(iv) if areBase64 else iv,
        padding=Pkcs7Padding(32),
        block_size=32,
    )
    return b64encode(aes.encrypt(data.encode())).decode("latin_1") if areBase64 else aes.encrypt(data.encode()).decode("latin_1")

def compute_online_checksum(scoreData: list, osu_client_hash: str, storyboard_checksum: str) -> str:
    checksum_string = "chickenmcnuggets{}o15{}{}smustard{}{}uu{}{}{}{}{}{}{}Q{}{}{}{}{}{}".format(
        (int(scoreData[3])+int(scoreData[4])), scoreData[5], scoreData[6], scoreData[7], scoreData[8], 
        scoreData[0], scoreData[10], scoreData[11], scoreData[1].strip(), scoreData[9], 
        scoreData[12], scoreData[13], scoreData[14], scoreData[15], scoreData[17], scoreData[16],
        osu_client_hash, storyboard_checksum
    ).encode()
    return hashlib.md5(checksum_string).hexdigest()