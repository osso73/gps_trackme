# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). For the version numbers, I just use a simple 2-digit, for major and minor changes. Each version has its corresponding apk under the folder `releases`.


## 1.0 - 2021-05-08

### Changed
- Precision of the GPS coordinates adjusted to phone, by reducing to 5 decimals (degrees view) or 2 decimals for the seconds (deg-min-sec view).

### Added
- Map, with icon showing current GPS position, as per iss. #1
- Menu with options to see log, help, about, and settings (not yet implemented), as per iss. #2
- Button to capture current position, with a comment, as per iss. #3.
- App icon and splash screen.


## 0.1 - 2021-05-02

Initial release, showing very basic functionality of using GPS and showing position.


## Added
- GPS activation (permissions, etc.), show current GPS coordinates in the screen
- Button to switch on/off GPS
- Status icon and text, showing if GPS is on, searching or off
- Accuracy icon to show the level of accuracy of the coordinates
