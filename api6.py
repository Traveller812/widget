abi = [
        {
            "inputs": [
            {
                "internalType": "string",
                "name": "name_",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol_",
                "type": "string"
            },
            {
                "internalType": "uint8",
                "name": "decimals_",
                "type": "uint8"
            },
            {
                "internalType": "uint256",
                "name": "totalSupply_",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "pinkAntiBot_",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "serviceFeeReceiver_",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "serviceFee_",
                "type": "uint256"
            }
            ],
            "stateMutability": "payable",
            "type": "constructor"
        },
        {
            "anonymous": False,
            "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "token",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "enum TokenType",
                "name": "tokenType",
                "type": "uint8"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "version",
                "type": "uint256"
            }
            ],
            "name": "TokenCreated",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "VERSION",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
            ],
            "name": "allowance",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
            ],
            "name": "approve",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "balanceOf",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                "type": "uint256"
            }
            ],
            "name": "decreaseAllowance",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "enableAntiBot",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                "type": "uint256"
            }
            ],
            "name": "increaseAllowance",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "pinkAntiBot",
            "outputs": [
            {
                "internalType": "contract IPinkAntiBot",
                "name": "",
                "type": "address"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bool",
                "name": "_enable",
                "type": "bool"
            }
            ],
            "name": "setEnableAntiBot",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
            ],
            "name": "transfer",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
            ],
            "name": "transferFrom",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
]
