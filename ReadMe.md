# Mass Downloader (Version 1.0)

This is a mass downloader for Drupal 7 and Drupal 10 files. If a file is available (returns a 200 status code), then it will be downloaded into the "downloads" folder. If a file is unavailable (returns a 404 status code), then an error message will be printed to the terminal.

The Requests (Python) library sends out an HTTP GET request for data. When a webpage is available, users receive a 200 status code.

Note: Can use Financial & Support Services as an example

To use the program, follow the instructions below

1) Copy the links from the spreadsheet
2) Paste the links into the "scripts/input.txt" file
3) In "scripts/input.txt", use "CTRL" + "S" to save the changes
4) Navigate to the "scripts/script.py" file
5) To run the script file, either type "python scripts/script.py" in the terminal, or navigate to the top right corner and click the play button