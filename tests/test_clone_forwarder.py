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
