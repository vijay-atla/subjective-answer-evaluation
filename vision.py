import os

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io

    credential_path = r#"Service Account Token Path"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    docText=response.full_text_annotation.text
    return docText



    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



