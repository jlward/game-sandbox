import time
import sys
import pygame
from contextlib import contextmanager
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
frames_per_second = 60.0
frame_length = 1.0 / frames_per_second


def get_frame_counter_text(frame_number):
    return '{frame_number}: ({seconds} seconds)'.format(
        frame_number=frame_number,
        seconds=round(frame_number / frames_per_second, 2),
    )


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(func, e)
    return wrapper


class Game(object):
    def __init__(self):
        self.frame_number = 1
        self.screen = pygame.display.set_mode(size)
        self.font = pygame.font.Font(None, 12)
        self.ball = pygame.image.load('tutorial/intro_ball.gif')
        self.ballrect = self.ball.get_rect()
        self.blit_objects = [
            self.process_ball,
            self.process_frame_text,
        ]

    def process_ball(self):
        self.ballrect = self.ballrect.move(speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            speed[0] = -speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            speed[1] = -speed[1]
        self.screen.blit(self.ball, self.ballrect)

    def process_frame_text(self):
        frame_text = self.font.render(
                get_frame_counter_text(self.frame_number), 1, white)
        self.screen.blit(frame_text, (10, 10))

    @contextmanager
    def increment_frame(self):
        try:
            self.frame_number += 1
            yield
        finally:
            time.sleep(frame_length)

    @exception_handler
    def _process_frame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.screen.fill(black)
        for func in self.blit_objects:
            func()
        pygame.display.flip()

    def process_frame(self):
        with self.increment_frame():
            self._process_frame()

    def run(self):
        while 1:
            self.process_frame()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
