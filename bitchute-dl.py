#!/usr/bin/env python3

# region Imports
import requests
import argparse
import sys
import logging
import loadingbar

# endregion

# region Parsing Arguments
parser = argparse.ArgumentParser(
    prog='bitchute-dl',
    description='Program downloads bitchute mp4 from url',
    epilog='Thank you for downloading')

parser.add_argument('--url',
                    required=True,
                    help="Provide bitchute url",
                    dest="url")
parser.add_argument("--debug",
                    help="enable debug",
                    dest="debug",
                    default=False,
                    action="store_true")
args = parser.parse_args()

if args.debug is True:
    loggingLevel = logging.DEBUG
else:
    loggingLevel = logging.INFO
# endregion

# region logging
logging.basicConfig(format='%(asctime)-20s - %(levelname)s - %(message)s',
                    level=loggingLevel)

log = logging.getLogger()
# endregion

# region getting mp4 url
response = requests.get(args.url)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    log.error(f"Encountered error: {error}")
    sys.exit(-255)

log.info("url accepted")
log.debug("debug")

mp4List = []
for i in response.text.split("\n"):
    if "mp4" in i:
        mp4List.append(i)
if mp4List == []:
    log.debug("mp4 url not found")
    sys.exit(-255)

try:
    urlStart = (mp4List[0].find("https:"))
    urlEnd = (mp4List[0].find(".mp4"))
    urlDownload = mp4List[0][urlStart:urlEnd + 4]
except IndexError as error:
    log.error(f"Encountered {error}")
    sys.exit(-255)

log.info(urlDownload + " url")

fileName = (urlDownload.split("/"))[-1]
# endregion

# region downloading mp4 url
try:
    fd = open(fileName, "wb")
except (IOError, ValueError, EOFError) as error:
    log.error(f"Encountered {error}")
except:
    log.error("Encountered unknown error")

session = requests.Session()

request = session.get(urlDownload, stream=True)
try:
    request.raise_for_status()
except requests.exceptions.HTTPError as error:
    log.error(f"Encountered error: {error}")
    sys.exit(-255)

fileSize = (request.headers)["Content-Length"]
log.info("File size in Mb = " + str(round((int(fileSize) / (1024 * 1024)), 1)))
log.info("debug")

loadingBar = loadingbar.InternetLoadingBar(int(fileSize))

for chunk in request.iter_content(1024 * 1024):
    loadingBar.update(len(chunk))
    try:
        fd.write(chunk)
    except OSError as error:
        log.error(f"Encountered {error}")
        sys.exit(-255)

loadingBar.done()
fd.close()
log.info("Finished")
# endregion

# EOF
