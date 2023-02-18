# epl_passmaps

This script downloads pass maps for English Premier League teams from the website http://mclachbot.com/, saves them as image files, and then compiles them into a video. The resulting video shows the pass map for each game a team played during the 22/23 season.

## How to use the code
Make sure you have the required libraries imported in your environment. The code uses the following libraries:

- Python 3
- pandas
- BeautifulSoup
- requests
- urllib
- OpenCV
- numpy

Run the download_passmaps() function to start the download process.

The function will create a directory named "epl-pass-maps" on the desktop if it doesn't exist. Within this directory, it will create a subdirectory for each team and download the pass maps in .jpg format for each team in the 2022 season.

## Important notes
The pass maps are downloaded from a third-party website, and their availability is not guaranteed. The code will attempt to download all pass maps available for each team, but it may not be able to download all of them due to website errors or other issues.
The code is designed to save the pass maps in a specific directory on the desktop. If you want to change the directory, you will need to modify the code accordingly.

The pass maps images are saved in a .jpg format and the videos are saved in mp4 format. If you want to change the file format, you will need to modify the code accordingly.
