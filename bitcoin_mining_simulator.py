import time
from hashlib import sha256

# Max number of nonce attempts
MAX_NONCE = 10000000000

def SHA256(text):
    """Function to apply SHA-256 hashing algorithm on input text"""
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    """
    Function to mine a block by finding a valid nonce that results in a hash
    starting with a certain number of zeros.
    
    Arguments:
    block_number -- the number of the current block
    transactions -- transaction details to be included in the block
    previous_hash -- the hash of the previous block
    prefix_zeros -- the number of leading zeros the hash should start with
    
    Returns:
    new_hash -- the successfully mined hash
    """
    # Creating a string of zeros that the hash should start with
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        # Combining the block data (block number, transactions, previous hash, and nonce)
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        
        # If the hash starts with the required number of zeros, we've mined the block
        if new_hash.startswith(prefix_str):
            print(f"Yayyyy! I mined bitcoins with nonce value: {nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times")

if __name__ == "__main__":
    # Sample transactions to be included in the mined block
    transactions = '''
    Sheron->Janz->20,
    Zera->Luxsi->29,
    Thara->Buchi->50
    '''
    
    # Setting the mining difficulty (number of leading zeros in the hash)
    difficulty = 3
    print("Mining start")

    # Starting the mining process and measuring the time taken
    start = time.time()
    new_hash = mine(5, transactions, '0000000a036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)

    # Displaying the time taken and the successfully mined hash
    print(f"Time taken to mine: {time.time() - start}")
    print(new_hash)
