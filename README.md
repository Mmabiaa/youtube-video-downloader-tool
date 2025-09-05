
# YouTube Video Downloader Tool

A versatile tool to download YouTube videos, audio, and subtitles using Python. This project includes both a command-line interface (CLI) and a Flask web application for user-friendly access.

![YouTube Video Downloader](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)
[![Watch the video](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID)

## Features

- **Download Videos**: Download videos in the highest resolution or select from available qualities.
- **Download Audio**: Option to download audio only.
- **Download Subtitles**: Download subtitles if available.
- **Search Functionality**: Search for videos directly from the application.
- **Batch Downloads**: Download multiple videos at once by entering multiple URLs.
- **Web Interface**: Access the downloader through a web browser using Flask.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```
git clone https://github.com/mmabiaa/youtube-video-downloader-tool.git
cd youtube-video-downloader-tool
```

### Set Up a Virtual Environment (Optional but Recommended)

```
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
```

### Install Dependencies

`pip install -r requirements.txt`

## Usage

### Command-Line Interface (CLI)

To run the command-line version:

1. **Download Videos**:

`python downloader.py`

Follow the prompts to enter one or more YouTube video URLs.

2. **Search for Videos**:

`python search.py`

Enter your search query to find videos on YouTube.

### Web Application

To run the Flask web application:

1. **Start the Flask App**:

`python app.py`

2. **Access the Application**:

Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Download Videos via Web Interface**:

Enter a YouTube video URL in the provided input field and click "Download".

## Example Commands

- To download a single video:
```
python downloader.py
Enter YouTube video URL: https://www.youtube.com/watch?v=VIDEO_ID
```

- To download multiple videos:
```
python downloader.py
Enter YouTube video URLs (comma-separated): https://www.youtube.com/watch?v=VIDEO_ID1, https://www.youtube.com/watch?v=VIDEO_ID2
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps [CONTRIBUTION](CONTRIBURION.md):

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [pytube](https://github.com/nficano/pytube) for providing an easy way to download videos from YouTube.
- [Flask](https://flask.palletsprojects.com/) for creating the web application.

## Contact

For any inquiries or issues, please open an issue in this repository or contact me directly.

---

_Last updated: January 10, 2025_
