import db
import random
from os import system


class func():
    @staticmethod
    def clear(): return system('cls')

    @staticmethod
    def end():
        import pyfiglet
        with open("font.txt", "r") as f:
            font = f.readlines()
            font = [x.strip('\n') for x in font]
        print(pyfiglet.figlet_format("Thank You", font=random.choice(font)))

    @staticmethod
    def add_device():
        name = input('Enter device name: ')
        with open('devices.txt', "a") as f:
            f.write(f'{name}\n')

    @staticmethod
    def add():
        def clear(): return system('cls')
        with open("devices.txt", "r") as f:
            d = f.readlines()
            d = [x.strip('\n') for x in d]
            d_name = {}
            for index, value in enumerate(d):
                d_name[index+1] = value

        l = len(d)
        k = True
        while k == True:
            clear()
            print('\t\t\tSelect the Device to Add')
            for i in d_name:
                print(f'Enter {i} for {d_name[i]}')
            print(f"Enter {l + 1} to go to Main Menu")
            n = int(input('Enter your option: '))
            if n <= l:
                clear()
                for i in d_name:
                    if n == i:
                        db.add_devices(d_name[i])
                        a = input(
                            'Do you want to add more record in (y/n): ').lower()
                        if a == 'y':
                            continue
                        else:
                            k = False
            elif n == l + 1:
                clear()
                break
            else:
                clear()
                print('Invalid Option...')
                input('Press Enter to continue...')
                continue

    @staticmethod
    def update():
        def clear(): return system('cls')
        with open("devices.txt", "r") as f:
            d = f.readlines()
            d = [x.strip('\n') for x in d]
            d_name = {}
            for index, value in enumerate(d):
                d_name[index+1] = value

        l = len(d)
        k = True
        while k == True:
            clear()
            print('\t\t\tSelect the Device to Update')
            for i in d_name:
                print(f'Enter {i} for {d_name[i]}')
            print(f"Enter {l + 1} to go to Main Menu")
            n = int(input('Enter your option: '))
            if n <= l:
                clear()
                for i in d_name:
                    if n == i:
                        db.update(d_name[i])
                        a = input(
                            'Do you want to add more record in (y/n): ').lower()
                        if a == 'y':
                            continue
                        else:
                            k = False
            elif n == l + 1:
                clear()
                break
            else:
                clear()
                print('Invalid Option...')
                input('Press Enter to continue...')
                continue
