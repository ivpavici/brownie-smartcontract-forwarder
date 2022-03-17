from brownie import ForwarderFactory, Forwarder, accounts
import pytest


def test_cloneForwarder():
    # Arrange
    account = accounts[0]
    payer = accounts[1]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    forwarderFactory = ForwarderFactory.deploy({"from": account})
    # Assert
    assert forwarderFactory.cloneForwarder(forwarder, 1)


@pytest.fixture(scope="module")
def test_recieve_clone_forward_to_account():
    # Arrange
    account = accounts[0]
    sender = accounts[1]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    forwarderFactory = ForwarderFactory.deploy({"from": account})
    clone = forwarderFactory.cloneForwarder(forwarder, 1)
    clone.wait(1)
    clonedAddress = clone.events[0]["clonedAdress"]
    txn = sender.transfer(clonedAddress, "1 ether")
    txn.wait(1)
    # Assert
    assert account.balance() == 1001000000000000000000
