import os

icons = {
    "telegram.svg":[
        "chrome-https___telegram.org_.svg",
        "goa-account-telegram.svg",
        "org.telegram.desktop.svg",
        "telegram-desktop.svg",
        "unity-webapps-telegram.svg",
        "web-telegram.svg"
    ],
    "vs-code.svg":[
        "visual-studio-code.svg",
        "com.visualstudio.code.svg",
        "com.visualstudio.code-oss.svg",
        "com.visualstudio.code.oss.svg",
        "visualstudiocode.svg",
        "code-oss.svg",
        "vscodium.svg",
        "vscode.svg",
        "vso.svg",
        "vsc.svg"
    ],
    "firefox.svg":[
        "firefox-3.0.svg",
        "firefox-3.5.svg",
        "firefox-4.0.svg",
        "firefox-beta-bin.svg",
        "firefox-bin.svg",
        "firefox-beta.svg",
        "firefox-default.svg",
        "firefox-esr.svg",
        "firefox-gtk3.svg",
        "firefox-icon.svg"
    ],
    "discord.svg":[
        "discord-ptb.svg",
        "web-discord.svg",
        "com.discordapp.Discord.svg"
    ],
    "spotify.svg":[
        "Spotify.svg",
        "spotify_A.svg",
        "spotify-client.svg",
        "spotify-linux-48x48.svg",
        "spotify-linux-512x512.svg",
        "spotify-web-player.svg",
        "spotify-client.svg"
        "spotifywebplayer.svg"
    ],
    "google-chrome.svg":[
        "chrome.svg",
        "google-chrome2.svg",
        "google-chrome-dev.svg",
        "google-chrome-beta.svg",
        "googlechrome.svg",
        "google-chrome-unstable.svg"
    ],
    "vlc.svg":[
        "org.videolan.VLC.svg",
        "Vlc.svg"
    ]
}

for key in icons:
    for link in icons[key]:
        cmd = 'ln -s ./../scalable/'+key+' ./links/'+link
        os.system(cmd)

print('done ...')
