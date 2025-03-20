import canvas 
import io

def create_pdf(text, bucket_name):
    """
    Creates a PDF from text, uploads it to Google Cloud Storage, and returns the public URL.

    Args:
        text: The text content to be written to the PDF.
        bucket_name: The name of the Google Cloud Storage bucket.

    Returns:
        The public URL of the uploaded PDF, or None if an error occurred.
    """
    try:
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        textobject = c.beginText()
        textobject.setTextOrigin(inch, 7.5 * inch)  

        lines = text.split('\n')
        for line in lines:
            textobject.textLine(line)
        c.drawText(textobject)
        c.save()
        buffer.seek(0)  # Rewind the buffer to the beginning

        # 2. Upload to Google Cloud Storage
        if credentials_path:
            storage_client = storage.Client.from_service_account_json(credentials_path)
        else:
            storage_client = storage.Client() # use application default credentials

        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_file(buffer, content_type='application/pdf')

        # 3. Make the blob publicly accessible (Optional but needed for URL)
        blob.make_public()

        # 4. Return the public URL
        return blob.public_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None 