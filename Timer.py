#AI-MINOR-JULY
#mailme8satyam@gmail.com
#Satyam Singh

#pygame must be installed

'''
Python Minor Project
Create A Countdown Timer Using Python
Features To Include
Reset / Stop
Pause / Resume
'''


import pygame
from sys import exit

def display():
    base_screen.blit(home_surface, (0,0))

    #Pause/Resume Button
    pygame.draw.rect(base_screen, "Green", start_rect)
    pygame.draw.rect(base_screen, "Blue", start_rect, 1)
    base_screen.blit(start_surf, start_rect)

    #Reset/Stop Button
    pygame.draw.rect(base_screen, "Green", stop_rect)
    pygame.draw.rect(base_screen, "Blue", stop_rect, 1)
    base_screen.blit(stop_surf, stop_rect)
    
    #Countdown
    pygame.draw.rect(base_screen, "Light Blue", text_rect)
    pygame.draw.rect(base_screen, "Dark Blue", text_rect, 2)
    base_screen.blit(text_surf, text_rect)

    #Buttons to increase or decrease timer by hours, mins and secs
    pygame.draw.rect(base_screen, "Cyan", h_rect_inc)
    base_screen.blit(h_surf_inc, h_rect_inc)
    pygame.draw.rect(base_screen, "Cyan", h_rect_dec)
    base_screen.blit(h_surf_dec, h_rect_dec)
    pygame.draw.rect(base_screen, "Cyan", m_rect_inc)
    base_screen.blit(m_surf_inc, m_rect_inc)
    pygame.draw.rect(base_screen, "Cyan", m_rect_dec)
    base_screen.blit(m_surf_dec, m_rect_dec)
    pygame.draw.rect(base_screen, "Cyan", s_rect_inc)
    base_screen.blit(s_surf_inc, s_rect_inc)
    pygame.draw.rect(base_screen, "Cyan", s_rect_dec)
    base_screen.blit(s_surf_dec, s_rect_dec)

pygame.init()

base_screen = pygame.display.set_mode((800, 400))
base_screen_rect = base_screen.get_rect(topleft = (0,0))
pygame.display.set_caption("Countdown Timer")
clock = pygame.time.Clock()

my_font = pygame.font.SysFont("Arial, Times New Roman", 50)          #Get a new font
arrow = pygame.font.SysFont("Arial, Times New Roman", 25)
comp_font = pygame.font.SysFont("Times New Roman, Arial", 50)

home_surface = pygame.Surface((800, 400))
home_surface.fill((127,248,96))

text_font = pygame.font.SysFont("Arial, Times New Roman", 80)
text_surf = text_font.render("00 h : 00 m : 00 s", True, "Black")
text_rect = text_surf.get_rect(center = (400, 125))

h_surf_inc = arrow.render("↑ +1 h", True, "Dark Blue")
h_rect_inc = h_surf_inc.get_rect(midbottom = (text_rect.left + text_rect.width / 6, text_rect.top))
h_surf_dec = arrow.render("↓ -1 h", True, "Dark Blue")
h_rect_dec = h_surf_inc.get_rect(midtop = (text_rect.left + text_rect.width / 6, text_rect.bottom))

m_surf_inc = arrow.render("↑ +1 m", True, "Dark Blue")
m_rect_inc = m_surf_inc.get_rect(midbottom = (text_rect.centerx, text_rect.top))
m_surf_dec = arrow.render("↓ -1 m", True, "Dark Blue")
m_rect_dec = m_surf_inc.get_rect(midtop = (text_rect.centerx, text_rect.bottom))

s_surf_inc = arrow.render("↑ +1 s", True, "Dark Blue")
s_rect_inc = s_surf_inc.get_rect(midbottom = (text_rect.right - text_rect.width / 6, text_rect.top))
s_surf_dec = arrow.render("↓ -1 s", True, "Dark Blue")
s_rect_dec = s_surf_inc.get_rect(midtop = (text_rect.right - text_rect.width / 6, text_rect.bottom))

start_stop_font = pygame.font.SysFont("Arial, Times New Roman", 40)
start_surf = start_stop_font.render("START", True, "Black")
start_rect = start_surf.get_rect(center = (200, 300))
stop_surf = start_stop_font.render("STOP", True, "Black")
stop_rect = stop_surf.get_rect(center = (600, 300))

