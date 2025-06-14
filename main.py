import pygame
import sys
from ai_agent import MLAgent
from data_collector import save_game_data
from random import choice

pygame.init()

# Ekran boyutu
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors - ML Edition")

# Fontlar ve renkler
font = pygame.font.SysFont(None, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Görselleri yükle
rock_img = pygame.image.load('assets/rock.png')
paper_img = pygame.image.load('assets/paper.png')
scissors_img = pygame.image.load('assets/scissors.png')
images = {'Rock': rock_img, 'Paper': paper_img, 'Scissors': scissors_img}

# Butonlar için pozisyonlar
button_rects = {
    'Rock': pygame.Rect(100, 450, 150, 100),
    'Paper': pygame.Rect(325, 450, 150, 100),
    'Scissors': pygame.Rect(550, 450, 150, 100),
}

# AI ajanı
agent = MLAgent()
last_moves = []

# Yardımcı fonksiyonlar
def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

def move_to_int(move):
    return {'Rock': 0, 'Paper': 1, 'Scissors': 2}.get(move, -1)

def determine_winner(player, ai):
    if player == ai:
        return "Draw"
    elif (player == 'Rock' and ai == 'Scissors') or \
         (player == 'Paper' and ai == 'Rock') or \
         (player == 'Scissors' and ai == 'Paper'):
        return "You Win!"
    else:
        return "AI Wins!"

# Ana döngü
clock = pygame.time.Clock()
result = ""
player_choice = None
ai_choice = None

while True:
    screen.fill(WHITE)
    draw_text("Choose your move:", 280, 400)

    # Butonları çiz
    for move, rect in button_rects.items():
        pygame.draw.rect(screen, (200, 200, 200), rect)
        draw_text(move, rect.x + 25, rect.y + 30)

    # Seçimler varsa görselleri çiz
    if player_choice:
        screen.blit(images[player_choice], (150, 100))
        draw_text("You", 200, 80)
    if ai_choice:
        screen.blit(images[ai_choice], (500, 100))
        draw_text("AI", 560, 80)
    if result:
        draw_text(result, 330, 300)

    # Olaylar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for move, rect in button_rects.items():
                if rect.collidepoint(event.pos):
                    player_choice = move
                    last_moves.append(move)
                    ai_choice = agent.predict_next_move(last_moves)
                    result = determine_winner(player_choice, ai_choice)

                    # Veri kaydet
                    if len(last_moves) >= 4:
                        seq = [move_to_int(m) for m in last_moves[-4:-1]]
                        target = move_to_int(last_moves[-1])
                        save_game_data(seq, target)

    pygame.display.flip()
    clock.tick(30)
