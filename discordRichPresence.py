import time
from pypresence.presence import Presence
app_id = 'Your app id'
time_elapsed = True

RPC = Presence(app_id)
RPC.connect()


start = None
if time_elapsed == False:
    start = time.time()


RPC.update(
    details='First line',
    state='Second Line' ,
    large_image='Image name',
    large_text='My image',
    buttons=[
        {
            "label": 'Your first label',
            "url": 'Your first Url'
        },
        {
            "label": 'Your second label',
            "url": 'Your second Url'
        }

    ],
    start=start
)

print('Discord Rich Presence launched!')

while True: time.sleep(15)