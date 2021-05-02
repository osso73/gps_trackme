# GPS TrackMe

A simple mobile application to register your gps position at a given moment in time.

The initial idea behind the application is to be able to get the GPS coordinates of your position, at a given time, so you can later know your position exactly. It can be used to know the GPS coordinates when taking a picture (if using a camera without GPS, or with GPS switched off), or to be able to remember a certain location.

Additional functionality may be to register a track and save it as a GPX track. I will explore this later.


## Usage

You can either run the python code and build an .apk image, or you can use directly the .apk image already compiled from the [`releases`](./releases) folder. In order to compile the code you will need the following dependencies:
- [kivy](https://kivy.org/doc/stable/): the main language to make the app run on the mobile
- [KivyMD](https://kivymd.readthedocs.io/en/latest/): a layer on top of `kivy` to make it pretty, using Material Design compliant widgets, icons and colours.
- [buildozer](https://buildozer.readthedocs.io/en/latest/): to compile kivy apps for mobile. Can be used both for android and for iOS.

Note the app will only work on android, I have not built the necessary configuration to run on iOS (and I don't have the tools to compile it and test it). Although it should be relatively straight forward, since the `plyer` module I'm using to access the GPS works for both android and iOS platforms.

See the instructions on how to use the app in the [manual pages](https://osso73.github.io/gps_trackme/).


## Contribution

I started this project to practice with KivyMD, and also to solve a functionality that I'm missing in my phone. I'm sure there are plenty of apps out there that can track your gps, but I wanted something very simple and straight forward, and avoid any advertising.

So I'm not expecting to have a collaboration on this project. Having said that, feel free to open issues to improve the code or the functionality. If you would like to contribute, drop me a mail.



## License

This project is under MIT license.
