"""
Game Agent: The main AI orchestrator that manages all other agents.
"""

from ollama import Client
from typing import Dict, Any, Tuple, List
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

        # Command type mapping with examples
        self.command_types = {
            "move": {
                "handler": self._handle_movement,
                "examples": [
                    "go left",
                    "move to the center",
                    "walk forward",
                    "head to the top right",
                    "move to bottom"
                ]
            },
            "attack": {
                "handler": self._handle_combat,
                "examples": [
                    "attack enemy",
                    "cast fireball",
                    "shoot arrow"
                ]
            },
            "inventory": {
                "handler": self._handle_inventory,
                "examples": [
                    "check inventory",
                    "use potion",
                    "equip sword"
                ]
            },
            "talk": {
                "handler": self._handle_dialogue,
                "examples": [
                    "talk to merchant",
                    "speak with guard",
                    "ask about quest"
                ]
            }
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
            handler = self.command_types[command_type]["handler"]
            success, message = handler(command_text)
            print(f"Handler result: success={success}, message='{message}'")
            return success, message

        return False, "Command not recognized"

    def _interpret_command_type(self, command_text: str) -> str:
        """Use Ollama to classify the command type."""
        # Build examples string from command_types
        example_lines = []
        for cmd_type, info in self.command_types.items():
            example_lines.append(f"Category '{cmd_type}':")
            for example in info["examples"]:
                example_lines.append(f"- {example}")
        examples = "\n".join(example_lines)

        prompt = f"""
        Classify this command into one of these categories based on these examples:

        {examples}

        Respond with EXACTLY ONE WORD (the category name) from: {', '.join(self.command_types.keys())}.
        If the command doesn't match any category, respond with 'invalid'.
        DO NOT include any explanation or additional text.
        
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
