# openmuse

## Description
OpenMuse is a Python-based AI music generator designed specifically for macOS with Apple M1. It leverages advanced machine learning algorithms to create unique and high-quality music compositions. The project aims to provide an easy-to-use interface for generating music, making it accessible to both novice and experienced users.

## Features
- Generate music using AI
- Save generated music to a file
- Easy-to-use interface
- Optimized for macOS with Apple M1

## Setup Instructions
To set up the project on macOS for Apple M1, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mandaliyavatsal/openmuse.git
   cd openmuse
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the project:
   ```bash
   python setup.py install
   ```

## Usage Instructions
To generate music using the AI, follow these steps:

1. Import the `MusicGenerator` class:
   ```python
   from openmuse.music_generator import MusicGenerator
   ```

2. Create an instance of the `MusicGenerator` class:
   ```python
   music_generator = MusicGenerator()
   ```

3. Generate music:
   ```python
   music = music_generator.generate_music()
   ```

4. Save the generated music to a file:
   ```python
   music_generator.save_music(music, 'output_file.mid')
   ```

## Dependencies
- Python 3.8 or higher
- TensorFlow 2.4.0
- NumPy 1.19.5
- Music21 5.7.1

## Contributing
We welcome contributions to the OpenMuse project! If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Commit your changes
4. Push the branch to your fork
5. Create a pull request

Please make sure to follow the coding standards and write tests for your changes.
