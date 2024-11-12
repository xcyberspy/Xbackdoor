<h1 align="center" id="title">Xsbackdoor</h1>

<p align="center"><img src="https://socialify.git.ci/xcyberspy/Xsbackdoor/image?font=Rokkitt&forks=1&issues=1&language=1&name=1&owner=1&pattern=Overlapping%20Hexagons&pulls=1&stargazers=1&theme=Auto"></p>

<p id="description">This script creates a simple reverse shell backdoor that allows a remote attacker to execute commands on the victim's machine. The script connects to a remote server at a specified IP address and port then continuously listens for commands by using python</p>

<p align="center"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&amp;logo=python&amp;logoColor=ffdd54" alt="shields"></p>



## 🚀 How to Use

1. **Set Up the Connection**  
   Replace `'your ngrok link ip or ip or localhost` in the script with your `ngrok` URL or `localhost` IP if running locally.

2. **Run the Server**  
   Start `server.py` in your terminal to establish the main server connection.

3. **Run on Target Machine**  
   On the target machine, execute `client.py` to connect it to the server.

4. **Control the Target Machine**  
   Use the following commands in the server terminal to interact with the target machine:

## ⌨️ Commands

- **File Operations**  
  - `cd` : Change directory
  - `ls` : List directory contents
  - `mdir` : Make a directory
  - `rvf` : Rename a file
  - `rvd` : Rename a directory
  - `rm` : Remove file or directory
  - `gsize` : Get file size
  - `cwd` : Show current working directory

- **Additional Controls**
  - `camera` : Activate the camera to capture an image
  - `screen` : Capture a screen recording
  - `download` : Download files or folders

## 📜 Notes

Ensure `ngrok` is properly set up and both `server.py` and `client.py` are correctly configured to allow full communication between devices. Follow security best practices when using these scripts.




<h1 align="center">GUI SOON:</h1>

<p align="center" href="https://ibb.co/BLb5j1p"><img src="https://i.ibb.co/Q9L3n5g/Xsbackdoor.png" alt="Xskeylogger" border="0"></p>


<h2>🛠️ Installation Steps:</h2>

<p>1.First step </p>

```
git clone https://github.com/xcyberspy/Xsbackdoor.git
```

<p>2.Second step</p>

```
cd Xsbackdoor
```



<h2>🍰 Contribution Guidelines:</h2>

Disclaimer: This code is for educational purposes only. Using backdoors for unauthorized access is illegal and unethical. Always ensure that your work complies with ethical guidelines and legal requirements

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   python
*   vscode


<h2>💖Like my work?</h2>

<p><a href="https://www.buymeacoffee.com/xcyberspy" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;"></a></p>
