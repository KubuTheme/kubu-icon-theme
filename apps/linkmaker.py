import os

icons = {
    "ms-office-teams": [
        "teams"
    ],
    "jetbrains-intellij":[
        "intellij",
        "intellij-idea",
        "jetbrains-idea-ce",
        "intellij-idea-community"
    ],
    "jetbrains-pycharm": [
        "pycharm",
        "pycharm-professional",
        "pycharm-education",
        "pycharm-community",
        "com.jetbrains.PyCharm",
        "com.jetbrains.PyCharm-Professional",
        "com.jetbrains.PyCharm-Community"
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
    "firefox-dark":[
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
    "google-chromium": [
        "chromium"
    ],
    "vlc":[
        "org.videolan.VLC",
        "Vlc"
    ],
    "vim":[
        "vim-qt",
        "vimlogo"
    ],
    "file-manager": [
        "dolphin",
        "thunar",
        "Thunar",
        "thunar-filemanager",
        "system-file-manager",
        "spacefm",
        "dde-file-manager",
        "org.kde.dolphin"
    ],
    "skype": [
        "Skype",
        "skypeforlinux",
        "skype_protocol"
    ],
    "spotify": [
        "Spotify",
        "com.spotify.Client"
    ],
    "lollypop": [
        "org.gnome.Lollypop",
        "Lollypop"
    ]
}

os.system("mkdir -f ./links")

for key in icons:
    for link in icons[key]:
        cmd = f"ln -f -s ./../scalable/{key}.svg ./links/{link}.svg"
        os.system(cmd)

print('done ...')
