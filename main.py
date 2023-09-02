import pygame

pygame.init()

largeur = 800
hauteur = 600

blanc = (255, 255, 255)
noir = (0, 0, 0)

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Beetlife")

icone = pygame.image.load('Beet.ico')
pygame.display.set_icon(icone)

# Police
police = pygame.font.Font(None, 24)

# Zone de saisie
saisie = ""
saisie_x = 10
saisie_y = hauteur - 40

# Liste de messages
messages = []
max_messages = 10

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if saisie:
                    messages.append(saisie)
                    if len(messages) > max_messages:
                        messages.pop(0)
                    saisie = ""
            elif event.key == pygame.K_BACKSPACE:
                saisie = saisie[:-1]
            else:
                saisie += event.unicode
    
    # Effacer l'écran avec la couleur blanche
    fenetre.fill(blanc)
    
    # Afficher les messages
    y = 10
    for message in messages:
        texte_surface = police.render(message, True, noir)
        fenetre.blit(texte_surface, (10, y))
        y += texte_surface.get_height() + 5
    
    # Afficher la zone de saisie
    pygame.draw.rect(fenetre, noir, (saisie_x, saisie_y, largeur - 20, 30), 2)
    saisie_surface = police.render(saisie, True, noir)
    fenetre.blit(saisie_surface, (saisie_x + 5, saisie_y + 5))
    
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()