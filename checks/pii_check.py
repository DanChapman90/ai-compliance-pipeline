import re

# Toggle for testing: True = make it pass, False = make it fail
PASS_MODE = True

sample_text_pass = """
Hello team,

Please review the attached report. No sensitive data included here.

Thanks,
Data Compliance Officer
"""

sample_text_fail = """
Hello team,

Here is the customer list:

Name: John Doe
Email: john.doe@example.com
Phone: +1-555-123-4567

Handle with care!

Thanks,
Data Compliance Officer
"""

text_to_check = sample_text_pass if PASS_MODE else sample_text_fail

# Simple regex patterns for email and phone numbers
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+?\d[\d\-\s]{7,}\d'

found_emails = re.findall(email_pattern, text_to_check)
found_phones = re.findall(phone_pattern, text_to_check)

if found_emails or found_phones:
    print(f"❌ PII check failed! Found emails: {found_emails}, phones: {found_phones}")
    exit(1)
else:
    print("✅ PII check passed! No emails or phone numbers found.")
