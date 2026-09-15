# Multi Container Weather App

A containerized real-time weather application demonstrating a simple DevOps workflow with Flask, Nginx, Docker Compose, and Jenkins.

## Features

- Search real-time weather by city
- Flask REST API backend
- Responsive HTML/CSS/JavaScript frontend
- Nginx-based frontend container
- Docker Compose orchestration
- Jenkins CI/CD-style pipeline for build and deployment
- OpenWeatherMap API integration

## Tech Stack

**Frontend:** HTML5, CSS3, JavaScript  
**Backend:** Python, Flask, Flask-CORS  
**API:** OpenWeatherMap  
**DevOps:** Docker, Docker Compose, Jenkins, Nginx

## Project Structure

```text
weather-devops-project/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   ├── nginx.conf
│   └── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── .env.example
└── .gitignore
```

## Run Locally

### 1. Configure the API key

Copy `.env.example` to `.env` and set your OpenWeatherMap API key:

```env
OPENWEATHER_API_KEY=<openweathermap_api_key>
```

### 2. Start the application

```bash
docker compose up --build
```

### 3. Open the frontend

Visit:

```text
http://localhost:3000
```

The Flask API runs at:

```text
http://localhost:5000
```

## Jenkins Pipeline

The `Jenkinsfile` automates:

1. Docker version checks
2. Stopping existing containers
3. Building application images
4. Starting containers with Docker Compose
5. Verifying running containers

The Jenkins agent must have Docker and Docker Compose available.

## API Endpoint

```text
GET /weather/<city>
```

Example:

```text
http://localhost:5000/weather/Mysuru
```

## Security Note

API credentials are intentionally not stored in the repository. Configure `OPENWEATHER_API_KEY` through the local `.env` file or your deployment environment.

## Future Improvements

- Add automated tests
- Add GitHub Actions CI
- Add health checks and container monitoring
- Use Nginx as a reverse proxy for the API
- Deploy to AWS
