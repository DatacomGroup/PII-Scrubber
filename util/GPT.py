from openai import AzureOpenAI
import json
# import config
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    
# Set up OpenAI API using the configuration
config['openai']['api_key']
config['openai']['api_type']
config['openai']['api_base']
config['openai']['api_version']

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    api_key = config['openai']['api_key'],
    api_version=config['openai']['api_version'],
    azure_endpoint=config['openai']['azure_endpoint']
)

def new_file_path(filename_):
    # split . and / and replace with redacted.
    n_filename = filename_.split('.')
    n_filename = n_filename[0] + ' Redacted.' + n_filename[1]
    return n_filename

def find_sensitive_data(doc):
    # read txt files FewShot1_Assistant.txt and FewShot1_User.txt
    with open('FewShot1_Assistant.txt', 'r') as file:
        assistant = file.read()
    with open('FewShot1_User.txt', 'r') as file:
        user = file.read()
    
    prompt = "Find all Phone numbers, Email address, Street address, Suburbs, Cities, Postcodes, People names, Company names, URLs, Server names, Credit card number, Bank account number, IP address, Usernames, Passwords, Passport numbers, Driver’s license number and Dates: doc --Find all Phone numbers, Email address, Street address, Suburbs, Cities, Postcodes, People names, Company names, URLs, Server names, Credit card number, Bank account number, IP address, Usernames, Passwords, Passport numbers, Driver’s license number, Dates:-->"
    messages = [
        {"role": "system",
         "content": "You are an AI assistant that helps people highlight data in documents."},
    
        {"role": "user",
         "content": user
        },
        {"role": "assistant",
         "content": assistant
        },
        {"role": "user",
         "content": prompt + doc 
        }
    ]
    completion = client.chat.completions.create(
        model="gpt35test",  # e.g. gpt-35-instant
        messages=messages,
        
    )
    return completion.choices[0].message.content

def redact_with_chatGPT(doc):

    prompt = "Replace URLs, Email addresses, Home/street address, Passport numbers, Driver’s license number, Telephone number, mobile numbers, Date of Birth, Credit card number, Bank account number, IP address, Usernames, Passwords, Server names which could look like technical jargon, People names, Company names and business with [redacted]:"
    messages=[{"role":"system","content":"You are an AI assistant that helps people find information."},
            {"role":"user","content":prompt+doc},
    ]
    completion = client.chat.completions.create(
        model="gpt35test",  # e.g. gpt-35-instant
        messages=messages,
        temperature=0.5,
        max_tokens=1000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,        
    )
    
    return completion.choices[0].message.content