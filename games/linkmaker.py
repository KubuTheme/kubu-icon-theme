import os

icons = {
    "minecraft": [
        "Minecraft",
        "minecraft-launcher",
        "minecraft-pi",
        "minetest",
        "minetest-icon",
    ],
    "among-us": [
        "among-us",
        "amongus"
    ],
    "mini-motorways": [
        "mini-motorways",
        "minimotorways",
        "steam_icon_1127500",
    ],
}

os.system("mkdir -f ./links")

for key in icons:
    for link in icons[key]:
        cmd = f"ln -f -s ./../scalable/{key}.svg ./links/{link}.svg"
        os.system(cmd)

print('done ...')
