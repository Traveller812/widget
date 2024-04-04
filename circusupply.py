from web3 import Web3
import api6

# Initialize Web3 with Infura API endpoint
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/88431cb6f9db49d2b4650fd78717fc88'))

# ERC20 contract ABI
erc20_abi = api6.abi

# Token contract address
token_address = '0x50739bd5b6afF093ba2371365727C48a420a060D'

# Addresses for burn, lock, and liquidity
burn_address = Web3.to_checksum_address('0x000000000000000000000000000000000000dead')
lock_address = Web3.to_checksum_address('0x71b5759d73262fbb223956913ecf4ecc51057641')

# Instantiate ERC20 contract
erc20_contract = web3.eth.contract(address=token_address, abi=erc20_abi)

# Define a function to convert token balance to human-readable format
def from_wei(balance):
    return balance / 10**18

# Get balances of addresses and convert them to human-readable format
burn_balance = from_wei(erc20_contract.functions.balanceOf(burn_address).call())
lock_balance = from_wei(erc20_contract.functions.balanceOf(lock_address).call())

# Total supply (you need to replace this with the actual total supply)
total_supply = 21000000

# Calculate circulating supply
circulating_supply = total_supply - burn_balance - lock_balance

print(f"Circulating Supply: {circulating_supply:,.0f} $CRGPT")
print (f"Total Supply: {total_supply:,.0f} $CRGPT")
