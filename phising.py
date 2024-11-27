import re
import tldextract

# List of known suspicious domains (for demonstration purposes)
suspicious_domains = [
    "example-phish.com", "malicious-website.org", "phishy-site.net"
]

# Common phishing words and patterns in URLs
phishing_keywords = [
    "login", "verify", "account", "update", "secure", "confirm", "banking"
]

# Helper function to extract domain name from a URL
def extract_domain(url):
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

# Function to check if the URL matches phishing patterns
def is_phishing_url(url):
    # Check if domain is in suspicious list
    domain = extract_domain(url)
    if domain in suspicious_domains:
        print(f"Suspicious Domain Found: {domain}")
        return True
    
    # Check for common phishing keywords in the URL path
    for keyword in phishing_keywords:
        if keyword in url.lower():
            print(f"Suspicious Keyword Found: {keyword}")
            return True
    
    # Check for unusual characters or structure, like many subdomains
    if url.count(".") > 3 or len(url) > 100:
        print("Unusual URL structure detected.")
        return True

    return False

# Collect URLs from the user
def get_urls_from_user():
    urls = []
    print("Enter the URLs you want to check (type 'done' when finished):")
    while True:
        url = input("Enter a URL: ")
        if url.lower() == 'done':
            break
        urls.append(url)
    return urls

# Get URLs to check
urls = get_urls_from_user()

# Scan each URL
for url in urls:
    print(f"Scanning URL: {url}")
    if is_phishing_url(url):
        print("Phishing link detected!\n")
    else:
        print("URL seems safe.\n")

