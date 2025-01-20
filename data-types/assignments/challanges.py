#Check if a string contains only certain characters
import re

def is_allowed_string(string):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pattern.match(string))

print(is_allowed_string("Welcome254"))  
print(is_allowed_string("Welcome@254")) 


#Match a string with 'a' followed by anything, ending in 'b'

def match_a_followed_by_anything_ending_b(string):
    pattern = re.compile(r'a.*b$')
    return bool(pattern.match(string))

print(match_a_followed_by_anything_ending_b("anneb"))  
print(match_a_followed_by_anything_ending_b("127b")) 
print(match_a_followed_by_anything_ending_b("animal"))   
print(match_a_followed_by_anything_ending_b("a254b"))   


#Validate user input using regex
#PASSWORD validation


def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z]).{8,}$')
    return bool(pattern.match(password))

print(is_valid_password("ALCHEMY123"))
print(is_valid_password("ALCHEMY")) 

#Date format validation
def is_valid_date(date_string):
    pattern = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    return bool(pattern.match(date_string))

print(is_valid_date("16/01/2025"))
print(is_valid_date("16-01-2025")) 

#Extracting specific info from a string
#EMAILS
def extract_emails(text):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return pattern.findall(text)

text = "Email us at Zindua@info.com and Onbonding@zindua.co.ke"
print(extract_emails(text)) 

#phone numbers
def extract_phone_numbers(text):
    pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
    return pattern.findall(text)

text = "Call us 0756478936 or 0753490864"
print(extract_phone_numbers(text))

#Search and replace text in a string
import re

def replace_mr_with_ms(text):
    return re.sub(r'\bMr\.\b', 'Ms.', text)

text = "Mr. Mwangi is gone. Mr. Kamuau has arrived."
print(replace_mr_with_ms(text))









