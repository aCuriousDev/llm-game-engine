"""
Movement Agent: Handles player movement with AI command interpretation.
"""

from ollama import Client
from typing import Tuple, Dict, List, Optional
from config import (
    GRID_SIZE,
    PLAYER_START_POS,
    COMMAND_RETRY_ATTEMPTS,
    LLM_MODEL
)


class MovementAgent:
    def __init__(self):
        """Initialize the movement agent."""
        self.x, self.y = PLAYER_START_POS
        self.valid_directions = {
            "left": (-1, 0),
            "right": (1, 0),
            "up": (0, -1),
            "down": (0, 1)
        }

        # Define named locations
        self.locations = {
            "center": (GRID_SIZE // 2, GRID_SIZE // 2),
            "top": (GRID_SIZE // 2, 0),
            "bottom": (GRID_SIZE // 2, GRID_SIZE - 1),
            "left": (0, GRID_SIZE // 2),
            "right": (GRID_SIZE - 1, GRID_SIZE // 2),
            "top_left": (0, 0),
            "top_right": (GRID_SIZE - 1, 0),
            "bottom_left": (0, GRID_SIZE - 1),
            "bottom_right": (GRID_SIZE - 1, GRID_SIZE - 1)
        }

        self.client = Client()  # Initialize Ollama client

    def handle_movement(self, command_text: str) -> tuple[bool, str]:
        """
        Process a movement command using AI interpretation.
        Returns: (success, message)
        """
        print(f"\nMovementAgent processing: '{command_text}'")

        # First try to interpret as a location command
        location = self._interpret_location_command(command_text)
        if location != "invalid":
            return self._move_towards_location(location)

        # If not a location command, try as a direction command
        direction = self._interpret_direction_command(command_text)
        if direction in self.valid_directions:
            success = self._move(direction)
            result_msg = f"Moved {direction}" if success else "Cannot move there"
            print(f"Movement result: {result_msg}")
            return success, result_msg

        return False, "Invalid movement command"

    def _interpret_location_command(self, command_text: str) -> str:
        """Use Ollama to interpret location-based commands."""
        prompt = f"""
        If this is a location-based command, respond with EXACTLY ONE WORD from: {', '.join(self.locations.keys())}.
        If it's not a location command, respond with 'invalid'.
        DO NOT include any explanation or additional text.
        
        Examples:
        Command: "go to the center" -> center
        Command: "move to top left corner" -> top_left
        Command: "head to the bottom" -> bottom
        Command: "walk left" -> invalid
        
        Command: "{command_text}"
        """

        print("\nChecking for location command...")
        print(f"Valid locations: {list(self.locations.keys())}")

        for attempt in range(COMMAND_RETRY_ATTEMPTS):
            try:
                response = self.client.chat(
                    model=LLM_MODEL,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                location = response['message']['content'].strip().lower()
                print(
                    f"LLM location response (attempt {attempt + 1}): '{location}'")

                if location in self.locations or location == "invalid":
                    return location

            except Exception as e:
                print(
                    f"Error in location interpretation (attempt {attempt + 1}): {e}")

        return "invalid"

    def _interpret_direction_command(self, command_text: str) -> str:
        """Use Ollama to interpret directional movement commands."""
        prompt = f"""
        Convert this movement command by responding with EXACTLY ONE WORD from: 'left', 'right', 'up', 'down', or 'invalid'.
        DO NOT include any explanation or additional text. Just return the single direction word.

        Examples:
        Command: "go left" -> left
        Command: "move forward" -> up
        Command: "step back" -> down
        Command: "walk right" -> right
        Command: "jump" -> invalid

        Command: "{command_text}"
        """

        print("\nChecking for direction command...")
        print(f"Valid directions: {list(self.valid_directions.keys())}")

        for attempt in range(COMMAND_RETRY_ATTEMPTS):
            try:
                response = self.client.chat(
                    model=LLM_MODEL,
                    messages=[{'role': 'user', 'content': prompt}]
                )
                direction = response['message']['content'].strip().lower()
                print(
                    f"LLM direction response (attempt {attempt + 1}): '{direction}'")

                if direction in self.valid_directions or direction == "invalid":
                    return direction

            except Exception as e:
                print(
                    f"Error in direction interpretation (attempt {attempt + 1}): {e}")

        return "invalid"

    def _get_next_step_direction(self, current_pos: Tuple[int, int], target_pos: Tuple[int, int]) -> Optional[str]:
        """
        Calculate the next step direction towards the target position.
        Returns None if we're already at the target.
        """
        curr_x, curr_y = current_pos
        target_x, target_y = target_pos

        # Already at target
        if (curr_x, curr_y) == (target_x, target_y):
            return None

        # Prioritize horizontal movement
        if curr_x < target_x:
            return "right"
        elif curr_x > target_x:
            return "left"
        # Then vertical movement
        elif curr_y < target_y:
            return "down"
        elif curr_y > target_y:
            return "up"

        return None

    def _move_towards_location(self, location: str) -> Tuple[bool, str]:
        """Move one step towards the target location."""
        if location not in self.locations:
            return False, "Invalid location"

        target_x, target_y = self.locations[location]
        print(
            f"Target location '{location}' is at position ({target_x}, {target_y})")
        print(f"Current position: ({self.x}, {self.y})")

        # Get the next step direction
        next_direction = self._get_next_step_direction(
            (self.x, self.y), (target_x, target_y))

        # If we're already at the target
        if next_direction is None:
            return True, f"Already at {location}"

        # Try to move one step towards the target
        success = self._move(next_direction)
        if success:
            # Check if we've reached the target
            if (self.x, self.y) == (target_x, target_y):
                return True, f"Reached {location}"
            else:
                return True, f"Moving towards {location}, took one step {next_direction}"
        else:
            return False, f"Cannot move {next_direction} towards {location}"

    def _move(self, direction: str) -> bool:
        """
        Attempt to move in the specified direction.
        Returns: True if movement was successful, False otherwise.
        """
        print(f"\nAttempting to move: '{direction}'")

        if direction not in self.valid_directions:
            print(f"Invalid direction: '{direction}'")
            return False

        dx, dy = self.valid_directions[direction]
        new_x = self.x + dx
        new_y = self.y + dy

        print(f"Current position: ({self.x}, {self.y})")
        print(f"Attempting to move to: ({new_x}, {new_y})")
        print(f"Grid boundaries: 0 to {GRID_SIZE-1}")

        # Check grid boundaries
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            print(f"Moving from ({self.x}, {self.y}) to ({new_x}, {new_y})")
            self.x, self.y = new_x, new_y
            return True

        print(
            f"Movement blocked: Position ({new_x}, {new_y}) is out of bounds")
        return False

    @property
    def position(self) -> tuple[int, int]:
        """Get current position."""
        return self.x, self.y
