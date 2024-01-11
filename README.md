1/09/2024 - 1/10/2024

# Veronica v2.0 - AI Personal Assistant

## Project Overview

Veronica v2.0 is an upgraded version of the open-source artificial intelligent personal assistant developed by DGTech Solutions LLC. The project is now organized into modular Python files: `brain.py`, `neurons.py`, `voice.py`, and `ears.py`. These files collectively enhance the user experience by introducing task management capabilities and improved modularity.

## Table of Contents

- [Introduction](#veronica-v20---ai-personal-assistant)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [User Manual](#user-manual)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

Veronica v2.0 introduces the following features:

- Modular organization of code into `brain`, `neurons`, `voice`, and `ears`.
- Task management capabilities: add, save, delete, and review notes.
- Improved voice synthesis and recognition.
- Enhanced natural language processing for a wider range of commands.
- Integration with Wikipedia, Wolfram Alpha, and Google Search for information retrieval.
- Real-time weather information retrieval.
- Customizable responses through intent configuration.
- Time and date information retrieval.

## Getting Started

To get started with Veronica v2.0, follow the steps below:

1. Clone the repository: `git clone https://github.com/your-username/veronica.git`
2. Navigate to the project directory: `cd veronica`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Configure API keys in `neurons.py`: Replace 'YOUR_OPENWEATHERMAP_API_KEY' and 'YOUR_WOLFRAM_ALPHA_API_KEY' with your actual API keys.
5. Run the application: `python brain.py`

## Installation

Veronica v2.0 requires the following Python packages. You can install them using the provided `requirements.txt` file:

```plaintext
pyttsx3==2.90
datetime
wikipedia==1.4.0
SpeechRecognition==3.8.1
wolframalpha==5.0.0
requests==2.26.0
```

Install the dependencies by running `pip install -r requirements.txt`.

## Usage

Run the application by executing `python brain.py`. Veronica will greet you based on the time of day and respond to voice commands. You can use commands for tasks such as checking the time, date, adding, saving, deleting, and reviewing notes, searching the web, calculating, checking the weather, and more.

To exit the application, use voice commands like "quit" or "exit."

## User Manual

1. **Adding a Note:**
   - Command: "add note [your note]"
   - Example: "add note Remember to buy groceries."

2. **Saving Notes:**
   - Command: "save note"
   - Example: "save note"

3. **Deleting a Note:**
   - Command: "delete note [note to delete]"
   - Example: "delete note Buy groceries."

4. **Reviewing Notes:**
   - Command: "review note"
   - Example: "review note"

5. **Google Search:**
   - Command: "search google [your search query]"
   - Example: "search google OpenAI GPT-4."

6. **Weather Information:**
   - Command: "weather [city]"
   - Example: "weather New York."

7. **Time and Date:**
   - Command: "time" or "date"
   - Example: "time" or "date"

8. **Wikipedia Search:**
   - Command: "search [your search query]"
   - Example: "search Artificial Intelligence."

9. **Wolfram Alpha Calculation:**
   - Command: "calculate [your calculation]"
   - Example: "calculate 2 + 2."

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please contact DGTech Solutions LLC at [requests@dgtech.com](mailto:requests@dgtech.com).

---

© 2024 DGTech Solutions LLC. All Rights Reserved.
