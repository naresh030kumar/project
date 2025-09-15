import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import io

# Load the color dataset
@st.cache_data
def load_colors():
    df = pd.read_csv('colors.csv')
    return df

def closest_color_name(r, g, b, df):
    # Calculate distance to each color in the dataset
    colors = df[['R', 'G', 'B']].values
    dists = np.sqrt(np.sum((colors - np.array([r, g, b]))**2, axis=1))
    idx = np.argmin(dists)
    return df.iloc[idx]['color_name']

def main():
    st.title("Color Detection App 🎨")

    st.write("Upload an image and click anywhere to detect the color at that pixel.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("Click on the image below to detect color:")
        # Streamlit image click returns coordinates
        clicked = st.image(image, use_column_width=True, output_format="PNG")
        # Use Streamlit's experimental image coordinates feature
        coords = st.experimental_get_image_coordinates("image")

        if coords:
            x, y = int(coords['x']), int(coords['y'])
            arr = np.array(image)
            # y is row, x is column
            r, g, b = arr[y, x]
            st.write(f"**Coordinates:** ({x}, {y})")
            st.write(f"**RGB:** ({r}, {g}, {b})")

            df = load_colors()
            color_name = closest_color_name(r, g, b, df)

            st.write(f"**Closest Color Name:** {color_name}")

            # Show color box
            color_box = f"rgb({r}, {g}, {b})"
            st.markdown(
                f"<div style='width:100px; height:50px; background:{color_box}; border:1px solid #000;'></div>",
                unsafe_allow_html=True
            )
        else:
            st.info("Click on the image to detect color.")

if __name__ == '__main__':
    main()