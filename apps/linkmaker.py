import os

icons = {
    "jetbrains-intellij":[
        "intellij",
        "intellij-idea",
        "jetbrains-idea-ce",
        "intellij-idea-community"
    ],
    "telegram":[
        "chrome-https___telegram.org_",
        "goa-account-telegram",
        "org.telegram.desktop",
        "telegram-desktop",
        "unity-webapps-telegram",
        "web-telegram"
    ],
    "vs-code":[
        "visual-studio-code",
        "com.visualstudio.code",
        "com.visualstudio.code-oss",
        "com.visualstudio.code.oss",
        "visualstudiocode",
        "code-oss",
        "vscodium",
        "vscode",
        "vso",
        "vsc"
    ],
    "firefox":[
        "firefox-3.0",
        "firefox-3.5",
        "firefox-4.0",
        "firefox-beta-bin",
        "firefox-bin",
        "firefox-beta",
        "firefox-default",
        "firefox-esr",
        "firefox-gtk3",
        "firefox-icon"
    ],
    "discord":[
        "discord-ptb",
        "web-discord",
        "com.discordapp.Discord"
    ],
    "spotify":[
        "Spotify",
        "spotify_A",
        "spotify-client",
        "spotify-linux-48x48",
        "spotify-linux-512x512",
        "spotify-web-player",
        "spotify-client"
        "spotifywebplayer"
    ],
    "google-chrome":[
        "chrome",
        "google-chrome2",
        "google-chrome-dev",
        "google-chrome-beta",
        "googlechrome",
        "google-chrome-unstable"
    ],
    "vlc":[
        "org.videolan.VLC",
        "Vlc"
    ]
}

os.system("mkdir ./links")

for key in icons:
    for link in icons[key]:
        cmd = f"ln -s ./../scalable/{key}.svg ./links/{link}.svg"
        os.system(cmd)

print('done ...')
