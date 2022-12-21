import configparser

config = configparser.ConfigParser()
config.read('config.ini')

maze_path = config['paths']['maze_path']
