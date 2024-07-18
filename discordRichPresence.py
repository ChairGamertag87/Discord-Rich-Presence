import time
from pypresence.presence import Presence
app_id = '1233899778534801418'
time_elapsed = True

RPC = Presence(app_id)
RPC.connect()


start = None
if time_elapsed == False:
    start = time.time()


RPC.update(
    details='Just some ',
    state='Working on 1.0.6' ,
    large_image='hydromel',
    large_text='My mod',
    buttons=[
        {
            "label": 'Download Hydromel',
            "url": 'https://www.curseforge.com/minecraft/mc-mods/hydromel'
        },
        {
            "label": 'Hydromel News',
            "url": 'https://discord.gg/GXQBXWMj7s'
        }

    ],
    start=start
)

print('Hydromel Discord Rich Presence launched!')

while True: time.sleep(15)