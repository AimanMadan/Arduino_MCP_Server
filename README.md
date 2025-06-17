# Arduino MCP Server: Control Your Arduino with AI!

Welcome to the Arduino MCP Server project! This project lets you control an Arduino board from your computer using a special connection called **MCP (Model Context Protocol)**. Think of it like giving instructions to your Arduino using a smart AI assistant!

## What is this project for?

In this project, we're building a "server" that listens for commands from an AI (like Claude Desktop). When the AI tells it to, our Arduino will turn on or off some LEDs. This is a super cool way to see how AI can interact with the real world!

## What you'll need

Before we start, make sure you have:

* **An Arduino board:** Any Arduino board like an Uno or Nano will work.
* **Two LEDs:** One white and one red.
* **Two 1k Resistors:** These are important to protect your LEDs.
* **Jumper wires:** To connect everything.
* **USB cable:** To connect your Arduino to your computer.
* **Claude Desktop:** This is the AI assistant we'll be using.
* **Python 3.12 or higher:** Our code is written in Python.
* **`uv` (Ultrafast Python package installer and resolver):** We use this to manage our Python libraries.
* Claude Desktop

## How to set up your Arduino

1.  **Connect the LEDs:**
    * **White LED:** Connect the longer leg (positive) of the white LED to **Digital Pin 12** on your Arduino through a 220 Ohm resistor. Connect the shorter leg (negative) to a **GND** (Ground) pin on your Arduino.
    * **Red LED:** Connect the longer leg (positive) of the red LED to **Digital Pin 11** on your Arduino through a 220 Ohm resistor. Connect the shorter leg (negative) to a **GND** (Ground) pin on your Arduino.

    *(Remember to always use a resistor with LEDs to prevent them from burning out!)*

2.  **Upload the StandardFirmataPlus sketch:**
    * Open the Arduino IDE (Integrated Development Environment).
    * Go to Library `Library Manager` > Search and download `Firmata` 
    * Go to `File` > `Examples` > `Firmata` > `StandardFirmata`.
    * Select your Arduino board from `Tools` > `Board`.
    * Select the correct Port from `Tools` > `Port`.
    * Upload the `StandardFirmata` sketch to your Arduino board. This program allows Python to control your Arduino.

## Getting the Python code ready

1.  **Download the project:** If you haven't already, download or clone this project to your computer.
2.  **Open your terminal/command prompt:** Navigate to the folder where you saved this project.
3.  **Install Python dependencies:** We'll use `uv` to install everything our Python code needs.


    ```bash
    uv pip install
    ```
    This command reads the `pyproject.toml` file and installs the `fastmcp` and `pyfirmata2` libraries.

## Understanding the Python Code (`main.py`)

Let's take a quick look at the main parts of our Python code:

* `from fastmcp import FastMCP`: This line imports the `FastMCP` library, which helps us create our MCP server.
* `import pyfirmata2`: This line imports `pyfirmata2`, which is a library that lets Python talk to your Arduino.
* `Arduino = pyfirmata2.Arduino('/dev/cu.usbmodem212201')`: **IMPORTANT!** You need to change `'/dev/cu.usbmodem212201'` to the **COM port** that your Arduino is connected to. You can find this in the Arduino IDE under `Tools` > `Port`. It might look something like `COM3` on Windows or `/dev/ttyUSB0` on Linux.
* `@ArduinoMCP.tool`: These special lines (`@ArduinoMCP.tool`) are called "decorators." They tell `FastMCP` that the function right below them is a "tool" that the AI client can use.
* `white_led_ON()`, `red_led_ON()`, `led_OFF()`: These are our functions (mini-programs) that tell the Arduino to turn the white LED on, the red LED on, or both LEDs off.
* `ArduinoMCP.run()`: This line starts our MCP server, making it ready to receive commands!

## Setting up Claude Desktop

Now, let's tell Claude Desktop how to connect to our Arduino server.

1.  **Open your MCP Client** in this case `Claude Desktop`
2.  Go to `Settings` > `Developer` > `Edit Config` > and open the config file `claude_desktop_config.json`
2.  **Copy and paste what is below and update the path:**
    ```json
    {
        "mcpServers": {
            "arduino": {
                "command": "/Users/aiman/.local/bin/uv", # this too
                "args": [
                    "--directory",
                    "/Users/aiman/Dev/Arduino_MCP", # update to the path 
                    "run",
                    "main.py"
                ]
            }
        }
    }
    ```
    * **`"command"`:** This should be the full path to your `uv` executable. If you're on Windows, it might be something like `C:\Users\YourUser\AppData\Local\uv\uv.exe`. On macOS/Linux, it's often in your user's local bin directory as shown.
    * **`"--directory"`:** This should be the **full path** to the `Arduino_MCP` folder on your computer where your `main.py` file is located. Make sure this path is correct!
    * **`"run", "main.py"`:** These tell `uv` to run your `main.py` script.

## Running the Project!

1.  **Start Claude Desktop.**
2.  **The MCP server should start automatically.** Claude Desktop will use the `claude_desktop_config.json` file to launch your Arduino MCP server. 
3.  **Talk to Claude!** Now you can ask Claude to control your Arduino. Try saying things like:
    * "Turn on the white LED."
    * "Turn on the red LED."
    * "Turn off all LEDs."

    Claude Desktop will understand your commands and send them to your Arduino MCP server, which will then tell your Arduino what to do!



Have fun controlling your Arduino with AI! This is just the beginning of what you can do!


