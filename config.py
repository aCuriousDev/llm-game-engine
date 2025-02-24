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

# Modern Color Palette (Using a dark theme with vibrant accents)
COLORS = {
    # Base colors
    "background": (40, 44, 52),      # Dark background
    "grid_lines": (75, 85, 99),      # Subtle grid lines
    "text": (171, 178, 191),         # Easy to read text

    # Player and UI colors
    "player": {
        "primary": (97, 175, 239),   # Bright blue for player
        "secondary": (86, 153, 209),  # Darker blue for effects
        "outline": (152, 195, 241)   # Light blue outline
    },

    # UI Elements
    "ui": {
        "primary": (152, 195, 121),  # Green for positive actions
        "secondary": (229, 192, 123),  # Yellow for warnings
        "accent": (224, 108, 117),    # Red for critical info
        "background": (33, 37, 43)    # Darker than main background
    },

    # Status colors
    "status": {
        "success": (152, 195, 121),  # Green
        "warning": (229, 192, 123),  # Yellow
        "error": (224, 108, 117),    # Red
        "info": (97, 175, 239)       # Blue
    }
}

# Dynamic Game Settings


def calculate_center_pos(grid_size: int = GRID_SIZE) -> tuple[int, int]:
    """Calculate the center position of the grid."""
    return (grid_size // 2, grid_size // 2)


def calculate_spawn_points(grid_size: int = GRID_SIZE) -> dict[str, tuple[int, int]]:
    """Calculate various spawn points on the grid."""
    return {
        "center": calculate_center_pos(grid_size),
        "top": (grid_size // 2, 0),
        "bottom": (grid_size // 2, grid_size - 1),
        "left": (0, grid_size // 2),
        "right": (grid_size - 1, grid_size // 2),
        "top_left": (0, 0),
        "top_right": (grid_size - 1, 0),
        "bottom_left": (0, grid_size - 1),
        "bottom_right": (grid_size - 1, grid_size - 1)
    }


# Game Settings
SPAWN_POINTS = calculate_spawn_points()
PLAYER_START_POS = SPAWN_POINTS["center"]  # Start in center
PLAYER_START_HEALTH = 100
PLAYER_START_INVENTORY = {
    "health_potion": 2,
    "sword": 1
}

# Visual Settings
TILE_PADDING = 5  # Pixels of padding between tiles
PLAYER_OUTLINE_WIDTH = 2  # Width of player outline in pixels
GRID_LINE_WIDTH = 1  # Width of grid lines

# Animation Settings
MOVEMENT_ANIMATION_SPEED = 0.2  # Seconds per tile movement
EFFECT_FADE_SPEED = 0.5  # Seconds for effects to fade

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
