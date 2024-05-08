# Streamlit Survey Automation

A web application  to clean IVR Data for Analytics Purposes.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ivr-cleaning-automation.streamlit.app/)

---

## Overview
The IVR Data Processing Suite is a comprehensive toolset designed for cleaning, processing, and analyzing IVR (Interactive Voice Response) campaign data. It utilizes a combination of Streamlit and FastAPI to provide an intuitive user interface for file uploads, data cleaning, questionnaire definition, keypress decoding, and data analysis. The suite is split into three main components: IVR Data Cleaner & Pre-Processor App, Questionnaire Definer, and Keypresses Decoder, which are built to work seamlessly together or as standalone modules.

## Getting Started

### Prerequisites
- Docker
- Python 3.8 or newer

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory and build the Docker container:
   ```sh
   cd <project-directory>
   docker build -t ivr-data-suite .
   ```
3. Run the Docker container:
   ```sh
   docker run -p 8501:8501 ivr-data-suite
   ```

### Project Structure

```
.
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── requirements.txt
├── .streamlit
│   └── secrets.toml
├── fastapiapp
│   ├── dockerfile
│   ├── security_utils.py
│   ├── test.db
│   ├── app
│   │   ├── main.py
│   │   └── modules
│   │       ├── aws_utils.py
│   │       ├── crud.py
│   │       ├── data_cleaner_utils_page1.py
│   │       ├── dependencies.py
│   │       ├── keypress_decoder_utils_page3.py
│   │       ├── questionnaire_utils_page2.py
│   │       ├── schemas.py
│   │       └── ...
│   ├── tests
│   │   └── tests_main.py
│   └── images
│       └── invoke_logo.png
└── mainapp
    ├── 1_IVR_Data_Cleaner_Pre_Processor_App.py
    ├── modules
    │   ├── data_cleaner_utils_page1.py
    │   ├── keypress_decoder_utils_page3.py
    │   ├── questionnaire_utils_page2.py
    │   └── security_utils.py
    └── pages
        ├── 2_Questionnaire_Definer.py
        └── 3_Keypresses_Decoder.py
```

## Usage

### IVR Data Cleaner & Pre-Processor App

- **Objective**: To clean and preprocess IVR data for analysis.
- **Features**: Upload IVR files, visualize basic statistics, download cleaned data, and manage phone numbers for future sampling.

### Questionnaire Definer

- **Objective**: To define and structure the questionnaire from IVR campaigns.
- **Features**: Upload script files, parse questions and answers, rename data columns, and prepare data for further processing.

### Keypresses Decoder

- **Objective**: To decode and categorize keypress responses from IVR campaigns.
- **Features**: Upload script or JSON files for decoding, classify responses, and download the decoded data for analysis.

### FastAPI App Integration

- **Objective**: To integrate the Streamlit apps with a FastAPI backend for advanced data processing and storage capabilities.
- **Setup**: Refer to the `fastapiapp` directory and Dockerfile for setup and deployment instructions.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---
