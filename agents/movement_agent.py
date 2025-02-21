"""
Movement Agent: Handles player movement with AI command interpretation.
"""

from ollama import Client
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
        self.client = Client()  # Initialize Ollama client

    def handle_movement(self, command_text: str) -> tuple[bool, str]:
        """
        Process a movement command using AI interpretation.
        Returns: (success, message)
        """
        print(f"\nMovementAgent processing: '{command_text}'")
        direction = self._interpret_command(command_text)
        print(f"Interpreted direction: '{direction}'")

        if direction in self.valid_directions:
            success = self._move(direction)
            result_msg = f"Moved {direction}" if success else "Cannot move there"
            print(f"Movement result: {result_msg}")
            return success, result_msg
        return False, "Invalid movement command"

    def _interpret_command(self, command_text: str) -> str:
        """Use Ollama to interpret movement commands."""
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

        print("\nSending movement command to LLM...")
        print(f"Valid directions: {list(self.valid_directions.keys())}")

        for attempt in range(COMMAND_RETRY_ATTEMPTS):
            try:
                response = self.client.chat(
                    model=LLM_MODEL,
                    messages=[{
                        'role': 'user',
                        'content': prompt
                    }]
                )
                direction = response['message']['content'].strip().lower()
                print(
                    f"LLM movement response (attempt {attempt + 1}): '{direction}'")

                # Extract just the direction word if it's in a sentence
                for valid_dir in list(self.valid_directions.keys()) + ["invalid"]:
                    if valid_dir in direction:
                        direction = valid_dir
                        break

                print(f"Processed direction: '{direction}'")
                if direction in self.valid_directions or direction == "invalid":
                    return direction

            except Exception as e:
                print(
                    f"Error in movement interpretation (attempt {attempt + 1}): {e}")

        print("No valid direction found after all attempts")
        return "invalid"

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
