# Streamlit IVR Survey Automation Project Documentation
A web application  to clean IVR Data for Analytics Purposes.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ivr-cleaning-automation.streamlit.app/)

## Project Overview

The Streamlit IVR (Interactive Voice Response) Survey Automation project aims to streamline the process of cleaning and preparing IVR survey data for analytics. This web application simplifies the often complex and time-consuming task of data processing, allowing analysts to focus more on extracting insights rather than data manipulation. Leveraging FastAPI for backend services and Streamlit for the frontend, the project offers a user-friendly interface for users to upload, process, and analyze their IVR survey data efficiently.

## Getting Started

### Prerequisites

- Docker: The application is containerized using Docker, ensuring consistent environments across different systems.
- Python 3.8 or later: Required for local development and running the application outside Docker.

### Installation and Setup

1. **Clone the Repository**: Begin by cloning the project repository to your local machine.
   ```
   git clone https://github.com/fahmizainal17/streamlit_ivr_survey_automation.git
   ```
2. **Navigate to the Project Directory**:
   ```
   cd streamlit_ivr_survey_automation
   ```
3. **Build and Run the Docker Container**:
   - To build the Docker container, execute:
     ```
     docker build -t streamlit_ivr_survey_app .
     ```
   - Once the build is complete, run the container:
     ```
     docker run -p 8501:8501 streamlit_ivr_survey_app
     ```
   This will start the Streamlit server, and the application will be accessible at `http://localhost:8501`.

### Project Structure

- **`.devcontainer`**: Contains configurations for setting up a development container in VSCode, ensuring a consistent development environment.
- **`.structure`**: Describes the project's architecture, facilitating understanding and navigation of the project layout.
- **`.surveyscript`**: Holds scripts related to survey data processing, including data cleaning, transformation, and analysis scripts.
- **`fastapiapp`**: The FastAPI application directory, containing backend logic and APIs for handling data processing tasks.
- **`images`**: Contains images used within the Streamlit application for UI enhancement.
- **`mainapp`**: The main Streamlit application scripts, responsible for rendering the web interface and interacting with the backend FastAPI services.
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`Dockerfile`**: Defines the Docker container specifications for the project.
- **`LICENSE`**: The project's license file.
- **`README.md`**: Provides an overview of the project, setup instructions, and other essential information.
- **`requirements.txt`**: Lists all Python dependencies required for the project.

## Usage

After successfully starting the application, navigate to `http://localhost:8501` in your web browser. The Streamlit interface provides intuitive options to upload your IVR survey data, specify cleaning and processing parameters, and initiate the data analysis process. Results can be viewed directly within the web application, and processed datasets can be downloaded for further analysis or reporting purposes.

## Development

For developers looking to contribute or customize the application, refer to the `.devcontainer` directory for setting up a development environment with VSCode. This ensures that all developers work within a consistent environment, minimizing the "it works on my machine" problem.

## Contributing

Contributions are welcome, and they can be made by following these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
