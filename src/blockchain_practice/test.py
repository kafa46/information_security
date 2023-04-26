import utils
from blockchain import BlockChain
from wallet import Wallet
from transaction import Transaction

def blockchain_test():
    '''지금까지 만든것 테스트'''
    
    ##########################
    ### 개인들끼리 거래 상황 ###
    ###########################
    wallet_Miner = Wallet() # 채굴하는 사람 지갑
    wallet_A = Wallet() # A라는 사람의 지갑
    wallet_B = Wallet() # B라는 사람의 지갑
    
    # 거래 생성: A -> B에게 1.0 코인 송금
    trans = Transaction(
        send_private_key=wallet_A.private_key,
        send_public_key=wallet_A.public_key,
        send_blockchain_addr=wallet_A.blockchain_address,
        recv_blockchain_addr=wallet_B.blockchain_address,
        amount=1.0
    )
    print(
        f'trans.generate_signature(): {trans.generate_signature()}'
    )
    #####################################
    ### 블록체인 네트워크 - 노드의 상황 ###
    #####################################
    
    # 채굴자를 통해 최초 제네시스 블록 생성
    blockchain = BlockChain(
        blockchain_addr=wallet_Miner.blockchain_address
    )
    
    chain_add_success = blockchain.add_transaction(
        send_blockchain_addr=wallet_A.blockchain_address,
        recv_blockchain_addr=wallet_B.blockchain_address,
        amount=1.0,
        send_public_key=wallet_A.public_key,
        signature= trans.generate_signature(),
    )
    
    print(f'블록체인 추가 여부: {chain_add_success}')
    

    blockchain.mining()
    utils.print_blockchain(blockchain.chain)
    
    # 개인별 계좌 상황 확인
    amount_miner = blockchain.calculate_total_amount(
        wallet_Miner.blockchain_address
    )
    amount_A = blockchain.calculate_total_amount(
        wallet_A.blockchain_address
    )
    amount_B = blockchain.calculate_total_amount(
        wallet_B.blockchain_address
    )
    print(f'채굴자: {amount_miner}')
    print(f'A: {amount_A}')
    print(f'B: {amount_B}')
    
if __name__=='__main__':
    blockchain_test()
    
    
    