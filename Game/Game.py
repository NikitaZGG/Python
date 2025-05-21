import pygame



class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed =[0, 0]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]



pygame.init()
screen = pygame.display.set_mode([600, 400])

group_obj = pygame.sprite.Group()

sheep = Sprite(100, 100, 60, 'Sheep.png')
kust = Sprite(420, 300, 70, 'Kust.png')
kust.speed = [-6, 0]

group_obj.add(kust)

result = 0
next_boost = 5

font = pygame.font.Font(None, 32)


running = True
while running:

    if kust.rect.x < 0:
        kust.rect.x = 620
        result += 1

    if sheep.rect.y > 250 :
        sheep.speed = [0, 0]
    else:
        sheep.speed[1] += 1

    if result >= next_boost:
        kust.speed[0] -= 3
        next_boost += 5

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                sheep.speed[1] = -20

    if pygame.sprite.spritecollide(sheep, group_obj, False):
        running = False



    sheep.update()
    kust.update()

    screen.fill((64, 237, 255))
    screen.blit(font.render(f'Счёт: {result}', True,( 0, 0, 0), (64, 237, 255)), (40, 40))
    screen.blit(pygame.image.load('Ground.png'), [0, 260])
    screen.blit(sheep.image, sheep.rect)
    screen.blit(kust.image, kust.rect)
    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()
print(f'Счёт: {result}')