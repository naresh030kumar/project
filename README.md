# Color Detection App

A web app that detects the color name and RGB values at any pixel you click on an uploaded image.

## Features

- Upload an image (jpg, png).
- Click anywhere on the image to get:
  - RGB values
  - Closest color name from the dataset
  - Color box as reference

## Setup

1. Clone this repo:
   ```
   git clone https://github.com/naresh030kumar/color-detector.git
   cd color-detector
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   streamlit run app.py
   ```

## Deployment

Deploy easily on [Streamlit Cloud](https://share.streamlit.io/) or [Render](https://render.com/).

## Dataset

Edit `colors.csv` to add more colors.

## Example

![demo](demo.png)
