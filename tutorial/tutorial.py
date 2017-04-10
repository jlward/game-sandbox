import time
import sys
import pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
frame_length = 1.0 / 60


def main():
    screen = pygame.display.set_mode(size)
    frame_number = 0

    ball = pygame.image.load('tutorial/intro_ball.gif')
    ballrect = ball.get_rect()

    while 1:
        time.sleep(frame_length)
        frame_number += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
