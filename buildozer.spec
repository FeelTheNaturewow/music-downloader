[app]

# (str) Title of your application
title = SpotifyDownloader

# (str) Package name
package.name = spotify2mp3

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version.regex = __version__ = '(.*)'
version.filename = %(source.dir)s/main.py

# -------------------------------------------------------------------
# CRITICAL: This tells the app which libraries to install
# -------------------------------------------------------------------
# We added: mutagen (for audio tags), pycryptodomex (for encryption), certifi (for SSL), and sqlite3
requirements = python3,kivy==2.2.1,kivymd,pillow,yt-dlp,requests,openssl,mutagen,pycryptodomex,certifi,sqlite3

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# -------------------------------------------------------------------
# Android specific
# -------------------------------------------------------------------

# (list) Permissions
# INTERNET: To download music
# STORAGE: To save music to your files
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android API to use (33 is Android 13, a good modern standard)
android.api = 33

# (int) Minimum API required (21 = Android 5.0)
android.minapi = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (int) Android architecture to build for
android.archs = arm64-v8a

# -------------------------------------------------------------------
# FIX FOR GITHUB ACTIONS / AUTOMATION
# -------------------------------------------------------------------
# This prevents the "EOFError" and "Broken Pipe" crashes
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
