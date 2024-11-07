# UNISLA UTS Participant Card Data Crawler

A Python-based data crawler for extracting participant card data for midterm exams (UTS) for Information Technology students at UNISLA. This tool automates the collection of participant card information, providing a streamlined approach for efficient data acquisition.

## Table of Contents

- [UNISLA UTS Participant Card Data Crawler](#unisla-uts-participant-card-data-crawler)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Requirements](#requirements)
  - [Contributing](#contributing)
  - [License](#license)
## Project Overview

The `crawling.py` script is designed to collect and save participant card data for UNISLA's Information Technology students during UTS exams. By utilizing web scraping techniques, the tool simplifies data gathering and minimizes manual effort.

## Features

- **Automated data crawling**: Quickly retrieves participant card information.
- **Data Storage**: Stores the extracted data in a structured format for easy access.
- **Error Handling**: Includes basic error handling to manage unexpected data structures or connection issues.

## Installation

To get started, clone this repository and ensure all required dependencies are installed:

```bash
git clone https://github.com/rulshrm/Crawling-Kartu-UTS-UNISLA.git
cd Crawling-Kartu-UTS-UNISLA
pip install -r requirements.txt
```
**Note:** Ensure that you have Python 3.8 or above.

## Usage

Run the crawling.py script to start the data collection process:

```bash
python crawling.py
```

This will execute the crawler, collecting the necessary participant card data. Data will be saved in the designated output format specified within the script `KARTU UTS MAHASISWA INFORMATIKA`.

## Configuration

Update configuration settings (such as URLs or output paths) directly in the crawling.py file or create a separate config file if required.

## Requirements

The following libraries are required to run this project:

- requests
- BeautifulSoup4
- urllib3
To install these dependencies, use:

```bash
pip install -r requirements.txt
```
## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with any enhancements, bug fixes, or additional features.

## License

This project is licensed under the MIT License - see LICENSE file for details.
