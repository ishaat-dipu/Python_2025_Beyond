<h1>What is Python ?</h1>
<p>Python is a populer programming language . It was Created by Guido Van and it was Released in 1991 </p>
<p>It is used for : </p>
<ul>
  <li>Web Developement</li>
  <li>Software Developement</li>
  <li>Mathematics</li>
  <li>System Scripting </li>
  <li>Data Science and Machine Learning</li>
  <li>Automatin</li>
</ul>
<h1>Why Python?</h1>
<ul>
  <li>We can Works on Different Platforms (windows, MAC, Linux, Respberry Pi, etc.</li>
  <li>It is High Level language so it is Human Readable</li>
  <li>Python can be connected to database</li>
  <li>There are Lots of supported community and Library only Dedicated for Python</li>
  <li>Python can be Treated in Procedural way</li>
</ul>

<h1>Python Installation Guideline for Linux(manjaro)/Windows</h1>
# Python Installation Guide for Manjaro Linux

## 🚀 Prerequisites
- **Manjaro Linux** (Updated system recommended)
- **Basic terminal knowledge**

---

## 📦 Step 1: Check for Existing Python Installation
```bash
python --version
# or
python3 --version
```
If Python is not installed or outdated, follow the steps below.

---

## 🔄 Step 2: Update the System
```bash
sudo pacman -Syu
```
This ensures your system packages are up to date.

---

## 🐍 Step 3: Install Python Using Pacman
```bash
sudo pacman -S python
```
This will install the latest Python 3 along with `pip` (Python's package manager).

---

## ✅ Step 4: Verify the Installation
```bash
python --version
# or
python3 --version

pip --version
# or
pip3 --version
```

---

## ⚙️ Optional: Install Additional Python Tools
- **Virtual Environment:**
  ```bash
  sudo pacman -S python-virtualenv
  ```
- **IDLE (Python GUI):**
  ```bash
  sudo pacman -S idle
  ```

---

## 🔢 Step 5: Install a Specific Python Version (Using Pyenv)
If you need multiple versions of Python:

1. Install dependencies:
   ```bash
   sudo pacman -S git gcc make zlib libffi openssl readline xz
   ```
2. Install `pyenv`:
   ```bash
   curl https://pyenv.run | bash
   ```
3. Add `pyenv` to your shell:
   ```bash
   echo -e 'export PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```
4. Install Python version:
   ```bash
   pyenv install 3.11.0
   pyenv global 3.11.0
   ```

Verify:
```bash
python --version
```

---

## 🛠️ Troubleshooting
- **Fix broken dependencies:**
  ```bash
  sudo pacman -Syyu
  ```
- **Clear package cache if errors occur:**
  ```bash
  sudo pacman -Scc
  ```

---

## 📄 License
This guide is open-source under the [MIT License](LICENSE).

## 🙌 Contributing
Feel free to submit issues or pull requests to improve this guide.

---

**Happy Coding! 🚀**
