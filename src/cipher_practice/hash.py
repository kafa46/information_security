import hashlib

input_string = '안녕하세요, 노기섭 교수님^^'

# 입력 문자열 인코딩
encoded = input_string.encode()
print('Encoded >>>')
print(encoded)

# 해시 알고리즘 실행
hashed = hashlib.sha256(encoded)
print('Hashed >>>')
print(hashed)

# 해시 다이제스트
digested = hashed.hexdigest()
print('Digested >>>')
print(digested)
print(f'SHA 256 다이제스트 길이: {len(digested)}')

