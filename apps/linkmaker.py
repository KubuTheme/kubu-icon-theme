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
    "ms-office-teams": [
        "teams",
        "appimagekit-teams-for-linux",
        "teams-for-linux",
    ],
    "ms-office-powerpoint": [
        "ms-powerpoint",
    ],
    "ms-office-word": [
        "ms-word",
    ],
    "ms-office-outlook": [
        "ms-outlook",
    ],
    "ms-office-onenote": [
        "web-onenote",
        "io.gitlab.o20.onenote",
        "ms-onenote",
    ],
    "ms-office-excel": [
        "ms-excel",
    ],
    "musescore-4": [
        "org.musescore.MuseScore",
        "mscore",
        "musescore",
    ],
    "jetbrains-intellij":[
        "intellij",
        "intellij-idea",
        "jetbrains-idea-ce",
        "intellij-idea-community",
        "com.jetbrains.Community",
        "com.jetbrains.IntelliJ-IDEA-Community",
        "com.jetbrains.Intellij-IDEA-Community",
        "com.jetbrains.IntelliJ-IDEA-Ultimate",
        "com.jetbrains.Intellij-IDEA-Ultimate",
        "jetbrains-intellij-idea",
        "idea",
        "idea-ultimate"
        "intellij-idea-ce",
        "jetbrains-intellij-idea",
        "intellij-idea-ultimate",
        "intellij-idea-ultimate-edition",
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
    "jetbrains-datagrip": [
        "datagrip",
        "datagrip-professional",
        "datagrip-education",
        "datagrip-community",
        "com.jetbrains.DataGrip",
        "com.jetbrains.DataGrip-Professional",
        "com.jetbrains.DataGrip-Community",
        "datagrip_datagrip", 
    ],
    "telegram":[
        "chrome-https___telegram.org_",
        "goa-account-telegram",
        "org.telegram.desktop",
        "telegram-desktop",
        "unity-webapps-telegram",
        "web-telegram",
        "telegram-classic"
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
    "thunderbird": [
        "org.mozilla.Thunderbird",
        "Thunderbird",
    ],
    "jellyfin": [
        "com.github.iwalton3.jellyfin-media-player",
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
        "firefox-icon",
        "firefox3",
        "firefox-mozilla-build",
        "firefox-icon-unbranded",
        "org.mozilla.Firefox",
        "org.mozilla.firefox",
        "mozilla-firefox"
    ],
    "brave": [
        "brave-bin",
        "brave-desktop",
        "brave-browser",
        "brave-browser-beta",
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
        "vimlogo",
        "gvim"
    ],
    "file-manager": [
        "dolphin",
        "thunar",
        "Thunar",
        "thunar-filemanager",
        "user-file-manager",
        "system-file-manager",
        "redhat-filemanager",
        "xfce-filemanager",
        "spacefm",
        "dde-file-manager",
        "org.kde.dolphin",
        "org.gnome.files",
        "org.gnome.Files",
        "io.elementary.files",
        "Insight-FileManager",
        "file-system-manager",
        "filerunner"
    ],
    "skype": [
        "Skype",
        "skypeforlinux",
        "skype_protocol"
    ],
    "slack": [
        "com.slack.Slack"
    ],
    "spotify": [
        "Spotify",
        "com.spotify.Client",
        "spotify_A",
        "spotifywebplayer",
        "spotify-web-player",
        "spotify-linux-512x512",
        "spotify-linux-48x48",
        "spotify-client",
        "spotify-launcher",

    ],
    "lollypop": [
        "org.gnome.Lollypop",
        "Lollypop"
    ],
    "davinci-resolve": [
        "Davinci-Resolve",
        "DaVinci-Resolve",
        "com.blackmagicdesign.resolve",
    ],
    "easy-tag": [
        "easytag",
    ],
    "adobe-photoshop-2020": [
        "4473_photoshop.0",
    ]
}

os.system("mkdir -f ./links")

for key in icons:
    for link in icons[key]:
        cmd = f"ln -f -s ./../scalable/{key}.svg ./links/{link}.svg"
        os.system(cmd)

print('done ...')
