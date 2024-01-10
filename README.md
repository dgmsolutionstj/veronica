1/09/2024

# Veronica v1.2 - Artificial Intelligent Personal Assistant

## Project Overview

Veronica is an open-source artificial intelligent personal assistant developed by DGTech Solutions LLC. It is designed to perform various tasks, including answering questions, providing weather information, retrieving Wikipedia articles, and more, all through voice commands.

## Table of Contents

- [Introduction](#veronica-v12---artificial-intelligent-personal-assistant)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

Veronica v1.2 comes with the following features:

- Speech recognition and synthesis capabilities
- Querying and summarizing information from Wikipedia
- Answering general knowledge questions
- Providing current time and date
- Performing calculations through Wolfram Alpha
- Retrieving real-time weather information for a specified city
- Personalized greetings based on the time of the day
- Customizable responses through intent configuration

## Getting Started

To get started with Veronica, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/veronica.git`
2. Navigate to the project directory: `cd veronica`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Configure API keys in the code: Replace 'YOUR_OPENWEATHERMAP_API_KEY' and 'YOUR_WOLFRAM_ALPHA_API_KEY' with your actual API keys.
5. Run the application: `python veronica.py`

## Dependencies

Veronica relies on the following Python modules:

- pyttsx3
- datetime
- wikipedia
- speech_recognition
- wolframalpha
- requests
- random
- json

Make sure to install these dependencies before running the application.

## Configuration

Veronica uses an 'intents.json' file for customizing responses. You can modify this file to add new intents or customize existing ones.

## Usage

Once the application is running, Veronica will greet you based on the time of the day. You can then issue voice commands for tasks such as checking the time, date, searching the web, calculating, checking the weather, and more.

To exit the application, use voice commands like "quit" or "exit."

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please contact DGTech Solutions LLC at [requests@dgtech.com](mailto:requests@dgtech.com).

---

© 2024 DGTech Solutions LLC. All Rights Reserved.
