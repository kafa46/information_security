import hashlib
import time

def create_csrf_token() -> str:
    '''csrf 토큰 생성'''
    token_bytes = hashlib.sha256(str(time.time()).encode('utf-8'))
    token = token_bytes.hexdigest()
    return token

if __name__=='__main__':
    create_csrf_token()
