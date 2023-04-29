import streamlit as st
from google.cloud import storage

# Set up Google Cloud Storage client
client = storage.Client()
bucket_name = "your-bucket-name"
bucket = client.get_bucket(bucket_name)

def upload_file(file):
    blob = bucket.blob(file.name)
    blob.upload_from_string(file.read(), content_type=file.type)
    return blob.public_url

def list_files():
    files = [blob.name for blob in client.list_blobs(bucket_name)]
    return files

file = st.file_uploader("Choose a file")
if file:
    if st.button("Upload"):
        url = upload_file(file)
        st.success(f"File uploaded to {url}")

files = list_files()
st.write("Files in your storage:")
for f in files:
    st.write(f)
