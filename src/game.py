import time
from snake import Snake
from utils import clear_screen, random_food, load_high_score, save_high_score


# ----- Configuración -----
WIDTH = 12
HEIGHT = 8

EMPTY = "."
SNAKE_BODY = "O"
FOOD = "*"
SNAKE_HEAD = "@"

HIGH_SCORE_FILE = "highscore.txt"


def draw(snake: Snake, food: list[int], score: int, high_score: int) -> None:
    clear_screen()
    print(f"--- SNAKE (puntos: {score}) ---  (record: {high_score})")
    print("Controles: w/a/s/d + Enter | q = salir")
    print("Tip: evita girar 180° cuando tengas cuerpo.\n")

    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            pos = [x, y]
            if pos == snake.head():
                row += SNAKE_HEAD
            elif pos in snake.body:
                row += SNAKE_BODY
            elif pos == food:
                row += FOOD
            else:
                row += EMPTY
        print(row)


def read_input(snake: Snake) -> bool:
    """Devuelve False si el usuario quiere salir."""
    mov = input("\nMovimiento (w/a/s/d): ").strip().lower()

    if mov == "q":
        return False

    if mov == "w":
        snake.set_direction((0, -1))
    elif mov == "s":
        snake.set_direction((0, 1))
    elif mov == "a":
        snake.set_direction((-1, 0))
    elif mov == "d":
        snake.set_direction((1, 0))

    # Si escribió cualquier otra cosa, no pasa nada (se mantiene dirección).
    return True


def choose_speed() -> float:
    clear_screen()
    print("Elige dificultad (velocidad):")
    print("1) Fácil (lento)")
    print("2) Normal")
    print("3) Difícil (rápido)")
    choice = input("Opción (1/2/3): ").strip()

    if choice == "1":
        return 0.25
    if choice == "3":
        return 0.08
    return 0.15


def run_game() -> None:
    delay = choose_speed()
    high_score = load_high_score(HIGH_SCORE_FILE)

    # Estado inicial
    snake = Snake(body=[[WIDTH // 2, HEIGHT // 2]], direction=(1, 0))
    food = random_food(WIDTH, HEIGHT, snake.body)
    score = 0

    while True:
        draw(snake, food, score, high_score)

        if not read_input(snake):
            print("\nSaliendo... 👋")
            return

        next_head = snake.next_head()

        # 1) choque con paredes
        if next_head[0] < 0 or next_head[0] >= WIDTH or next_head[1] < 0 or next_head[1] >= HEIGHT:
            break

        # 2) choque con cuerpo
        if next_head in snake.body:
            break

        # 3) comer o no comer
        grow = next_head == food
        snake.move(grow=grow)

        if grow:
            score += 1
            food = random_food(WIDTH, HEIGHT, snake.body)

        time.sleep(delay)

    # Game over
    draw(snake, food, score, high_score)
    print("\nX_X Perdiste. Choque detectado.")
    print("Puntos:", score)

    if score > high_score:
        print("🎉 Nuevo récord!")
        save_high_score(HIGH_SCORE_FILE, score)

    again = input("\n¿Jugar otra vez? (s/n): ").strip().lower()
    if again == "s":
        run_game()


if __name__ == "__main__":
    run_game()
