from brownie import ForwarderFactory, Forwarder, accounts
import pytest


def test_cloneForwarder():
    # Arrange
    account = accounts[0]
    payer = accounts[1]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    forwarderFactory = ForwarderFactory.deploy({"from": account})
    txn = forwarderFactory.cloneForwarder(forwarder, 1)
    # Assert
    assert txn  # check how to exactly verify
