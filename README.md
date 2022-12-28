# bitchute-dl

## About

bitchute-dl will download any video from the BitChute video platform, said video will be inside the directory that bitchute-dl is in. This project was for my 
father and for myself as project to improve in my pthon skills.

## Installation

### Linux / Windows
- install python 
- install pip
- install or validate that you have dependancy modules (requests, argparse, sys, logging, loadingbar)

#### Exec option-1 (Linux / Windows)
```
python bitchute-dl.py -h
```
#### Exec option-2 (Linux)
```
chmod 755 python-dl.py
./bitchute-dl.py -h
```

## Sample exec
```
hasar@sharki:~/dev/bitchute-dl-1.0$ python bitchute-dl.py --url https://www.bitchute.com/video/15vV8oZr62m1/
2022-12-28 11:59:44,807 - INFO - url accepted
2022-12-28 11:59:44,808 - INFO - https://seed167.bitchute.com/kzQXMRfiCqov/15vV8oZr62m1.mp4 url
2022-12-28 11:59:45,157 - INFO - File size in Mb = 24.4
2022-12-28 11:59:45,157 - INFO - debug
██████████████████████████████████████████████████ 25.6M 67.0M/s  0sec  
2022-12-28 11:59:45,751 - INFO - Finished
hasar@sharki:~/dev/bitchute-dl-1.0$ ll
```


