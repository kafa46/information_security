import logging
import sys
import time
import utils
import json
import hashlib

from ecdsa import VerifyingKey
from ecdsa import NIST256p

# 시스템 운영 시 필요한 로그 메시지 출력을 위한 설정
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

MINING_DIFICULTY = 3
MINING_SENDER = 'BLOCK CHAIN NETWORK'
MINING_REWARD = 1.0

class BlockChain:
    '''블록체인 클래스'''
    def __init__(self, blockchain_addr:str = None) -> None:
        self.transaction_pool = []
        self.chain = []
        # 최초블록(Genesis block) 1개 작성
        self.create_block(nonce=0, prev_hash=self.hash({}))
        self.blockchain_address = blockchain_addr


    def create_block(self, nonce, prev_hash):
        '''블록체인에서의 새로운 단위 블록 생성'''
        block = utils.sorted_dict_by_key(
            {
                'timestamp': time.time(),
                'transactions': self.transaction_pool,
                'nonce': nonce,
                'prev_hash': prev_hash,
            }
        )

        # 새롭게 만든 블록을 블록체인의 마지막에 추가
        self.chain.append(block)

        # transacntion 정보가 새로운 블록에 반영되었으므로
        #   -> transaction_pool을 초기화
        self.transaction_pool = []

        return block


    def hash(self, block):
        sorted_block = json.dumps(block, sort_keys=True)
        return hashlib.sha256(sorted_block.encode()).hexdigest()

    # 업데이트
    def add_transaction(
        self, 
        send_blockchain_addr:str, 
        recv_blockchain_addr:str, 
        amount:float,
        send_public_key: str = None,
        signature: str = None,
    ) -> bool:
        transaction = utils.sorted_dict_by_key(
            {
                'send_blockchain_addr': send_blockchain_addr,
                'recv_blockchain_addr': recv_blockchain_addr,
                'amount': float(amount),
            }
        )
        # 마이닝 하는 사람은 검증없이 transaction pool에 추가
        if send_blockchain_addr == MINING_SENDER:
            self.transaction_pool.append(transaction)
            return True
        
        # transaction 검증 과정
        verify_result = self.verify_transaction_signature(
            send_public_key,
            signature,
            transaction
        )
        
        # 검증을 통과하면 transaction pool에 추가
        if verify_result:
            self.transaction_pool.append(transaction)
            return True
        
        return False
    
    # 메서드 추가
    def verify_transaction_signature(
        self, 
        send_public_key: str,
        singature: str,
        transaction: dict
    ) -> bool:
        sha256 = hashlib.sha256()
        sha256.update(str(transaction).encode('utf-8'))
        message = sha256.digest()
        print(f'signature: {singature}')
        singature_bytes = bytes().fromhex(singature)
        verifying_key = VerifyingKey.from_string(
            bytes().fromhex(send_public_key), curve=NIST256p 
        )
        verified_key = verifying_key.verify(
            signature=singature_bytes,
            data=message,
        )
        return verified_key
    
    
    def valid_proof(
        self, 
        transactions:list, 
        prev_hash:str, 
        nonce:int, 
        difficulty:int = MINING_DIFICULTY,
    ) -> int:
        guess_block = utils.sorted_dict_by_key(
            {
                'transactions': transactions,
                'nonce': nonce,
                'prev_hash': prev_hash,
            }
        )
        guess_hash = self.hash(guess_block)
        return guess_hash[:difficulty] == '0' * difficulty
    
    def proof_of_work(self) -> int:
        '''nonce 구하기'''
        transactions: list = self.transaction_pool.copy()
        prev_hash:str = self.hash(self.chain[-1])
        nonce: int = 0
        while self.valid_proof(transactions, prev_hash, nonce) is False:
            nonce += 1
        return nonce


    def mining(self,) -> bool:
        '''블록체인 마이닝(채굴)'''
        self.add_transaction(
            send_blockchain_addr=MINING_SENDER,
            recv_blockchain_addr=self.blockchain_address,
            amount=MINING_REWARD,
        )
        nonce = self.proof_of_work()
        prev_hash = self.hash(self.chain[-1])
        self.create_block(nonce, prev_hash)
        logger.info(
            {
                'action': 'mining',
                'status': 'success'
            }
        )
        return True
    
    
    def calculate_total_amount(self, blockchain_addr:str) -> float:
        '''blockchain_addr에 해당하는 계좌의 총액 구하기'''
        total_amount = 0.0
        for block in self.chain:
            # 체인으로 연결된 모든 블록을 검사
            for transaction in block['transactions']:
                # 개별 블록에 포함된 모든 거래 내역 검사
                value = float(transaction['amount'])
                if blockchain_addr == transaction['recv_blockchain_addr']:
                    # 계산할 주소와 돈 받은 주소가 동일하면 금액 추가
                    total_amount += value
                if blockchain_addr == transaction['send_blockchain_addr']:
                    # 계산할 주소와 송금한 주소가 동일하면 금액 빼기
                    total_amount -= value
        return total_amount
                    
        
def test():
    '''테스트 함수'''
    my_blockchain_addr = 'my_blockchain_address'
    blockchain = BlockChain(my_blockchain_addr)
    
    blockchain.add_transaction('A', 'B', 1.0)
    blockchain.mining()

    blockchain.add_transaction('B', 'C', 2.0)
    blockchain.add_transaction('X', 'Y', 3.0)
    blockchain.mining()
    
    utils.print_blockchain(blockchain.chain)
    
    print(f'채굴한사람: {blockchain.calculate_total_amount(my_blockchain_addr)}')
    print(f'A: {blockchain.calculate_total_amount("A")}')
    print(f'B: {blockchain.calculate_total_amount("B")}')
    print(f'X: {blockchain.calculate_total_amount("X")}')
    print(f'Y: {blockchain.calculate_total_amount("Y")}')
    

if __name__=='__main__':
    test()

