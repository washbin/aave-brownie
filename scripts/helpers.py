from brownie import accounts, network


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in {"mainnet-fork"}:
        return accounts[0]
    else:
        return accounts.load("meta")
