from actor import Actor
from clip import Clip
from documentary import Documentary
from film import Film
from series import Series
from pyfiglet import Figlet
import sys

def show_menu():
    print('welcome to the biggest media database. Specify your operation: ')
    print('1- Add')
    print('2- Edit')
    print('3- Delete')
    print('4- Search')
    print('5- Show')
    print('6- Download')
    print('7- Advance Search')
    print('8- Exit')

def add_media(media):
    id = input('Enter ID of product: ')
    for medium in media:
        if medium.id == id:
            print('This medium is repetitious and is available in database')
            break
    else:
        type_medium = input('Choose type of medium: Clip, Documentary, Film, Series ')
        name = input('Enter name of medium: ')
        director = input('Enter director of medium: ')
        IMDB_score = input('Enter IMDB_score of medium: ')
        url = input('Enter url of medium: ')
        duration = input('Enter duration of medium: ')
        casts = input('Enter casts of medium: ')
        if type_medium == 'Clip':
            medium = Clip(id=id, name=name, director=director, IMDB_score=IMDB_score, url=url, duration=duration, casts=casts)
        elif type_medium == 'Documentary':
            medium = Documentary(id=id, name=name, director=director, IMDB_score=IMDB_score, url=url, duration=duration, casts=casts)
        elif type_medium == 'Film':
            medium = Film(id=id, name=name, director=director, IMDB_score=IMDB_score, url=url, duration=duration, casts=casts)
        elif type_medium == 'Series':
            season = input('Enter season of medium')
            part = input('Enter part of medium')
            medium = Series(id=id, name=name, director=director, IMDB_score=IMDB_score, url=url, 
            duration=duration, season=season, part=part, casts=casts)
        media.append(medium) 
        print('Added medium into database')
    return media

def edit_media(media):
    id = input('Enter id of medium that you want to edit: ')
    item = input('Enter item that you want to edit: ')
    item_value = input('Enter new value: ')
    for medium in media:
        if medium.id == id:
            if item == 'name':
                medium.name = item_value
            elif item == 'director':
                medium.director = item_value
            print('Product edited ........ ')
            break
    return media

def delete_media(media):
    id = input('Enter id of medium that you want to delete: ')
    for medium in media:
        if medium.id == id:
            media.remove(medium)
            print('Medium removed ....... ')
            break
    return media

def serach_media(media):
    name = input('Enter name of medium that you want to search: ')
    for medium in media:
        if medium.name == name:
            medium.show_info()
            break
    else:
        print('medium not found')

def show_media(media):
    for medium in media:
        medium.show_info()
        
def download_media(media):
    id = input('Enter ID of medium that you want to download: ')
    for medium in media:
        if medium.id == id:
            medium.download()
    else:
        print('Unfortunately we dont have this medium')

def advance_search_media(media):
    min_duration = int(input('Enter minimum of duration: '))
    max_duration = int(input('Enter maximum of duration: '))
    for medium in media:
        if (int(medium.duration) > min_duration) and (int(medium.duration) < max_duration):
            medium.show_info()

def exit_program(media):
    with open('database.txt', 'w') as f:
        for medium in media:
            medium.write_info(f)
    print('Exited ........')
    sys.exit()

def read_database():
    print('Loading database ....... ')
    media = list()
    with open('database.txt', 'r') as f:
        for line in f:
            line = line.strip()
            before_casts, casts = line.split(',[')[0], line.split(',[')[1]
            medium_list = before_casts.split(',')
            if medium_list[1] == 'Clip':
                medium = Clip(id=medium_list[0], name=medium_list[2], director=medium_list[3], IMDB_score=medium_list[4], url=medium_list[5], 
                duration=medium_list[6], casts=casts[:-1])
            elif medium_list[1] == 'Documentary':
                medium = Documentary(id=medium_list[0], name=medium_list[2], director=medium_list[3], IMDB_score=medium_list[4], url=medium_list[5], 
                duration=medium_list[6], casts=casts[:-1])
            elif medium_list[1] == 'Film':
                medium = Film(id=medium_list[0], name=medium_list[2], director=medium_list[3], IMDB_score=medium_list[4], url=medium_list[5], 
                duration=medium_list[6], casts=casts[:-1])
            elif medium_list[1] == 'Series':
                medium = Series(id=medium_list[0], name=medium_list[2], director=medium_list[3], IMDB_score=medium_list[4], url=medium_list[5], 
                duration=medium_list[6], season=medium_list[7], part=medium_list[8], casts=casts[:-1])
            media.append(medium)
    print('Loaded database ....... ')
    return media

if __name__ == '__main__':
    f = Figlet(font='standard')
    print(f.renderText('Media database'))
    media = read_database()
    show_menu()
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            media = add_media(media)
        elif choice == '2':
            products = edit_media(media)
        elif choice == '3':
            media = delete_media(media)
        elif choice == '4':
            serach_media(media)
        elif choice == '5':
            show_media(media)
        elif choice == '6':
            download_media(media)
        elif choice == '7':
            advance_search_media(media)
        elif choice == '8':
            exit_program(media)
        else:
            print("Invalid input")

