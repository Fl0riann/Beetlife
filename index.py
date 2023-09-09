import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Chat de Réseau Social")

# Chargement de l'icône
icone = pygame.image.load("Beet.ico")
pygame.display.set_icon(icone)

# Police
police = pygame.font.Font(None, 24)

# Bouton
bouton = pygame.Rect(10, hauteur - 40, 100, 30)
bouton_clic = False

# Texte de la zone de saisie
saisie = ""

# Liste de messages
messages = []
max_messages = 10

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton.collidepoint(event.pos):
                messages.append("Coucou")
                if len(messages) > max_messages:
                    messages.pop(0)
                saisie = ""
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
    
    # Afficher le bouton
    pygame.draw.rect(fenetre, noir, bouton, 2)
    texte_bouton = police.render("Envoyer", True, noir)
    fenetre.blit(texte_bouton, (bouton.x + 5, bouton.y + 5))
    
    # Afficher la zone de saisie
    pygame.draw.rect(fenetre, noir, (bouton.right + 10, bouton.top, largeur - bouton.width - 30, 30), 2)
    saisie_surface = police.render(saisie, True, noir)
    fenetre.blit(saisie_surface, (bouton.right + 15, bouton.y + 5))
    
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
