"""
Core game engine with GPU-accelerated rendering and game loop management.
"""

import pygame
import pygame.gfxdraw
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, FPS,
    WHITE, BLACK, GRID_COLOR, PLAYER_COLOR,
    TILE_SIZE, GRID_SIZE
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
        self.player_pos = (2, 2)  # Start in center

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
        # Clear screen
        self.window.fill(WHITE)

        # Draw grid
        self._draw_grid()

        # Draw player
        player_x = self.player_pos[0] * TILE_SIZE
        player_y = self.player_pos[1] * TILE_SIZE
        pygame.draw.rect(
            self.window,
            PLAYER_COLOR,
            pygame.Rect(player_x, player_y, TILE_SIZE, TILE_SIZE)
        )

        # Show FPS
        fps = int(self.clock.get_fps())
        pygame.display.set_caption(f"AI-Powered RPG (FPS: {fps})")

    def _draw_grid(self):
        """Draw the game grid."""
        # Draw vertical lines
        for x in range(0, WINDOW_WIDTH + 1, TILE_SIZE):
            pygame.draw.line(
                self.window,
                GRID_COLOR,
                (x, 0),
                (x, WINDOW_HEIGHT)
            )

        # Draw horizontal lines
        for y in range(0, WINDOW_HEIGHT + 1, TILE_SIZE):
            pygame.draw.line(
                self.window,
                GRID_COLOR,
                (0, y),
                (WINDOW_WIDTH, y)
            )

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