comp_surf = comp_font.render("COUNTDOWN COMPLETED", True, "Dark Blue")
comp_rect = comp_surf.get_rect(center = base_screen_rect.center)

restart_surf = my_font.render("Restart", True, "Black")
restart_rect = restart_surf.get_rect(center = (base_screen_rect.right / 3, comp_rect.bottom + 30))
exit_surf = my_font.render("Exit", True, "Black")
exit_rect = exit_surf.get_rect(center = (base_screen_rect.right * 2 / 3, comp_rect.bottom + 30))


start_time = 0
pause_time = 0
paused = True
remaining_time = 3600       #Countdown in seconds later converted to hours and minutes
hh = mm = ss = ms = 00      #ms is millisecond used to compensate excessive delay
counting = True
start_display = "START"
stop_display = "STOP"

#Functionality
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #To exit using cross button
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):  #Clicked on Pause/Resume button
                paused = not paused
                if paused:
                    start_display = "RESUME"
                    stop_display = "RESET"
                    current_time = pygame.time.get_ticks()
                    remaining_time -= int((current_time - start_time) / 1000)
                    ms = (current_time - start_time) % 1000
                    print("Paused")
                else:
                    start_display = "PAUSE"
                    stop_display = "STOP"
                    counting = True
                    print("Resume")
                    start_time = pygame.time.get_ticks() - ms
            if stop_rect.collidepoint(event.pos):   #Clicked on Reset/Stop button
                #if timer is not paused, question not clear, so, I showed countdown finished
                if not paused or stop_display == "STOP":
                    remaining_time = 0
                    paused = True
                    counting = False
                    print("Stop")
                else:                       #if timer is paused, reset to 1 hour
                    start_display = "START"
                    stop_display = "STOP"
                    remaining_time = 3600
                    print("Reset")
            if paused:         #Enable changing the countdown, only if timer is paused
                if h_rect_inc.collidepoint(event.pos):
                    remaining_time += 3600
                if h_rect_dec.collidepoint(event.pos):
                    remaining_time -= 3600
                if m_rect_inc.collidepoint(event.pos):
                    remaining_time += 60
                if m_rect_dec.collidepoint(event.pos):
                    remaining_time -= 60
                if s_rect_inc.collidepoint(event.pos):
                    remaining_time += 1
                if s_rect_dec.collidepoint(event.pos):
                    remaining_time -= 1   
            #Extra Functionalities
            if restart_rect.collidepoint(event.pos):        #To restart the Timer after completion
                counting = True
                remaining_time = 3600
                paused = True
                start_display = "START"
                stop_display = "STOP"
            if exit_rect.collidepoint(event.pos):           #Exit Button
                pygame.quit()
                exit()

    if not paused:
        current_time = pygame.time.get_ticks()
        time_passed = int((current_time - start_time) / 1000)
        mm = remaining_time - time_passed
        if(mm < 0):                     #Stop negative time
            mm = 0
            counting = False            #Countdown is completed
    else:
        mm = remaining_time

    #Stop negative time
    if remaining_time < 0:
        remaining_time = 0

    #Convert remaining time(seconds) to hours, minutes and seconds
    ss = mm % 60
    hh = int(mm / 60)
    mm = hh % 60
    hh = int(hh / 60)

    #Display Time in hour, minutes and seconds
    text_surf = text_font.render(f"{hh:02d} h : {mm:02d} m : {ss:02d} s", True, "Black")

    start_surf = start_stop_font.render(f"{start_display}", True, "Black")
    start_rect = start_surf.get_rect(center = (200, 300))
    stop_surf = start_stop_font.render(f"{stop_display}", True, "Black")
    stop_rect = stop_surf.get_rect(center = (600, 300))

    display()                   #Display objects on screen

    if not counting:            #Countdown Completed option to restart/exit
        base_screen.fill("Cyan")
        base_screen.blit(comp_surf, (comp_rect.x, comp_rect.y - 80))
        pygame.draw.rect(base_screen, (148,216,93), restart_rect)
        base_screen.blit(restart_surf, restart_rect)
        pygame.draw.rect(base_screen, (148,216,93), exit_rect)
        base_screen.blit(exit_surf, exit_rect)

    pygame.display.update()     #refresh base_screen