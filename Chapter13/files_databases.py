# Date:06/11/2025
# Program to implement files and directories
import os 
print(os.getcwd())
print(os.path.abspath('photos'))
print(os.listdir('photos'))
print(os.listdir('photos/jan-2023'))
print(os.path.exists('photos'))
print(os.path.exists('photos/apr-2023'))
print(os.path.isdir('photos'))
print(os.path.isfile('photos/notes.txt'))
