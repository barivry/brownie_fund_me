from brownie import accounts, FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAK_BLOCKCHAIN_ENVIRONMANTS
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # This if statment is differantiates between development network and the main network, and if its in tme main network it can look for the net name and select the right address for the AggregatorV3Interface
    # If it is a development network it used mockV3Aggregator to mock the function of AggregatorV3Interface but you neet to put the values in the MockV3Aggregator.deploy function
    if network.show_active() not in LOCAK_BLOCKCHAIN_ENVIRONMANTS:
        price_feed_address = config["networks"][network.show_active(
        )]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    # the addres in the deploy functiion is the address for the price feed of the eth in the AggregatorV3Interface or MockV3Aggregator if its a development network, the vakuse befor the from are going to the constractor
    # the publish_source=True means that the contract will be publisht (working just in thr main net), the Api-Key Token is defind in the .env file under the name ETHERSCAN_TOKEN
    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account},
                            publish_source=config["networks"]["verify"][network.show_active()+"_verify"])
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
