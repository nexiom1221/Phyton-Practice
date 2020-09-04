import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에


# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enumy = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/enumy.png")
enumy_size = enumy.get_rect().size #이미지의 크기를 구해옴
enumy_width = enumy_size[0]
enumy_height = enumy_size[1]
enumy_x_pos = (screen_width / 2) - (enumy_width / 2)  # 화면 가로의 절반 크기 해당하는 곳에 위치
enumy_y_pos = (screen_height / 2)- (enumy_height /2) # 화면 세로 크기 가장 아래에

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(144) #게임화면의 초당 프레임 수 설정
    #print("fps :"+ str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height -character_height:
        character_y_pos = screen_height - character_height

    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    
    enumy_rect = enumy.get_rect()
    enumy_rect.left = enumy_x_pos
    enumy_rect.top = enumy_y_pos

    if character_rect.colliderect(enumy_rect):
        print("충돌")
        running = False

    #screen.fill((0, 0, 255)) 배경색 으로 채움
    screen.blit(background, (0 , 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enumy, (enumy_x_pos, enumy_y_pos))


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    #경과 시간을 1000으로 나누어 초 단위로 표시
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
# 잠시 대기

    pygame.display.update() # 게임화면을 다시 그리기
    
pygame.time.delay(2000) # 2 초 정도 대기
# pygame 종료
pygame.quit()
