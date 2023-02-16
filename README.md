# epl_passmaps

This code downloads pass maps for all teams in the English Premier League for the 2022 season from the website http://mclachbot.com/. The pass maps are downloaded and saved in separate directories for each team, with each pass map image saved as a .jpg file.

## How to use the code
Make sure you have the required libraries imported in your environment. The code uses the following libraries:

- requests
- beautifulsoup4
- os
- re
- urllib

Run the download_passmaps() function to start the download process.

The function will create a directory named "epl-pass-maps" on the desktop if it doesn't exist. Within this directory, it will create a subdirectory for each team and download the pass maps in .jpg format for each team in the 2022 season.

## Important notes
The pass maps are downloaded from a third-party website, and their availability is not guaranteed. The code will attempt to download all pass maps available for each team, but it may not be able to download all of them due to website errors or other issues.
The code is designed to save the pass maps in a specific directory on the desktop. If you want to change the directory, you will need to modify the code accordingly.

The pass maps are saved in a .jpg format. If you want to change the file format, you will need to modify the code accordingly.
