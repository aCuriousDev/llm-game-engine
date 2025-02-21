"""
Game Agent: The main AI orchestrator that manages all other agents.
"""

from ollama import Client
from typing import Dict, Any, Tuple
from queue import Queue

from config import LLM_MODEL, COMMAND_RETRY_ATTEMPTS
from .movement_agent import MovementAgent


class GameAgent:
    """
    Main AI orchestrator that:
    1. Interprets user commands
    2. Routes commands to appropriate sub-agents
    3. Manages game state
    4. Coordinates agent interactions
    """

    def __init__(self):
        """Initialize the game agent and its sub-agents."""
        # Initialize Ollama client
        self.client = Client()

        # Initialize all sub-agents
        self.movement_agent = MovementAgent()

        # Command type mapping
        self.command_types = {
            "move": self._handle_movement,
            "attack": self._handle_combat,
            "inventory": self._handle_inventory,
            "talk": self._handle_dialogue
        }

        # Initialize command queue
        self.command_queue = Queue()

    def process_command(self, command_text: str) -> Tuple[bool, str]:
        """
        Process a user command by:
        1. Interpreting the command type
        2. Routing to appropriate agent
        3. Returning the result
        """
        print(f"\nProcessing command: '{command_text}'")
        command_type = self._interpret_command_type(command_text)
        print(f"LLM interpreted command type as: '{command_type}'")

        if command_type in self.command_types:
            handler = self.command_types[command_type]
            success, message = handler(command_text)
            print(f"Handler result: success={success}, message='{message}'")
            return success, message

        return False, "Command not recognized"

    def _interpret_command_type(self, command_text: str) -> str:
        """Use Ollama to classify the command type."""
        prompt = f"""
        Classify this command by responding with EXACTLY ONE WORD from these options:
        - move (for movement commands like "go left", "walk forward")
        - attack (for combat commands like "attack enemy", "cast spell")
        - inventory (for item commands like "use potion", "check inventory")
        - talk (for NPC interaction like "talk to merchant")
        - invalid (if it doesn't fit any category)

        DO NOT include any explanation or additional text. Just return the single word category.
        
        Command: "{command_text}"
        """

        print(f"\nSending to LLM for classification...")

        for attempt in range(COMMAND_RETRY_ATTEMPTS):
            try:
                response = self.client.chat(
                    model=LLM_MODEL,
                    messages=[{"role": "user", "content": prompt}]
                )
                command_type = response['message']['content'].strip().lower()
                print(
                    f"LLM response (attempt {attempt + 1}): '{command_type}'")

                # Extract just the category word if it's in a sentence
                for valid_type in list(self.command_types.keys()) + ["invalid"]:
                    if valid_type in command_type:
                        command_type = valid_type
                        break

                if command_type in self.command_types or command_type == "invalid":
                    return command_type

            except Exception as e:
                print(
                    f"Error in LLM interpretation (attempt {attempt + 1}): {e}")

        return "invalid"

    def _handle_movement(self, command_text: str) -> Tuple[bool, str]:
        """Route movement commands to MovementAgent."""
        print("\nRouting to MovementAgent...")
        return self.movement_agent.handle_movement(command_text)

    def _handle_combat(self, command_text: str) -> Tuple[bool, str]:
        """Placeholder for combat system."""
        return False, "Combat system not implemented yet"

    def _handle_inventory(self, command_text: str) -> Tuple[bool, str]:
        """Placeholder for inventory system."""
        return False, "Inventory system not implemented yet"

    def _handle_dialogue(self, command_text: str) -> Tuple[bool, str]:
        """Placeholder for NPC dialogue system."""
        return False, "Dialogue system not implemented yet"

    def get_game_state(self) -> Dict[str, Any]:
        """
        Get the current game state from all agents.
        This will be used by the game engine for rendering.
        """
        return {
            "player_pos": self.movement_agent.position,
            # Add more state information as we implement other agents
        }

    def update(self) -> None:
        """
        Update all agents' states.
        Called every frame by the game engine.
        """
        # Process any queued commands
        while not self.command_queue.empty():
            command = self.command_queue.get()
            self.process_command(command)

        # Update agent states
        # (Will add more as we implement other agents)
