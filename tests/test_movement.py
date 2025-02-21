"""
Tests for the movement agent functionality.
"""

import pytest
from agents.movement_agent import MovementAgent


def test_movement_agent_initialization():
    """Test that the movement agent initializes correctly."""
    agent = MovementAgent()
    assert agent.position == (2, 2)  # Starting position


def test_valid_movement():
    """Test that valid movements work correctly."""
    agent = MovementAgent()

    # Test moving right
    success, message = agent.handle_movement("go right")
    assert success
    assert agent.position == (3, 2)

    # Test moving down
    success, message = agent.handle_movement("move down")
    assert success
    assert agent.position == (3, 3)


def test_invalid_movement():
    """Test that invalid movements are handled correctly."""
    agent = MovementAgent()

    # Move to edge
    agent.handle_movement("go right")
    agent.handle_movement("go right")

    # Try to move beyond edge
    success, message = agent.handle_movement("go right")
    assert not success
    assert "Cannot move there" in message


def test_nonsense_command():
    """Test that nonsense commands are rejected."""
    agent = MovementAgent()
    success, message = agent.handle_movement("do a backflip")
    assert not success
    assert "Invalid" in message


if __name__ == "__main__":
    pytest.main([__file__])
