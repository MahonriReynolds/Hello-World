import time
import sys
import random

def animate_printout(message: str, spinner: str) -> None:    
    for idx in range(len(message)):
        for _ in range(random.randint(0, 2 * len(spinner))):
            sys.stdout.write(f'\r{message[:idx]}{spinner[_ % len(spinner)]}')
            sys.stdout.flush()
            time.sleep(0.07)
    sys.stdout.write(f'\r{message}')
    sys.stdout.flush()
    time.sleep(0.1)
    print()


animate_printout('Hello World', '⣾⣷⣯⣟⡿⢿⣻⣽')
animate_printout('Hello World', '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏')
animate_printout('Hello World', '-\\|/')
animate_printout('Hello World', '⠂-–—–-')
animate_printout('Hello World', '┤┘┴└├┌┬┐')
animate_printout('Hello World', '✶✸✹✺✹✷')
animate_printout('Hello World', '☱☲☴')
animate_printout('Hello World', '▏▎▍▌▋▊▉')
animate_printout('Hello World', '▏▎▍▌▋▊▉▊▋▌▍▎')






