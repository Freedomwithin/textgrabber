[app]

# (str) Title of your application
title = Grabber4.0

# (str) Package name
package.name = grabber4

# (str) Package domain (needed for android/ios packaging)
package.domain = org.jonathon

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,pillow,requests,pyjnius

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Android API to use
# Set to 35 for Android 15, but 30 is fine for compatibility.
# If you want to target Android 15 specifically, uncomment the next line:
# android.api = 35
android.api = 30

# (str) Minimum API required
android.minapi = 21

# (str) Android SDK directory, if empty, it will be automatically detected.
#android.sdk_path =

# (str) Android NDK directory, if empty, it will be automatically detected.
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b-linux

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use
android.build_tools_version = 34.0.0

# (bool) If True, then automatically try to detect the NDK and SDK
# android.auto_detect = True

# (list) Permissions
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Android incremental version code
#android.numeric_version = 1

# (bool) If True, then allow backup of the application
android.allow_backup = True

# (str) Supported architectures
# Add arm64-v8a for modern devices like Moto G 2025
# armeabi-v7a is kept for compatibility with older devices
android.archs = armeabi-v7a,arm64-v8a

# (str) Notification icon (if not set, it will use the icon)
#android.notification_icon = %(source.dir)s/data/notification_icon.png

# (str) Android branch of python-for-android to use
p4a.branch = develop

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,images/*/*.jpg
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#images/*/*.jpg
#
