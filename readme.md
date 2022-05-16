![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/seafu47/CMPE131_final-project)
![Lines of code](https://img.shields.io/tokei/lines/github/seafu47/CMPE131_final-project)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/seafu47/CMPE131_final-project)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/seafu47/CMPE131_final-project)
# UShop
## Team 7
- Xiyuan Zhou (@xiyuanzhou)
- Jiaheng Fang (@seafu47) 
- Rommel Aquino Jr (@RommelAquinoJr) 
- Ahmet Mutlugun (@ahmetmutlugun) @ Team Lead

## Installation
Run: `pip install -r requirements.txt` to install the required dependincies.  
Run: `python3 run.py` to start the website through localhost.

## How does it work?
Our website uses flask with python to create a shopping interface. Bycrypt and SQLAlchemy are used to hash and securely store user credentials.

## 12 Functional Features

1. Login - Xiyuan Zhou ✅
2. Logout - Xiyuan Zhou ✅
3. Create Account - Xiyuan Zhou ✅
4. Delete Account - Ahmet Mutlugun ✅
5. Search Items - Rommel Aquino Jr ✅
6. Post Items - Rommel Aquino Jr, Xiyuan Zhou ✅
7. Delete Item - Xiyuan Zhou ❌
8. Purchase/Bid on Item - Ahmet Mutlugun ❌
9. User Profile - Ahmet Mutlugun, Rommel Aquino Jr ✅
10. Edit Item - Ahmet Mutlugun, Jiaheng Fang ❌
11. Add pictures - Jiaheng Fang, Ahmet Mutlugun ✅
12. Sorting - Ahmet Mutlugun, Xiyuan Zhou ✅

## 4 Non-functional Requirements

## Non-functional Requirements

1. Chinese Language - Xiyuan Zhou, Jiaheng Fang ❌
2. Turkish Language - Ahmet Mutlugun ❌
3. Dark Mode - Ahmet Mutlugun ✅
4. Smooth interface - Jiaheng Fang, Ahmet Mutlugun, Xiyuan Zhou, Rommel Aquino Jr ✅

## Extra Feature: Docker
First, build the docker image for the flask app.
```
docker build --tag ushop .   
```
Next, run the docker image.
```
docker run -p PORT:PORT ushop
```
Replace "PORT" with the port used for the app. 4999 is the default for our app.

