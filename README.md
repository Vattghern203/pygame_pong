# Running a Pygame and Setting Up a Virtual Environment

This guide will walk you through the process of running a Pygame and setting up a virtual environment for your project.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.6 or higher)
- Git (for cloning the repository)

## Steps

### 1. Clone the Repository

First, you need to clone the repository containing your Pygame project. Open your terminal and run the following command:

```bash
git clone https://github.com/Vattghern203/pygame_pong.git

cd pygame_pong

```
### 2. Create the Virtual Enviroment(venv)
```py
python -m venv venv

venv/Scripts
```

on CMD use: ```bash activate.bat```

on PowerShell: ```bash .\activate.ps1```

now run: ```bash cd ../..``` to return to the root of the project

### 3. Install depedencies

```py
pip install -r requirements.txt
```

### 4. Run the Game

```bash
python main.py
```

### 5. Enjoy!

🎮