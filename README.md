# Discord Rich Presence Python Script

This README provides a detailed guide for setting up and using the provided Python script to display custom rich presence on Discord.

## Overview
The script utilizes the `pypresence` library to create and update a custom Rich Presence on Discord. This allows you to display custom text, images, and buttons in your Discord profile's activity section.

## Features
- Customizable details and state text.
- Large image with hover text.
- Two clickable buttons with custom labels and URLs.
- Optional timer to show elapsed time.

## Requirements
- Python 3.7 or higher.
- `pypresence` library installed.
- A Discord application created on the [Discord Developer Portal](https://discord.com/developers/applications).

## Setup Instructions

1. **Install Required Library**:
   Run the following command to install the `pypresence` library:
   ```bash
   pip install pypresence
   ```

2. **Create a Discord Application**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Click on "New Application" and give it a name.
   - Save the `Application ID` (required for the script).
   - Under the "Rich Presence" tab, upload assets (e.g., images) for your presence.

3. **Configure the Script**:
   - Replace `Your app id` with your Discord application's ID.
   - Set the `large_image` to the name of the uploaded image asset.
   - Customize the `details`, `state`, `large_text`, and `buttons` with your desired values.

4. **Run the Script**:
   - Save the script to a `.py` file.
   - Run the script using Python:
     ```bash
     python script_name.py
     ```
   - The presence should now appear in your Discord profile.

## Code Explanation

- **Initialization**:
  ```python
  RPC = Presence(app_id)
  RPC.connect()
  ```
  This initializes and connects the `pypresence` client to Discord.

- **Timer Option**:
  ```python
  start = None
  if time_elapsed == False:
      start = time.time()
  ```
  If `time_elapsed` is `False`, a timer will start to show elapsed time.

- **Presence Update**:
  ```python
  RPC.update(
      details='First line',
      state='Second Line',
      large_image='Image name',
      large_text='My image',
      buttons=[
          {"label": 'Your first label', "url": 'Your first Url'},
          {"label": 'Your second label', "url": 'Your second Url'}
      ],
      start=start
  )
  ```
  Updates the presence with custom text, image, and buttons.

- **Keep Alive**:
  ```python
  while True: time.sleep(15)
  ```
  Keeps the script running to maintain the Rich Presence.

## Notes
- Ensure that the image names and URLs are correct.
- The `pypresence` library requires an active internet connection to work.
- Discord Rich Presence is visible only on the desktop application.

## Troubleshooting
- If the presence does not appear:
  - Double-check the `Application ID` and asset names.
  - Ensure that the Discord application is running on your desktop.
- If errors occur, verify that the `pypresence` library is installed and up to date.

## Example Configuration
Here’s an example of a configured `RPC.update` block:
```python
RPC.update(
    details='Playing my favorite game',
    state='Leveling up!',
    large_image='game_icon',
    large_text='Gaming Time',
    buttons=[
        {"label": 'Join me', "url": 'https://example.com'},
        {"label": 'My Profile', "url": 'https://profile.example.com'}
    ]
)
```

Enjoy your customized Discord Rich Presence!

