from app import *
from app import app

def capturar(file_path):
    project_id ='119257377126'
    location = 'us' # Format is 'us' or 'eu'
    processor_id ='7a7253cb985a49f2' # Create processor in Cloud Console
    file_path = file_path # The local file in your current working directory gcloud config set project my-project-document-329520
    ENDPOINT = 'https://us-documentai.googleapis.com/v1/projects/119257377126/locations/us/processors/7a7253cb985a49f2:process'
    res = []
    res = process_document(project_id,location ,processor_id,file_path)
    return res


