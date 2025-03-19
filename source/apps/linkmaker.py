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
        "amongus",
        "steam_icon_945360",
    ],
    "portal-2": [
        "steam_icon_620",
        "portal2",
    ],
    "steam": [
        "com.valvesoftware.Steam"
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
    "transmission": [
        "org.equiem.Tremotesf",
        "transmission-gtk",
        "transmission-qt",
        "transmission-remote-gtk",
        "transmission-remote-qt",
        "tTremotesf",
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
    "firefox-developer-edition": [
        "firefox-developer",
        "firefox-aurora",
        "firefox-aurora-icon",
        "firefox-developer-edition",
        "firefox-developer-icon",
        "firefox-nightly",
        "firefox-nightly-icon",
        "firefox-trunk",
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
        "com.discordapp.Discord",
        "com.discordapp.DiscordPTB",
        "de.shorsh.discord-screenaudio",
        "discord-development",
        "discord-ptb",
        "discord-bin",
        ""
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
    "chromium": [
        "google-chromium"
    ],
    "vlc":[
        "org.videolan.VLC",
        "Vlc"
    ],
    "mysql-workbench": [
        "mysqlworkbench"
    ],
    "whatsapp": [
        "com.gigitux.youp",
        "com.gigitux.gtkwhats",
        "com.github.WhatsApp-For-Linux",
        "com.github.eneshecan.WhatsAppForLinux",
        "com.rtosta.zapzap",
        ""
    ],
    "fspy": [
        "appimagekit-fspy",
        "62121369-112df900-b289-11e9-8105-bbeec105c8a1",
        "appimagekit_464d350626db9e9aed3bbe4986f9e2d2-fSpy",
        "appimagekit_464d350626db9e9aed3bbe4986f9e2d2-fspy",
    ],
    "vim":[
        "vim-qt",
        "vimlogo",
        "gvim"
    ],
    "godot:": [
        "lutris_godot-engine",
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
    "davinci-resolve-uninstaller": [
        "DV_Uninstall",
        "com.blackmagicdesign.resolve-Installer",
        "resolve-Installer",
    ],
    "davinci-resolve-pannels": [
        "DV_Panels",
        "com.blackmagicdesign.resolve-Panels",
        "resolve-Panels",
    ],
    "easy-tag": [
        "easytag",
    ],
    "obsidian": [
        "Obsidian"
    ],
    "adobe-photoshop-2020": [
        "4473_photoshop.0",
    ],
    "app-image-launcher": [
        "appimagelauncher",
        "AppImageLauncher",
    ],
    "rpi-imager": [
        "raspberrypi-imager",
        "org.raspberrypi.rpi-imager",
    ],
    "postman": [
        "Postman",
        "com.getpostman.Postman",
    ],
    "inkscape": [
        "org.inkscape.Inkscape",
        "inkscape.viewer",
        "inkscape-logo",
    ],
    "renderdoc": [
        "Renderdoc",
    ],
    "android-studio": [
        "androidstudio",
        "android-studio-beta",
    ],
}

os.system("mkdir -f ./links")

for key in icons:
    for link in icons[key]:
        cmd = f"ln -f -s ./../scalable/{key}.svg ./links/{link}.svg"
        os.system(cmd)

libreoffice_apps = ['base', 'calc', 'draw', 'impress', 'math', 'oasis-web', 'template', 'writer']
versions = [ '3', '4.2', '5.0', '5.1', '5.3', '5.4', '6.0', '6.2', '6.4', '7.0', '7.2', '34', '7.4', '7.5', '7.6', 'dev6.1', 'dev6.0' ]

for app in libreoffice_apps:
    for version in versions:
        origin = f'libreoffice-{app}'
        dest = f'libreoffice{version}-{app}'
        cmd = f"ln -f -s ./../scalable/{origin}.svg ./links/{dest}.svg"
        os.system(cmd)

print('done ...')
