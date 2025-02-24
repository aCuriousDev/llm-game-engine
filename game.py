"""
Core game engine with GPU-accelerated rendering and game loop management.
"""

import pygame
import pygame.gfxdraw
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    COLORS, GRID_SIZE, TILE_SIZE,
    TILE_PADDING, PLAYER_OUTLINE_WIDTH,
    GRID_LINE_WIDTH, SPAWN_POINTS
)


class GameEngine:
    def __init__(self):
        """Initialize the game engine."""
        pygame.init()

        # Initialize display
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AI-Powered RPG")

        # Initialize clock for FPS control
        self.clock = pygame.time.Clock()
        self.running = False

        # Initialize game state
        self.player_pos = SPAWN_POINTS["center"]  # Start in center

        # Initialize fonts
        self.font = pygame.font.Font(None, 36)  # Default font for UI

    def start(self):
        """Start the game loop."""
        self.running = True
        while self.running:
            self._handle_events()
            self._update()
            self._render()

            # Cap the framerate
            self.clock.tick(FPS)
            pygame.display.flip()

    def _handle_events(self):
        """Process game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        """Update game state."""
        pass  # Will be implemented with game logic

    def _render(self):
        """Render the game state."""
        # Clear screen with background color
        self.window.fill(COLORS["background"])

        # Draw grid
        self._draw_grid()

        # Draw player with modern styling
        self._draw_player()

        # Draw UI elements
        self._draw_ui()

    def _draw_grid(self):
        """Draw the game grid with modern styling."""
        # Draw grid lines
        for x in range(0, WINDOW_WIDTH + 1, TILE_SIZE):
            pygame.draw.line(
                self.window,
                COLORS["grid_lines"],
                (x, 0),
                (x, WINDOW_HEIGHT),
                GRID_LINE_WIDTH
            )

        for y in range(0, WINDOW_HEIGHT + 1, TILE_SIZE):
            pygame.draw.line(
                self.window,
                COLORS["grid_lines"],
                (0, y),
                (WINDOW_WIDTH, y),
                GRID_LINE_WIDTH
            )

    def _draw_player(self):
        """Draw the player with modern styling and effects."""
        # Calculate player rectangle with padding
        player_x = self.player_pos[0] * TILE_SIZE + TILE_PADDING
        player_y = self.player_pos[1] * TILE_SIZE + TILE_PADDING
        player_width = TILE_SIZE - (2 * TILE_PADDING)
        player_height = TILE_SIZE - (2 * TILE_PADDING)

        # Draw player outline (slightly larger than the player)
        outline_rect = pygame.Rect(
            player_x - PLAYER_OUTLINE_WIDTH,
            player_y - PLAYER_OUTLINE_WIDTH,
            player_width + (2 * PLAYER_OUTLINE_WIDTH),
            player_height + (2 * PLAYER_OUTLINE_WIDTH)
        )
        pygame.draw.rect(
            self.window,
            COLORS["player"]["outline"],
            outline_rect,
            border_radius=8
        )

        # Draw player fill
        player_rect = pygame.Rect(
            player_x,
            player_y,
            player_width,
            player_height
        )
        pygame.draw.rect(
            self.window,
            COLORS["player"]["primary"],
            player_rect,
            border_radius=6
        )

    def _draw_ui(self):
        """Draw UI elements."""
        # Show FPS counter with modern styling
        fps = int(self.clock.get_fps())
        fps_text = self.font.render(f"FPS: {fps}", True, COLORS["text"])
        fps_rect = fps_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))

        # Draw FPS counter background
        padding = 5
        bg_rect = fps_rect.inflate(padding * 2, padding * 2)
        pygame.draw.rect(
            self.window,
            COLORS["ui"]["background"],
            bg_rect,
            border_radius=4
        )

        # Draw FPS text
        self.window.blit(fps_text, fps_rect)

        # Update window caption
        pygame.display.set_caption(f"AI-Powered RPG (FPS: {fps})")

    def stop(self):
        """Clean up and stop the game engine."""
        self.running = False
        pygame.quit()


if __name__ == "__main__":
    # Quick test of the game engine
    engine = GameEngine()
    try:
        engine.start()
    except KeyboardInterrupt:
        engine.stop()
