import os
import tempfile
import win32com.client
import pyoutlook
import pandas as pd
import PyPDF2

# Specify your Outlook email address and password
email_address = "your_email@example.com"
password = "your_password"

# Initialize the Outlook client
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
outlook.Logon(email_address, password)

# Connect to your SharePoint or local folder
# Replace 'your_sharepoint_folder' with the actual path to your SharePoint folder or local directory
folder_path = 'your_sharepoint_folder'

# Function to download attachments from email
def download_attachments(mail_item):
    for attachment in mail_item.Attachments:
        if attachment.FileName.endswith('.pdf') or attachment.FileName.endswith('.xlsx'):
            attachment.SaveAsFile(os.path.join(folder_path, attachment.FileName))

# Function to read attachments from the folder
def read_attachments_from_folder():
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(folder_path, filename)
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    pdf_text = page.extractText()
                    print(f"Contents of Page {page_num + 1} in {filename}:\n{pdf_text}")
        elif filename.endswith('.xlsx'):
            excel_file = pd.read_excel(os.path.join(folder_path, filename))
            # Process the Excel file as needed

# Iterate through your Outlook emails and download attachments
for mail_item in outlook.GetDefaultFolder(6).Items:  # 6 corresponds to the Inbox folder
    download_attachments(mail_item)

# Read attachments from the folder
read_attachments_from_folder()

# Log out of Outlook
outlook.Logoff()
