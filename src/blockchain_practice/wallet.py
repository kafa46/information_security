import base58
import codecs
import hashlib
from ecdsa import NIST256p, SigningKey

class Wallet:
    '''비트코인 전자지갑'''
    def __init__(self) -> None:
        self._private_key = SigningKey.generate(curve=NIST256p)
        self._public_key = self._private_key.get_verifying_key()
        self._blockchain_address = self.generate_blockchain_address()
    
    @property
    def blockchain_address(self) -> str:
        return self._blockchain_address
    
    @property
    def private_key(self) -> str:
        '''private key를 문자열로 변환'''
        return self._private_key.to_string().hex()
    
    @property
    def public_key(self) -> str:
        '''public key를 문자열로 변환'''
        return self._public_key.to_string().hex()
    
    def generate_blockchain_address(self) -> str:
        '''블록체인(지갑) 주소 생성'''
        # Step 1. __init__에서 이미 수행완료
        # Step 2. Public key에 SHA-256 수행
        public_key_bytes = self._public_key.to_string()
        sha256_bpk = hashlib.sha256(public_key_bytes)
        sha256_bpk_digest = sha256_bpk.digest()
        # Step 3. SHA-256 결과에 Ripemd160 수행
        ripemd160_bpk = hashlib.new('ripemd160')
        ripemd160_bpk.update(sha256_bpk_digest)
        ripemd160_bpk_digest = ripemd160_bpk.digest()
        ripemd160_bpk_digest_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
        # Step 4. Network byte 추가
        network_coin_public_key = b'00' + ripemd160_bpk_digest_hex
        network_coin_public_key_bytes = codecs.decode(
            network_coin_public_key, 'hex'
        )
        # Step 5. SHA-256 2회 수행
        sha256_bpk_digest = hashlib.sha256(network_coin_public_key_bytes).digest()
        sha256_2_bpk_digest = hashlib.sha256(sha256_bpk_digest).digest()
        sha256_hex = codecs.encode(sha256_2_bpk_digest, 'hex')
        # Step 6. Checksum 구하기
        checksum = sha256_hex[:8]
        # Step 7. Public key와 checksum 더하기
        addr_hex = (network_coin_public_key + checksum).decode('utf-8')
        # Step 8. 더한 키를 Base58로 인코딩
        blockchain_addr = base58.b58encode(addr_hex).decode('utf-8')
        
        return blockchain_addr
        

def test():
    wallet = Wallet()
    print(f'Private key: {wallet.private_key}')
    print(f'Public key: {wallet.public_key}')
    print(f'Wallet blockchain addr: {wallet.blockchain_address}')

    
if __name__=='__main__':
    test()