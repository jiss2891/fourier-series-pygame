import math
import pygame as pg


def init():
    """Initialization calls"""
    pg.init()
    screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)
    return screen, pg.time.Clock()


def coords(x, y):
    """Used to translate the coordinates origin"""
    return 300 + x, 300 + y


def mainloop(screen: pg.Surface, main_clock: pg.time.Clock):
    background_color = "black"
    run = True

    time = 0  # angle for polar-to-cartesian conversion
    r = 100
    wave = []
    circles = 3
    circle_color = (100, 100, 100)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    circles += 1
                elif event.key == pg.K_DOWN:
                    circles -= 1

        screen.fill(background_color)

        x, y = 0, 0
        for i in range(0, circles):
            previous_x = x
            previous_y = y
            n = i * 2 + 1
            radius = r * (4.0 / (n * math.pi))
            x += radius * math.cos(n * time)
            y += radius * math.sin(n * time)

            pg.draw.line(screen, "white", coords(previous_x, previous_y), coords(x, y))
            pg.draw.circle(screen, circle_color,
                           coords(previous_x, previous_y), radius=radius, width=1)

        wave.insert(0, y)
        if len(wave) > 2:
            pg.draw.aalines(screen, pg.Color("white"), False,
                            [coords(200 + i, wave[i]) for i in range(len(wave))], 1 )

        pg.draw.line(screen, pg.Color("white"), coords(x, y), coords(200, wave[0]), 1)

        time -= 0.02
        pg.display.flip()
        main_clock.tick(60)


def main():
    mainloop(*init())
    pg.quit()


if __name__ == "__main__":
    main()
