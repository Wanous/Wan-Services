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
- Browse your local movie library
- Grid layout with covers
- Responsive design (PC, tablet, phone)

[image here of the movies page]

---

### TV Series management
- Automatic detection of series, seasons and episodes
- Season selector with episode list

[image here of the series page]

---

### Integrated search
- Floating search bar
- Real-time filtering
- Clear button to reset search
- Works on movies and series

[image here of the search bar]

---

### ⚙️ Settings panel
- Change media directory
- Restart or stop the server from the web interface
- Restart warning when configuration changes
- Designed for both PC and Raspberry Pi usage

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


---

## Installation

Installation guides are separated by platform:

- 📄 **PC installation guide**  
  See: `docs/INSTALL_PC.md`

- 📄 **Raspberry Pi installation guide**  
  See: `docs/INSTALL_RASPBERRYPI.md`

## Note on privacy

Wan’Services:
- Does **not** connect to the internet
- Does **not** collect any data
- Runs entirely on your local network


## Conclusion

Wan’Services was created to provide a simple, local and private alternative to streaming platforms.
If you wish to modify this project, please note that it is entirely open-source.
