# 🦟 Mosquito Exterminator

A fun hand-tracking game built with **Python**, **Pygame**, **OpenCV**, and **MediaPipe**. Use your **real hand in front of a webcam** to swat mosquitoes — but watch out for the bees!

---

## 🎮 Gameplay

- Move your **open hand** in front of the webcam to aim the swatter
- **Close your fist** ✊ to swat insects
- **Kill mosquitoes** → gain points
- **Kill bees** → lose points (penalty!)
- As time progresses, **more bees spawn** — so stay sharp
- After the **first 30 seconds**, mosquitoes spawn twice as fast
- You have **60 seconds** — get the highest score you can!

---

## 🖥️ Requirements

- Python 3.8+
- A working **webcam**
- Linux / Windows / macOS

### Python Dependencies

| Package | Purpose |
|---|---|
| `pygame-ce` | Game window, rendering, audio |
| `opencv-python` | Webcam capture & image processing |
| `mediapipe` `0.10.30` | Hand landmark detection |
| `numpy` | Array operations |

---

## 🚀 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/Gyan-max/source-code-mosquito-game.git
cd source-code-mosquito-game
```

### 2. Install dependencies

```bash
pip3 install pygame-ce opencv-python mediapipe==0.10.30 numpy
```

> ⚠️ **Important:** Use `mediapipe==0.10.30` exactly. Newer versions (1.x) removed the legacy `mp.solutions` API and are **not compatible**.

> On Debian/Ubuntu systems that use externally-managed Python environments, add `--break-system-packages`:
> ```bash
> pip3 install pygame-ce opencv-python mediapipe==0.10.30 numpy --break-system-packages
> ```

### 3. Download the hand tracking model

The `hand_landmarker.task` model file is required for MediaPipe hand detection. It is already included in the repository (`source code/hand_landmarker.task`).

If missing, download it manually:
```bash
wget -O "source code/hand_landmarker.task" \
  "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
```

### 4. Run the game

```bash
cd "source code"
python3 main.py
```

---

## 🕹️ Controls

| Action | Gesture |
|---|---|
| **Move swatter** | Move open hand in front of webcam 🖐️ |
| **Swat / Hit** | Close your fist ✊ |
| **Quit** | Press `ESC` |

> Two windows will open: the **game window** (pygame) and a **webcam preview** window (OpenCV) showing your hand landmarks in real time.

---

## ⚙️ Configuration

All game settings are in [`source code/settings.py`](source%20code/settings.py):

| Setting | Default | Description |
|---|---|---|
| `SCREEN_WIDTH / HEIGHT` | `1200 x 700` | Game window resolution |
| `FPS` | `90` | Target frames per second |
| `GAME_DURATION` | `60` | Game length in seconds |
| `MOSQUITOS_SPAWN_TIME` | `1` | Seconds between insect spawns |
| `MOSQUITOS_MOVE_SPEED` | `min:1, max:5` | Insect movement speed range |
| `BEE_PENALITY` | `1` | Score penalty for killing a bee |
| `MUSIC_VOLUME` | `0.16` | Background music volume (0–1) |
| `SOUNDS_VOLUME` | `1` | Sound effects volume (0–1) |
| `DRAW_FPS` | `True` | Show FPS counter on screen |
| `DRAW_HITBOX` | `False` | Show hitboxes for debugging |

---

## 📁 Project Structure

```
source-code-mosquito-game/
├── source code/
│   ├── main.py              # Entry point — game loop
│   ├── game.py              # Core game logic & state
│   ├── menu.py              # Main menu screen
│   ├── hand.py              # Swatter sprite & hit detection
│   ├── hand_tracking.py     # MediaPipe hand landmark wrapper
│   ├── mosquito.py          # Mosquito sprite & behaviour
│   ├── bee.py               # Bee sprite & behaviour
│   ├── background.py        # Background rendering
│   ├── image.py             # Image loading utility
│   ├── ui.py                # UI helpers (text, buttons)
│   ├── settings.py          # All game configuration constants
│   ├── hand_landmarker.task # MediaPipe hand detection model
│   └── Assets/
│       ├── Sounds/          # Music & sound effects (.mp3, .wav)
│       └── Images/          # Sprites (hand, mosquito, bee, bg)
└── README.md
```

---

## 🔧 Troubleshooting

**`ModuleNotFoundError: No module named 'cv2'`**
→ Run: `pip3 install opencv-python --break-system-packages`

**`AttributeError: module 'mediapipe' has no attribute 'solutions'`**
→ You have mediapipe 1.x installed. Downgrade:
`pip3 install mediapipe==0.10.30 --break-system-packages`

**Webcam not detected**
→ Make sure no other app is using your camera. Check with: `ls /dev/video*`

**Game window doesn't open / SDL error**
→ On headless servers, set: `export DISPLAY=:0`

---

## 🛠️ Tech Stack

- **[Pygame-CE](https://pyga.me/)** — game engine & rendering
- **[OpenCV](https://opencv.org/)** — webcam capture
- **[MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)** — real-time hand landmark detection
- **[NumPy](https://numpy.org/)** — image array processing

---

## 📄 License

This project is open source. Feel free to use, modify, and share!
