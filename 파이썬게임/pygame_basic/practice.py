import pygame
############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Python Game") #게임 이름

# FPS
clock = pygame.time.Clock()
#############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)
background = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/background.png")

character = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.6

enumy = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/enumy.png")
enumy_size = character.get_rect().size
enumy_width = character_size[0]
enumy_height = character_size[1]
enumy_x_pos = (screen_width /2) - (enumy_width / 2)
enumy_y_pos = (enumy_height /2) - (enumy_height / 2)

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수 설정
    #print("fps :"+ str(clock.get_fps()))

    # 2. 이벤트 처리(키보드 ,마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)),True, (255,255,255))

    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()


pygame.time.delay(2000)

pygame.quit()