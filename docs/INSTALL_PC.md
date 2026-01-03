# Wan’Services – PC Installation Guide  
(Windows / Linux / macOS)

## ⚠️ Important Notice

If you are simply looking for an easy way to run Wan’Services on your computer, a **simpler installation method using a prebuilt executable** is available in the release of this GitHub project.

This guide is mainly provided for those who want to:
- Understand how Wan’Services works internally
- Customize or extend the project
- Contribute to its development

---

## Requirements


- Python **3.9 or newer**
- A web browser (Chrome, Firefox, Edge, Safari)
- An accessible folder containing your media
---

## 📁 Media folder structure

Wan’Services expects the following structure:
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

## Step 1 – Install Python

### Windows
1. Download Python from: https://www.python.org/downloads/
2. During installation:
   - Check **“Add Python to PATH”**
3. Verify installation:
   ```powershell
   python --version
   ```


### Linux

Python is usually preinstalled.

```bash
python3 --version
```

If not:

```bash
sudo apt install python3 python3-pip
```

### macOS

Using Homebrew :

```bash
brew install python
```

---

## Step 2 – Download Wan’Services

### With GitHub 

```bash
git clone https://github.com/Wanous/Wan-Services.git
cd Wan-Services
```

### Or by downloading the ZIP file

1. Go to the GitHub repository
2. Click **Code → Download ZIP**
3. Extract the archive

---

## Step 3 – Install dependencies

From the project root:

### Windows

```powershell
python -m pip install -r requirements.txt
```

### Linux / macOS

```bash
pip3 install -r requirements.txt
```

---

## Step 4 – Configure Wan’Services

Edit the file `config.json`:

```json
{
  "profile": "pc",
  "media_path": "D:/Media",
  "server": {
    "host": "127.0.0.1",
    "port": 5000
  },
  "ui": {
    "enable_settings": true
  }
}
```

### Notes

* `media_path` must point to the folder that contains `Movies/` and `Series/`
* On Linux/macOS, use paths like:

  ```
  /home/user/Media
  ```

---

## Step 5 – Run the server

From the project root:

### Windows

```powershell
python launcher.py
```

### Linux / macOS

```bash
python3 launcher.py
```

You should see something like:

```
===================================
    Wan'Services server starting
    Host : ...
    Port : ...
    Press Ctrl+C to stop
===================================
```

---

## Step 6 – Access Wan’Services

Normally your browser should open automatically but if not :
Open your browser and go to

```
http://127.0.0.1:5000
```

If your firewall allows it, other devices on your local network can access it using your PC’s IP address.

---

## Stopping the server

### From the terminal

Press:

```
Ctrl + C
```

### From the web interface

* Open **Settings**
* Click **Stop server**


## Troubleshooting

### Page not loading

* Check the terminal output
* Make sure the port is not already in use

### Media not showing

* Verify the folder structure
* Ensure file extensions are `.mp4`
* Check the `media_path` in `config.json`






