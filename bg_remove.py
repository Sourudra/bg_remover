import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
#made by sourudra
st.set_page_config(layout="wide", page_title="Image Background Remover")

st.title("Remove Background From Your Image")
st.info('Upload your image on the sidebar on the left.')

if st.button("More Info"):
    st.text("The upload limit for images has been set to a maximum of 7 MB.")

st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 7 * 1024 * 1024 

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    

    try:
        fixed = remove(image)
        col2.write("Background Removed Image :scissors:")
        col2.image(fixed)
        st.sidebar.markdown("\n")
        with st.sidebar.expander("Download the edited image."):
            st.image(fixed, use_column_width=True, caption="The background is removed!!", output_format="PNG")
            st.download_button("Download", convert_image(fixed), "background_removed_image.png")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 7MB.")
    else:
        fix_image(upload=my_upload)

if my_upload is None:
    st.info ("Your edited image will appear here once uploaded and processed.")

else:
    st.success("Your edited image is ready for download from the sidebar on the left.")
