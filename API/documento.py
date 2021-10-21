import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

project_id ='119257377126'
location = 'us' # Format is 'us' or 'eu'
processor_id ='7a7253cb985a49f2' # Create processor in Cloud Console
file_path ='otro.pdf' # The local file in your current working directory gcloud config set project my-project-document-329520
ENDPOINT = 'https://us-documentai.googleapis.com/v1/projects/119257377126/locations/us/processors/7a7253cb985a49f2:process'



def process_document(project_id=project_id, location=location, processor_id=processor_id,  file_path=file_path):

    # Set endpoint to EU
    # Instantiates a client
    from google.cloud import documentai_v1beta3 as documentai


    client = documentai.DocumentProcessorServiceClient()



    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()

    # Read the file into memory
    document = {"content": image_content, "mime_type": "application/pdf"}

    # Configure the process request
    request = {"name": name, "document": document}

    # Use the Document AI client to process the sample form
    result = client.process_document(request=request)

    document = result.document
    document_text = document.text


    document_pages = document.pages
    lista = []

    for page in document_pages:
        print("Page Number:{}".format(page.page_number))
        for form_field in page.form_fields:
            fieldName=get_text(form_field.field_name,document)
            nameConfidence = round(form_field.field_name.confidence,4)
            fieldValue = get_text(form_field.field_value,document)
            valueConfidence = round(form_field.field_value.confidence,4)
            #print(fieldName+fieldValue +"  (Confidence Scores: "+str(nameConfidence)+", "+str(valueConfidence)+")")
            print(fieldName+fieldValue)
            lista.append(fieldName+fieldValue)
        print(lista)
        fin = []
        for x in lista:
            key,value = x.strip("\n").split(':')[:2]
            otro = key,value
            fin.append(otro)
            print(f"key{key}=>{value}")
        print("holaaa")
        print(fin)
        return fin



def get_text(doc_element: dict, document: dict):
    """
    Document AI identifies form fields by their offsets
    in document text. This function converts offsets
    to text snippets.
    """
    response = ""
    # If a text segment spans several lines, it will
    # be stored in different text segments.
    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]
    return response

process_document()
