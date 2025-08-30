#!/usr/bin/python

import os, sys, shutil, os.path as path
import importlib.util

SRC_DIR = os.path.abspath('./source')
DIST_DIR = os.path.abspath('./dist')

LOCAL_INSTALL = f'{path.expanduser('~')}/.local/share/icons/'
SYSTEM_INSTALL = '/usr/share/icons/'

THEME_NAME = 'kubu'

IGNORE_FOLDERS = ['templates', 'source', '__pycache__']

COPY_ROOT_FILES = ['AUTHORS', 'COPYING', 'index.theme']


def get_links(file: str):
    """ 
        Some sections have link.py files with alternate names for the icons which we dynamically import here.
    """
    spec = importlib.util.spec_from_file_location("links", file)
    links = importlib.util.module_from_spec(spec)
    sys.modules["links"] = links
    spec.loader.exec_module(links)
    return links.links


def build_theme(dark_mode: bool):    
    # Remove old output folder.
    try: shutil.rmtree(DIST_DIR)
    except: pass 
    os.mkdir(DIST_DIR)

    # Copy root files in source folder.
    for file in COPY_ROOT_FILES:
        shutil.copyfile(f'{SRC_DIR}/{file}', f'{DIST_DIR}/{file}')

    # Copy icons from different sections.
    for section in os.listdir(SRC_DIR):
        if path.isdir(f'{SRC_DIR}/{section}') and not section in IGNORE_FOLDERS:
            os.mkdir(f'{DIST_DIR}/{section}')
            
            # Get alternate names for icons in this section (we'll make logical links to the main 
            # instance for each alternate name)
            links_file = f'{SRC_DIR}/{section}/links.py'
            links = {}
            if path.exists(links_file):
                links = get_links(links_file)

            # Iterate over different sizes.
            for size in os.listdir(f'{SRC_DIR}/{section}'):
                if path.isdir(f'{SRC_DIR}/{section}/{size}') and not size in IGNORE_FOLDERS:
                    
                    os.mkdir(f'{DIST_DIR}/{section}/{size}')
                    
                    # Iterate over all icons in the folder.
                    for icon in os.listdir(f'{SRC_DIR}/{section}/{size}'):
                        dest_icon = icon
                        # Is this a darkmode icon?
                        if '-dark.svg' in icon:
                            if dark_mode:
                                dest_icon = icon.replace('-dark.svg', '.svg')
                            else: 
                                continue
                        # Does a darkmode version exist?
                        elif path.exists(f'{SRC_DIR}/{section}/{size}/{icon.replace('.svg', '-dark.svg')}'):
                            if dark_mode:
                                # Then don't 
                                continue
                        shutil.copyfile(
                            f'{SRC_DIR}/{section}/{size}/{icon}', 
                            f'{DIST_DIR}/{section}/{size}/{dest_icon}'
                        )

                        # Does this icon have alternate names
                        icon_name = dest_icon.replace('.svg', '');
                        if icon_name in links:
                            for link in links[icon_name]:
                                os.symlink(f'{dest_icon}',f'{DIST_DIR}/{section}/{size}/{link}.svg')


def install_user():
    """ Installs the theme for this user only """
    try: shutil.rmtree(LOCAL_INSTALL+THEME_NAME)
    except: pass
    shutil.move(DIST_DIR+'/', LOCAL_INSTALL+THEME_NAME)


def install_system():
    """ Installs the theme for this user only """
    try: shutil.rmtree(SYSTEM_INSTALL+THEME_NAME)
    except: pass
    shutil.move(DIST_DIR+'/', SYSTEM_INSTALL+THEME_NAME)


def uninstall():
    """ Tries to uninstall the theme from all locations """
    try:
        shutil.rmtree(LOCAL_INSTALL+THEME_NAME)
    except: 
        pass
    try:
        shutil.rmtree(SYSTEM_INSTALL+THEME_NAME)
    except: 
        pass


if __name__ == '__main__':
    if '--uninstall' in sys.argv:
        uninstall()
        exit(0)

    dark_mode = '--dark-mode' in sys.argv

    build_theme(dark_mode)

    if '--install-system' in sys.argv:
        install_system()
    if '--install-user' in sys.argv:
        install_user()

