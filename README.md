# Wan Services

![Wan services Banner](assets/images/Banniere_WanServices.png)

<div align=center>
    <img alt="Taille du code GitHub" src="https://img.shields.io/github/languages/code-size/Wanous/Wan-Services?label=taille%20du%20code">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Wanous/Wan-Services?logo=github&style=plastic">
    <img alt="License" src="https://img.shields.io/github/license/Wanous/Wan-Services?style=plastic">
    <p></p>
</div>

Wan Services is a lightweight, self-hosted multimedia web platform designed to stream movies and TV series through a clean and responsive web interface to any device connected to your local network.

## Supported Platforms
![Windows](https://img.shields.io/badge/Windows-Supported-blue)
![Linux](https://img.shields.io/badge/Linux-Supported-yellow)
![macOS](https://img.shields.io/badge/macOS-Supported-lightgrey)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Supported-red)

## Built with
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-black)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-orange)
![systemd](https://img.shields.io/badge/Raspberry%20Pi-systemd-critical)


## Features

###  Movies streaming
- Browse your local movie library on a grid layout with covers. Plus the design is responsive (PC, tablet, phone)

[image here of the movies page]

---

### TV Series management
- Same grid layout with a automatic detection of series, seasons and episodes. When a series is selected, you are lead to a season selector with episode list.

[image here of the series page]

---

### Integrated search
- Floating search bar with real-time filtering and a clear button to reset search. It works on movies and series.

[image here of the search bar]

---

### ⚙️ Settings panel
- In the settings page you can change media directory and stop the server from the web interface.

**Note** that there is different parameters depending on the support

[image here of the settings page]

---

### 🖥️ PC & Raspberry Pi support
- **PC version**
  - Simple execution
  - No system modification required
- **Raspberry Pi version**
  - Automatic startup with systemd
  - External storage support
  - Designed for headless usage

---

## 🗂️ Media structure

Wan’Services expects the following directory structure:
```
Media/
├── Movies/
│ ├── MovieName.mp4
│ └── MovieName.jpg (optional cover)
└── Series/
    └── SeriesName/
        ├── cover.jpg (optional)
        └── Season01/
            ├── Episode01.mp4
            └── Episode02.mp4
```
You can place the `Media` folder anywhere on your computer or accessible external storage. Also you can call it whatever you want. Just respect the structure inside `Media`.

---

## Installation

Installation guides are separated by platform:

- 📄 **PC installation guide**  
  - See : [release](https://github.com/Wanous/Wan-Services/releases) for executable (.exe, .app, ...)
  - See: `docs/INSTALL_PC.md` [here](https://github.com/Wanous/Wan-Services/docs/INSTALL_PC.md) to customize or extend the project

- 📄 **Raspberry Pi installation guide**  
  See: `docs/INSTALL_RASPBERRYPI.md` [here](https://github.com/Wanous/Wan-Services/docs/INSTALL_PC.md)

## Note on privacy

Wan’Services:
- Does **not** connect to the internet
- Does **not** collect any data
- Runs entirely on your local network


## Conclusion

Wan’Services was created to provide a simple, local and private alternative to streaming platforms.
If you wish to modify this project, please note that it is entirely open-source.
