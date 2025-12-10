# Simple Python Web Server

A minimal HTTP server built with Python's standard library that serves a "Hello World" HTML page. (demo to show sync to github)

## Description

This project demonstrates how to create a basic web server using Python's built-in `http.server` module. It serves a simple HTML page with no external dependencies required.

## Requirements

- Python 3.x

## Installation

No installation required beyond having Python installed on your system.

## Usage

1. Run the server:
   ```bash
   python server.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

3. You should see a "Hello World!" message displayed on the page.

4. To stop the server, press `Ctrl+C` in the terminal.

## How It Works

The server listens on `localhost` at port `8000` and responds to GET requests with a simple HTML page. The `HelloHandler` class extends `BaseHTTPRequestHandler` to define custom behavior for handling HTTP requests.

## Customization

- To change the port, modify the port number in the `HTTPServer` initialization (currently `8000`)
- To serve different content, edit the HTML string in the `do_GET` method
- To change the host, modify `'localhost'` to your desired hostname or IP address

## License

This is a simple example project provided for educational purposes.
