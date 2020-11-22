import os

DRIVER = os.getenv('DRIVER', '{SQL SERVER}')
SERVER = os.getenv('SERVER', 'NT-04521')
DATABASE = os.getenv('DATABASE', 'MARMITAS')
