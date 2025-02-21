"""
Main entry point for the AI-Powered RPG Game.
Integrates the game engine with AI agents.
"""

import threading
from queue import Queue

from game import GameEngine
from agents.game_agent import GameAgent


def start_command_listener(game_agent: GameAgent, game_engine: GameEngine):
    """
    Listen for user commands in a separate thread.
    This allows for non-blocking command input while the game runs.
    """
    print("Game started! Enter commands (or 'exit' to quit):")
    print("Examples:")
    print("- Movement: 'go left', 'move forward'")
    print("- Combat: 'attack enemy', 'cast fireball'")
    print("- Inventory: 'use potion', 'check inventory'")
    print("- Dialogue: 'talk to merchant'")

    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                game_engine.running = False
                break

            if command:
                success, message = game_agent.process_command(command)
                print(f"Result: {message}")

                # Update game engine's player position
                game_engine.player_pos = game_agent.get_game_state()[
                    "player_pos"]

        except KeyboardInterrupt:
            game_engine.running = False
            break
        except Exception as e:
            print(f"Error processing command: {e}")


def main():
    """
    Main game loop that:
    1. Initializes the game engine and AI agents
    2. Starts the command listener in a separate thread
    3. Runs the game loop
    """
    try:
        # Initialize components
        game_agent = GameAgent()
        game_engine = GameEngine()

        # Start command listener in a separate thread
        command_thread = threading.Thread(
            target=start_command_listener,
            args=(game_agent, game_engine),
            daemon=True
        )
        command_thread.start()

        # Start game loop
        game_engine.start()

    except KeyboardInterrupt:
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"Error running game: {e}")
    finally:
        # Cleanup
        game_engine.stop()


if __name__ == "__main__":
    main()
