#Import necessary packages
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADRESS = 'EMAIL'
PASSWORD = 'PASSWORD' 

#Define function to read contacts and return list of names and emails
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

#Read template file and return a template object with its contents
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts('contacts.txt')
    message_template = read_template('message.txt')

    #Set up the SMTP server
    s = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
    s.starttls()
    s.login(MY_ADRESS, PASSWORD)

    #For each contact, send email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()
        
        #Substitute actual name 
        message = message_template.substitute(PERSON_NAME=name.title())

        #Parameters of the message
        msg['From']= MY_ADRESS
        msg['To']=email
        msg['Subject']='Hello, friend'

        #Message body
        msg.attach(MIMEText(message, 'plain'))

        #Send the message via the server
        s.send_message(msg)

        del msg


if __name__ == '__main__':
    main()
