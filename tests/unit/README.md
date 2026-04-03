# api-service

A simple API service built with Go.

## Overview

This project provides a basic API service with the following features:

*   Health check endpoint
*   Example endpoint returning a JSON response

## Getting Started

### Prerequisites

*   Go 1.18 or higher
*   Docker (optional, for containerization)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/api-service.git
    cd api-service
    ```

2.  Build the application:

    ```bash
    go build -o api-service main.go
    ```

### Running the Service

1.  Run the executable:

    ```bash
    ./api-service
    ```

2.  The service will start on port 8080 by default.  You can change this by setting the `PORT` environment variable.

    ```bash
    PORT=9000 ./api-service
    ```

### Running with Docker

1.  Build the Docker image:

    ```bash
    docker build -t api-service .
    ```

2.  Run the Docker container:

    ```bash
    docker run -p 8080:8080 api-service
    ```

## API Endpoints

*   `/health`:  Returns a simple "OK" response to indicate the service is running.
*   `/api/example`: Returns a JSON response with a sample data structure.

## Configuration

The service can be configured using environment variables:

*   `PORT`: The port the service listens on (default: 8080).

## Contributing

Contributions are welcome!  Please submit a pull request with your changes.

## License

[MIT](LICENSE)