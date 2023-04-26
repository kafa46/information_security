import hashlib
import utils
from ecdsa import NIST256p, SigningKey

class Transaction:
    '''거래 담당 클래스'''
    def __init__(
        self,
        send_private_key: str,
        send_public_key: str,
        send_blockchain_addr: str,
        recv_blockchain_addr: str,
        amount: float    
    ) -> None:
        self.send_private_key = send_private_key
        self.send_public_key = send_public_key
        self.send_blockchain_addr = send_blockchain_addr
        self.recv_blockchain_addr = recv_blockchain_addr
        self.amount = amount
    
    def generate_signature(self) -> str:
        '''거래에 필요한 signature 생성'''
        sha256 = hashlib.sha256()
        transaction = utils.sorted_dict_by_key(
            {
                'send_blockchain_addr': self.send_blockchain_addr,
                'recv_blockchain_addr': self.recv_blockchain_addr,
                'amount': float(self.amount)
            }
        )
        sha256.update(str(transaction).encode('utf-8'))
        message = sha256.digest()
        private_key = SigningKey.from_string(
            bytes().fromhex(self.send_private_key),
            curve=NIST256p
        )
        private_key_sign = private_key.sign(message)
        signature = private_key_sign.hex()
        print(f'generate_signature(self): {signature}')
        return signature

def test():
    from wallet import Wallet
    wallet = Wallet()
    trans = Transaction(
        wallet.private_key,
        wallet.public_key,
        wallet.blockchain_address,
        '홍길동에게 보냄',
        1.0,
    )
    
    print(f'Singature: {trans.generate_signature()}')
    
if __name__=='__main__':
    test()