from brownie import Forwarder, accounts, exceptions
import pytest


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    # Assert
    assert account == forwarder.destination()


def test_only_owner_can_withdraw():
    # Arrange
    account = accounts[0]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    bad_actor = accounts.add()
    # Assert
    with pytest.raises(exceptions.VirtualMachineError):
        forwarder.withdraw({"from": bad_actor})


def test_only_owner_can_changeDestination():
    # Arrange
    account = accounts[0]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    bad_actor = accounts.add()
    # Assert
    with pytest.raises(exceptions.VirtualMachineError):
        forwarder.changeDestination(bad_actor, {"from": bad_actor})


def test_cannot_call_init_when_forwarder_created():
    # Arrange
    account = accounts[0]
    bad_actor = accounts.add()
    # Act
    forwarder = Forwarder.deploy({"from": account})
    txn = forwarder.init(bad_actor, {"from": bad_actor})
    # Assert
    assert account == forwarder.destination()


def test_recieve():
    # Arrange
    account = accounts[0]
    sender = accounts[1]
    # Act
    forwarder = Forwarder.deploy({"from": account})
    txn = sender.transfer(forwarder, "1 ether")
    txn.wait(1)
    # Assert
    assert account.balance() == 1001000000000000000000
