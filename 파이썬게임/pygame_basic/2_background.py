import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/LG/Desktop/9.4 파이썬/파이썬게임/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #screen.fill((0, 0, 255)) 배경색 으로 채움
    screen.blit(background, (0 , 0))

    pygame.display.update() # 게임화면을 다시 그리기
# pygame 종료
pygame.quit()
