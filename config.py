"""
Configuration settings for the AI-Powered RPG Game Engine.
Contains all game constants and settings.
"""

# Display Settings
GRID_SIZE = 5
TILE_SIZE = 100
WINDOW_WIDTH = GRID_SIZE * TILE_SIZE
WINDOW_HEIGHT = GRID_SIZE * TILE_SIZE
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
GRID_COLOR = (200, 200, 200)
UI_COLOR = (100, 100, 100)

# Game Settings
PLAYER_START_POS = (2, 2)  # Center of 5x5 grid
PLAYER_START_HEALTH = 100
PLAYER_START_INVENTORY = {
    "health_potion": 2,
    "sword": 1
}

# AI Settings
LLM_MODEL = "mistral"  # Default Ollama model
COMMAND_RETRY_ATTEMPTS = 3  # Number of retries for failed LLM commands

# Performance Settings
ENABLE_GPU = True
DOUBLE_BUFFER = True
VSYNC = True

# Debug Settings
DEBUG_MODE = True
SHOW_FPS = True
LOG_COMMANDS = True
