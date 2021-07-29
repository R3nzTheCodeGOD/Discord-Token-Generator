from time import sleep
from colorama import init
from threading import Thread

from Generator import Generator


if __name__ == "__main__":
    init()
    generator = Generator(userid="123123123123123123")
    threads = 5

    [(Thread(target=generator.start, daemon=True).start(), sleep(0.3)) for _ in range(threads - 1)]

    generator.start()