import json
import os

sizes = [16,22,24]

with open('links.json') as links:
    links: dict = json.loads(links.read())
    for (source, links) in links.items():
        for size in sizes:
            icon = f'./{size}/{source}'
            if os.path.isfile(icon):
                for link in links:
                    icon_link = f'./{size}/{link}'
                    os.system(f'ln -fs {source} {icon_link}')
                    print(icon_link)
                    # os.system(f'ln -s {source} {icon_link}')
