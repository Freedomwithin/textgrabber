[app]
# Application title
title = Grabber4.0

# Package name (lowercase, no spaces)
package.name = grabber4

# Package domain (reverse DNS format)
package.domain = org.jonathon

# Directory containing your main.py
source.dir = .

# File extensions to include in the build
source.include_exts = py,png,jpg,kv,json,txt

# Application version
version = 1.0

# Python requirements (comma-separated)
requirements = python3,kivy==2.3.0,pillow,requests,pyjnius

# Screen orientation
orientation = portrait

# Start in fullscreen
fullscreen = 1

# Android permissions (comma-separated)
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android API level
android.api = 30

# Minimum Android API level
android.minapi = 21

# Android NDK version (must match your downloaded NDK)
android.ndk = 25b

# Path to your NDK (if you downloaded it manually)
android.ndk_path = /root/.buildozer/android/platform/android-ndk-r25b-linux

# Android build tools version
android.build_tools_version = 34.0.0

# Allow backup (default: True)
android.allow_backup = True

# Target architectures (comma-separated)
android.archs = armeabi-v7a

# (Optional) Presplash and icon (uncomment and set if you have them)
#presplash.filename = %(source.dir)s/data/presplash.png
#icon.filename = %(source.dir)s/data/icon.png

# (Optional) Notification icon (uncomment and set if you have it)
#android.notification_icon = %(source.dir)s/data/notification_icon.png

[buildozer]
# Log level (0=error, 1=info, 2=debug)
log_level = 2

# Disable warning about running as root (useful for Colab)
warn_on_root = 0
