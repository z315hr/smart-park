[app]
title = Smart Park
package.name = smartpark
package.domain = org.zahraa.smartpark
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = armeabi-v7a arm64-v8a