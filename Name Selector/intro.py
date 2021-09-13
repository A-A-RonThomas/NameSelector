import csv
from random import randint

# Opens a csv file and appends each entry to an array. Each name is in it's own array so
# when accessing a random name you have to index as such: name[random integer][0], to access
# the string value of that array instead of printing an array with the string inside.
def OpenFile(file,empty_array):
    with open(file, newline='') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            empty_array.append(row)
    return empty_array

WIDTH = 750
HEIGHT = 500

music.play('center')

names = Actor('names2',(375,300))
reset = Actor('reset',(45,20))
another = Actor('another', (625,20))
speaker = Actor('speaker_light', (125,25))

frame = 1
active_name_list = []
random_name = ''
random = 0

def draw():
    # Main Menu
    if frame == 1:
        screen.fill((156,105,157))
        screen.blit('ichooseyou', (115,150))
        names.draw()
        reset.draw()
        speaker.draw()

    # List of Lists of names
    if frame == 2:
        screen.fill((156,105,157))
        reset.draw()
        speaker.draw()
        screen.draw.text("Type the number of the list you want to pull from:", center=(375,100))
        screen.draw.text('1: CSCI1010-001', center=(375,175), fontsize=60)
        # Additional classes will need to be entered here and positioned correctly
        # and on_key_down function will need to be modified to accept additional key
        # commands to be able to access their respective .csv files.
        screen.draw.text('2: Some other class', center=(375,235), fontsize=60)

    # Chosen name.
    if frame == 3:
        screen.fill((156,105,157))
        screen.draw.text(random_name, center=(375,250), fontsize=60, color='black')
        reset.draw()
        another.draw()
        speaker.draw()

def on_mouse_down(pos):
    global frame
    global active_name_list
    global random_name
    global random

    if names.collidepoint(pos):
        frame = 2
    
    if reset.collidepoint(pos):
        frame = 1
        active_name_list = []
        random_name = ''

    if another.collidepoint(pos):
        frame = 3
        random = randint(0,len(active_name_list) - 1)
        random_name = active_name_list[random][0]
    
    if speaker.collidepoint(pos):
        if music.is_playing('center'):
            music.pause()
            speaker.image = 'speaker'
        else:
            music.unpause()
            speaker.image = 'speaker_light'

def on_mouse_move(pos):
    global active_name_list

    if another.collidepoint(pos):
        another.image = 'another_light'
    else:
        another.image = 'another'
    
    if names.collidepoint(pos):
        names.image = 'names2_light'
    else:
        names.image = 'names2'

    if reset.collidepoint(pos):
        reset.image = 'reset_light'
    else:
        reset.image = 'reset'
    
def on_key_down(key):
    global active_name_list
    global frame
    global random_name
    if frame == 2:
        if key == keys.K_1:
            OpenFile('Active_MLB_Players.csv',active_name_list)
            random = randint(0,len(active_name_list) - 1)
            random_name = active_name_list[random][0]
            frame = 3
    
    # Will need to hard code each key press to populate the active_name_list array

def update():
    pass