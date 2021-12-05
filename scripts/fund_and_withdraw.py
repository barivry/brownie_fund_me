from brownie import accounts, FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAK_BLOCKCHAIN_ENVIRONMANTS
from web3 import Web3

# because we are on the mine net(or simulat this) we need to deploy our deploy onse to creat a contract. this script will work jast on the main net


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
