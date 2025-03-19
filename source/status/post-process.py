import os

for file in os.listdir('./SVG'):
    if file.endswith('.svg'):
        [size, name] = file.split('_')
        size = int(size.split('x')[0])

        os.system(f'mkdir -p {size}')
        os.system(f'mv SVG/{file} {size}/{name}')

os.system(f'rmdir SVG')
