#!/usr/bin/env python3
# thoth-cli-examples
# Copyright(C) 2021 Red Hat, Inc.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Example application to demonstrate thamos resolution process."""

import click
from pillow import ImageGrab
import pygame
from typing import Tuple
from typing import Optional


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


@click.command()
@click.option(
    "-g",
    "--grid-size",
    help="Choose a grid size between 10 and 100 for rows and columns",
    type=int,
    nargs=2,
    default=(20, 20),
)
@click.option("-m", "--max-iter", help="Choose a maximum number of iterations", type=int, default=30)
def cli(grid_size, max_iter):
    """Thoth cli-examples command line interface."""
    create_game(grid_size=grid_size, max_iter=max_iter)


def create_game(grid_size: Optional[Tuple[int, int]] = (20, 20), max_iter: Optional[int] = 30):
    """Create a game."""
    pygame.init()

    new_game = GameOfLife(grid_size=grid_size, max_iter=max_iter)
    size = (new_game.grid_size[0] * (new_game.grid_size[0] + 4), new_game.grid_size[1] * (new_game.grid_size[1] + 4))
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Game of Life")

    width = new_game.grid_size[0]
    height = new_game.grid_size[1]
    margin = 4
    done = False
    game_started = False
    print(" 🐍 " * 20)
    print("✨ Welcome to the Game of Life!\n")
    print("🎮 Fill squares to initialize the grid and press any keyboard button to start the Game of Life")
    print("❌ Press ^C in terminal to exit\n")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif not game_started and event.type == pygame.MOUSEBUTTONDOWN:
                column = position[0] // (width + margin)
                row = position[1] // (height + margin)
                new_game.grid[row][column] = 1
                new_game.first_individuals_coordinates.append([row, column])
                continue
            elif not game_started and event.type == pygame.KEYDOWN:
                game_started = True
                print("Starting game of life... 🖥️🕹️🐍")

        if game_started:
            new_game.next_generation()
            pygame.time.wait(350)

        position = pygame.mouse.get_pos()
        x = position[0]
        y = position[1]

        screen.fill(BLACK)

        for row in range(width):
            for column in range(height):
                if new_game.grid[row][column] == 1:
                    color = GREEN
                else:
                    color = WHITE
                pygame.draw.rect(
                    screen, color, [margin + (margin + width) * column, margin + (margin + height) * row, width, height]
                )

        pygame.display.flip()
    screenshot = ImageGrab.grab()
    screenshot.show()
    screenshot.save('my_game.png', 'PNG')
    pygame.quit()


class GameOfLife:
    """Class for game of life."""

    def __init__(self, grid_size=[10, 10], first_individuals_coordinates=[], max_iter=10):
        """Instance initialization."""
        self.first_individuals_coordinates = first_individuals_coordinates
        self.grid_size = grid_size
        self.grid = [[0]*self.grid_size[0] for _ in range(self.grid_size[1])]
        self.max_iter = max_iter

        for coordinates in self.first_individuals_coordinates:
            self.grid[coordinates[0]][coordinates[1]] = 1

    def next_generation(self):
        """Create the next generation of individuals."""
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        rows = len(self.grid)
        columns = len(self.grid[0])
        new_board = [[self.grid[row][col] for col in range(columns)] for row in range(rows)]

        for row in range(rows):
            for col in range(columns):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if (r < rows and r >= 0) and (c < columns and c >= 0) and (new_board[r][c] == 1):
                        live_neighbors += 1
                if new_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    self.grid[row][col] = 0
                if new_board[row][col] == 0 and live_neighbors == 3:
                    self.grid[row][col] = 1

        return self.grid


if __name__ == "__main__":
    cli()
